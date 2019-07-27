from django.core.management.base import  BaseCommand
from groups.models import Group,GroupMember

class Command(BaseCommand):
    def handle(self,*args,**options):
        Group.objects.all().delete()
        GroupMember.objects.all().delete()
