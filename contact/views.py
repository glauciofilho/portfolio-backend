import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings

from .models import ContactMessage


@csrf_exempt
def send_contact_message(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return JsonResponse(
            {"error": "All fields are required"},
            status=400
        )

    contact = ContactMessage.objects.create(
        name=name,
        email=email,
        message=message,
        ip_address=request.META.get("REMOTE_ADDR"),
        user_agent=request.META.get("HTTP_USER_AGENT", ""),
    )

    send_mail(
        subject=f"Novo contato - {name}",
        message=f"""
Nome: {name}
Email: {email}

Mensagem:
{message}
        """,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.CONTACT_EMAIL_RECEIVER],
    )

    return JsonResponse({"success": True}, status=201)