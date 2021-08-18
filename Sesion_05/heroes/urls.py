"""Heroes app URL config"""

from django.urls import path

from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register("", views.HeroesViewSet)

app_name = "heroes"
urlpatterns = router.urls


# URLs normales

# urlpatterns = [
#     # FBV
#     # path("", views.heroes_list, name="list"),
#     # path("<int:pk>", views.heroes_detail, name="detail"),
#     # CBV
#     path("", views.HeroesListView.as_view(), name="list"),
#     path("<int:pk>", views.HeroesDetailView.as_view(), name="detail"),
# ]