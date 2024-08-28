from django.urls import path
from .views import login_view, dashboard_view, diet_questionnaire_view, logout_view
from .views import home_view  # Make sure this line is present

urlpatterns = [
    path("", home_view, name="home"),  # Add this line
    path("login/", login_view, name="login"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("diet-questionnaire/", diet_questionnaire_view, name="diet_questionnaire"),
    path("logout/", logout_view, name="logout"),
]
