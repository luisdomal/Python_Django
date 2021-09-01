"""Products app URL config"""

from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),  # products:list
    path("new/", views.ProductCreateView.as_view(), name="create"),  # products:create
    path("checkout/<int:pk>", views.checkout, name="checkout"),  # products:checkout
    path("editor/", views.permisos_v2, name="permisos"),  # products:checkout
]
