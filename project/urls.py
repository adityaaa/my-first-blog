"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
	 
	#url(r'^$','homepage.views.home'),
    url(r'^articles/',include('article.urls')),
    url(r'^admin/', include(admin.site.urls)),
    


	url(r'^accounts/login/$', 'project.views.login'),
	url(r'^accounts/auth/$', 'project.views.auth_view'),
	url(r'^accounts/logout/$', 'project.views.logout'),
	url(r'^accounts/loggedin/$', 'project.views.loggedin'),
	url(r'^accounts/invalid/$', 'project.views.invalid_login'),
	url(r'^accounts/register/$', 'project.views.register_user'),
	url(r'^accounts/register_success/$', 'project.views.register_success'),
]