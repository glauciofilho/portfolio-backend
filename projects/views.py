from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Project, File, Profile

def project_list(request):
    lang = request.GET.get("lang", "en")

    projects = []
    for p in Project.objects.all():
        projects.append({
            "id": p.id,
            "name": p.name_pt if lang == "pt" else p.name_en,
            "summary": p.summary_pt if lang == "pt" else p.summary_en,
            "created_at": p.created_at,
            "image_url": p.image_url,
            "stacks": [
                {
                    "id": link.stack.id,
                    "name": link.stack.name,
                    "badge_url": link.stack.badge_url
                }
                for link in p.stack_links.select_related("stack")
            ]
        })

    return JsonResponse(projects, safe=False)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    lang = request.GET.get("lang", "en")



    files = [
        {
            "id": f.id,
            "path": f.path
        }
        for f in project.files.all()
    ]

    data = {
        "project": {
            "id": project.id,
            "name": project.name_pt if lang == "pt" else project.name_en,
            "summary": project.summary_pt if lang == "pt" else project.summary_en,
            "created_at": project.created_at,
        },
        "files": files
    }

    return JsonResponse(data)

def file_detail(request, id_project, id_file):
    lang = request.GET.get("lang", "en")

    file = get_object_or_404(
        File,
        id=id_file,
        project_id=id_project
    )

    data = {
        "id": file.id,
        "path": file.path,
        "content": file.content_pt if lang == "pt" else file.content_en
    }

    return JsonResponse(data)



def resume(request):
    lang = request.GET.get("lang", "en")
    profile = Profile.objects.first()
    if not profile:
        return JsonResponse({"error": "Profile not found"}, status=404)
    if lang == "pt":
        resume_url = profile.resume_pdf_pt
    else:
        resume_url = profile.resume_pdf_en
    return JsonResponse({
        "resume_url": resume_url
    })