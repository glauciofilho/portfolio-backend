from django.urls import path
from .views import project_list, project_detail, file_detail, resume

urlpatterns = [
    path("projects/", project_list),
    path("projects/<int:project_id>/", project_detail),
    path("files/<int:id_project>/<int:id_file>/", file_detail),

    path("resume/", resume),
]