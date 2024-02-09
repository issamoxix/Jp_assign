from django.urls import path
from .views import SubmitLegalRequestView, LegalRequestView

urlpatterns = [
    path("requests", SubmitLegalRequestView.as_view(), name="submit-legal-request"),
    path("requests/<int:id>", LegalRequestView.as_view(), name="get-legal-request"),

]
