from django.http import HttpResponseNotFound
from django.template import loader

def custom_404_view(request, exception):
    template = loader.get_template('app/error/404.html')
    return HttpResponseNotFound(template.render())

handler404 = custom_404_view