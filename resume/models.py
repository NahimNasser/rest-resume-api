from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """
    Base model abstract class that allows having a timestamp and creation stamp on every model
    """
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class Resume(BaseModel):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

    @property
    def workexperience(self):
        return self.workexperience_set.all()

    @property
    def education(self):
        return self.education_set.all()


class WorkExperience(BaseModel):
    resume = models.ForeignKey(Resume)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)


class Education(BaseModel):
    resume = models.ForeignKey(Resume)
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
