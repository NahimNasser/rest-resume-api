from models import *
from rest_framework import serializers


class NewUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')

    def restore_object(self, attrs, instance=None):
        if instance:  # Update
            user = instance
            user.username = attrs['username']
            user.email = attrs['email']
        else:
            user = User(username=attrs['username'], first_name=attrs['first_name'], last_name=attrs['last_name'], email=attrs['email'],
            is_staff=False, is_active=True, is_superuser=False)
            user.set_password(attrs.get('password'))
            user.save()
        return user


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('created_at', 'modified_at')
        depth = 0


class UserSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = User
        exclude = ('password', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'groups', 'user_permissions')


class ResumeSerializer(BaseModelSerializer):
    user = UserSerializer()

    class Meta(BaseModelSerializer.Meta):
        model = Resume


class WorkExperienceSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = WorkExperience


class EducationSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Education


class FullResumeSerializer(ResumeSerializer):

    user = UserSerializer()
    workexperience = WorkExperienceSerializer()
    education = EducationSerializer()

    class Meta(ResumeSerializer.Meta):
        model = Resume
        fields = ('user', 'workexperience', 'education', 'location', 'industry', 'title')
        depth = 0
