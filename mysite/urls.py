from django.conf.urls import include, url
from django.contrib import admin
#from django.urls import path

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #这是由于在django2.0后不支持使用在urls.py中写
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),

    #path('admin/', admin.site.urls),


]
