from django.conf.urls import patterns, include, url
from rest_framework import generics
from resume import models
from resume import serializers
from resume import userviews

urlpatterns = patterns('',
    url(r'^resumes/?$', userviews.ListOrCreateOwnerAPIView.as_view(model=models.Resume, serializer_class=serializers.ResumeSerializer)),
    url(r'^resumes/(?P<user__username>[^/]+)/?$', userviews.ListResumeAPIView.as_view(model=models.Resume, serializer_class=serializers.FullResumeSerializer)),
    url(r'^workexperiences/?$', userviews.ListOrCreateSubResumeObjectAPIView.as_view(model=models.WorkExperience, serializer_class=serializers.WorkExperienceSerializer)),
    url(r'^educations/?$', userviews.ListOrCreateSubResumeObjectAPIView.as_view(model=models.Education, serializer_class=serializers.EducationSerializer)),
    url(r'^users/?$', generics.CreateAPIView.as_view(model=models.User, serializer_class=serializers.NewUserSerializer, permission_classes=())),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
