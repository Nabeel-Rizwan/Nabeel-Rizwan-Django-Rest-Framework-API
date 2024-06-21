from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf.urls.static import static 
from django.conf import settings 
from django.urls import include, path, re_path
from django.views.static import serve
## import debug_toolbar 


urlpatterns = [
    path('admin/', admin.site.urls),        ## Admin Panel created by default through django
    path('api/',include('app.urls')),   ##  Include urls.py from app
    path('',home),   ##  Home page url which is defined in views.py (project)
##  path('__debug__/',include(debug_toolbar.urls)),  ## Toolbar to check the performance

re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),

]

admin.site.site_header = 'API CONTROL PANEL'    ## Admin Panel heading
admin.site.index_title = 'CONTROL'      ## Admin Panel Index Title
admin.site.site_title = 'API CONTROL PANEL'     ## Admin Panel Site title