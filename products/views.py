from django.template import loader
from django.http import HttpResponse

# Create your views here.
def products(request):
  template = loader.get_template('myfirst1.html')
  return HttpResponse(template.render())