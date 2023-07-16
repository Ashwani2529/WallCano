from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "NASA"
admin.site.site_title = "NASA Admin Portal"
admin.site.index_title = "Welcome to NASA Researcher Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls'))
]