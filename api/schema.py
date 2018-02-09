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
    all_owners = graphene.List(OwnerType)
    all_pets = graphene.List(PetType)

    def resolve_all_owners(self, info, **kwargs):
        return Owner.objects.all()

    def resolve_all_pets(self, info, **kwargs):
        return Pet.objects.select_related('owner').all()
