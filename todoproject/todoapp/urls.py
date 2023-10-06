from . import views
from django.urls import path

urlpatterns = [

    path('',views.add, name='add'),
    # path('details/',views.details, name='details')
    path('delete/<int:id>/',views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('list/',views.Tasklistview.as_view(), name='list'),
    path('detail/<int:pk>/', views.Taskdetailview.as_view(), name='detail'),
    path('edit/<int:pk>/', views.Taskupdateview.as_view(), name='edit'),

]