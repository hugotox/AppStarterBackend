from django.conf import settings
from django.urls import re_path, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from api.auth import LoginView, WhoAmI, LogoutView
from api.views import TestEndPoint, TestJSON

urlpatterns = [
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('whoami', WhoAmI.as_view()),
    # TODO: check if we can user graphql and csrf cookie
    path('api/graphql', csrf_exempt(GraphQLView.as_view(graphiql=settings.DEBUG))),
    re_path(r'^data/(?P<id>\w+)/$', TestEndPoint.as_view()),
    re_path(r'^static/test.json/$', TestJSON.as_view()),
]
