from django.db import models
from userprofile.models import UserProfile


class Project(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)  # Field to mark featured projects
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp field

    def __str__(self):
        return self.title



    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='work_exp')
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='education')
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    graduation_date = models.DateField()

class Certification(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='certification')
    name = models.CharField(max_length=255)
    date_obtained = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True) 