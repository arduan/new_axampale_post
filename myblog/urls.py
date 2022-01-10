from django.urls import path



from myblog import views

urlpatterns = [

    path('', views.show),
    path('test/<int:id_title>', views.one_show, name='title-text'),
    path('my_form/', views.get_name, name='form'),
    path('about/', views.about, name='about'),








]