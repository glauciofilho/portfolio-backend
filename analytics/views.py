from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .services.ga_queries import (
    get_overview,
    get_countries,
    get_project_events,
)

@require_GET
def analytics_overview(request):
    try:
        return JsonResponse(get_overview(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@require_GET
def analytics_countries(request):
    try:
        return JsonResponse(get_countries(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@require_GET
def analytics_projects(request):
    try:
        return JsonResponse(get_project_events(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)