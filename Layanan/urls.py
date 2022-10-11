from django.urls import path


from . import views


urlpatterns = [
    path('',views.Mylayanan,name='service'),
    path('upload',views.upload,name='upload'),
    path('render-json/<str:name_file>/',views.PostJSONListView.as_view(),name='render_json'),
    # path('render-json', views.postjson_wthoutrequired.as_view(), name='render_jsons'),
    path('check_data',views.check_data,name='check_data'),

]