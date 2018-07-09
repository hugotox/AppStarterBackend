import graphene
from graphene_django.types import DjangoObjectType
from api.models import Owner, Pet


class OwnerType(DjangoObjectType):
    class Meta:
        model = Owner


class PetType(DjangoObjectType):
    class Meta:
        model = Pet


class Query(object):
    some_bool_field = graphene.Boolean(value=graphene.Boolean())
    hello = graphene.String(name=graphene.String(default_value="Hugo"))
    all_owners = graphene.List(OwnerType)
    all_pets = graphene.List(PetType)

    def resolve_some_bool_field(self, info, value):
        return value

    def resolve_hello(self, info, name):
        return 'Hello ' + name

    def resolve_all_owners(self, info, **kwargs):
        return Owner.objects.all()

    def resolve_all_pets(self, info, **kwargs):
        return Pet.objects.select_related('owner').all()
