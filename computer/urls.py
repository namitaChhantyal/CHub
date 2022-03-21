from django.urls import path

from computer.views import(
    IndexView,
    ComputerDetailsView,
    FormView,
    UpdateViewForm,
    IndividualDetailView,
    LogoDetailView
)

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('details/',ComputerDetailsView.as_view(),name='details'),
    path('form/',FormView.as_view(),name='form'),
    path('update/<int:pk>',UpdateViewForm.as_view(),name='update'),
    path('individualdetail/<int:pk>',IndividualDetailView.as_view(),name='individualdetail'),
    path('logodetail/<str:brandname>',LogoDetailView.as_view(),name='logodetail'),
    

]

