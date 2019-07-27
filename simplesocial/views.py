from django.views.generic import TemplateView
from django.shortcuts import render
STATIC_URL = '/static/'
def index(request):
    media= {'media': STATIC_URL }
    return render(request,'index.html',media)
class TestPage(TemplateView):
    template_name='test.html'
class Thankspage(TemplateView):
    template_name='thanks.html'
