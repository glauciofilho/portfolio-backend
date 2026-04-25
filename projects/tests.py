from django.test import TestCase, Client
from django.urls import reverse
import json
from .models import Project, Stack, StackProject, File, Profile

class ProjectsEndpointTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Create Stack
        self.stack = Stack.objects.create(name="Python", badge_url="http://python.badge")
        
        # Create Project
        self.project = Project.objects.create(
            name_pt="Projeto Teste",
            name_en="Test Project",
            summary_pt="Resumo",
            summary_en="Summary",
            image_url="http://image.url"
        )
        
        # Create StackProject link
        StackProject.objects.create(project=self.project, stack=self.stack)
        
        # Create File
        self.file = File.objects.create(
            project=self.project,
            path="src/main.py",
            content_pt="print('Olá')",
            content_en="print('Hello')"
        )
        
        # Create Profile
        self.profile = Profile.objects.create(
            resume_pdf_pt="http://resume.pt",
            resume_pdf_en="http://resume.en"
        )

    def test_project_list(self):
        response = self.client.get("/api/projects/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Test Project") # Default is 'en'
        self.assertEqual(data[0]["stacks"][0]["name"], "Python")

        response_pt = self.client.get("/api/projects/?lang=pt")
        self.assertEqual(response_pt.status_code, 200)
        data_pt = response_pt.json()
        self.assertEqual(data_pt[0]["name"], "Projeto Teste")

    def test_project_detail(self):
        response = self.client.get(f"/api/projects/{self.project.id}/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["project"]["name"], "Test Project")
        self.assertEqual(len(data["files"]), 1)

    def test_project_detail_not_found(self):
        response = self.client.get("/api/projects/999/")
        self.assertEqual(response.status_code, 404)

    def test_file_detail(self):
        response = self.client.get(f"/api/files/{self.project.id}/{self.file.id}/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["content"], "print('Hello')")

        response_pt = self.client.get(f"/api/files/{self.project.id}/{self.file.id}/?lang=pt")
        data_pt = response_pt.json()
        self.assertEqual(data_pt["content"], "print('Olá')")

    def test_resume(self):
        response = self.client.get("/api/resume/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["resume_url"], "http://resume.en")

        response_pt = self.client.get("/api/resume/?lang=pt")
        self.assertEqual(response_pt.json()["resume_url"], "http://resume.pt")
