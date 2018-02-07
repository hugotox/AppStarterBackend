from django.urls import re_path

from api.views import TestEndPoint, TestJSON

urlpatterns = [
    re_path(r'^data/(?P<id>\w+)/$', TestEndPoint.as_view()),
    re_path(r'^static/test.json/$', TestJSON.as_view()),
]
