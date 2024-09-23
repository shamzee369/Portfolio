from.import views
from django.urls import path
urlpatterns=[path('portfolio',views.addproject, name='portfolio'),
             path('porteducation', views.addeducation,name='portedu'),
             path('wrk',views.addwrkexp,name='wrkexp'),
             path('cert',views.addcertifi,name='certifi'),
             path('proshow',views.project_showcase,name='proshow'),
             path('all-projects/', views.all_users_projects_showcase, name='allproshow')
            #  path('portfoliousers/<str:username>/projects/', views.user_project_showcase, name='userproshow')

             
             
             
             ]