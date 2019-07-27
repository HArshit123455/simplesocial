from django.core.management.base import  BaseCommand
from posts.models import Post

class Command(BaseCommand):
    def handle(self,*args,**options):
        Post.objects.all().delete()
