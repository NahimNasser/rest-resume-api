from rest_framework.generics import ListCreateAPIView, ListAPIView
from models import *


class ListOrCreateOwnerAPIView(ListCreateAPIView):
    def pre_save(self, obj):
        obj.user = self.request.user


class ListOrCreateSubResumeObjectAPIView(ListCreateAPIView):
    def pre_save(self, obj):
        obj.resume = self.request.user.resume


class ListResumeAPIView(ListAPIView):
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        return Resume.objects.filter(**self.kwargs)
