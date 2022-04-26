from django.contrib import admin
from django.urls import path,include
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('todo/', views.TodoView.as_view(), name='TodoView'),
    path('user/', views.CreateUser.as_view(), name='CreateUser'),
    path('api/user/', include('userapp.urls')),


    path("app-models-<str:appname>/",views.GetAppModels.as_view(),name="GetAppModels"),
    path("model-fields-<str:appname>-<str:modelname>/",views.GetModelFields.as_view(),name="GetModelFields"),




    
    path("all-in-one-<str:appname>-<str:modelname>/",views.AllInOne.as_view(),name="AllInOne"),
    path("all-in-one-<str:appname>-<str:modelname>/<int:pk>/",views.AllInOne.as_view(),name="AllInOne"),
]
