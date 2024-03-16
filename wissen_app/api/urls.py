from django.urls import path, include
from wissen_app.api.views import user_list, user_details, ProjectAV, ProjectDetailAV

urlpatterns = [
    path('user/list/', user_list, name='user-list'),   
    path('user/<int:pk>', user_details, name='user-details'),
    path('project/list/', ProjectDetailAV.as_view(), name='project'),
    path('project/', ProjectDetailAV.as_view(), name='project'),
    path('project/<int:pk>', ProjectAV.as_view(), name='project-details')
]
