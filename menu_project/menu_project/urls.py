from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path(
        '<path:path>/',
        TemplateView.as_view(template_name='index.html'),
        name='home'
    ),
    path(
        'pc/',
        TemplateView.as_view(template_name='index.html'),
        name='pc'
    )
]
