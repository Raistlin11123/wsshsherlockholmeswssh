from . import views
from django.urls import path
from django.contrib import auth as auth_

urlpatterns = [
    path('', views.index, name='index'),
    path('scenario', views.scenario, name='scenario'),
    path('rules', views.rules, name='rules'),
    path('login', views.login_view, name='login'),
	path('logout', views.logout_view, name='logout'),
    path('list_clues', views.list_clues, name='list_clues'),
    path('content_clue/<int:id_clue>', views.content_clue, name='content_clue'),
    path('enumeration', views.enumeration, name='enumeration'),
    path('loaderio-a8cb860e9a4d3106db44400adfc87f3e', views.loderio, name='loderio'),

    #path('login', auth_views.LoginView.as_view(template_name= 'investigation1/login.html'), name='login'),
]