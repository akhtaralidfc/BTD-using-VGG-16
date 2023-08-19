from django.urls import path
from . import views

app_name = "classify"

urlpatterns = [
    path("", views.classify_image, name="classify_image"),
    path("contact.html/", views.contact, name="contact"),
    # path('upload/', views.upload_image, name='upload_image'),
    # path('view/<int:pk>/', views.view_image, name='image_view'),
]
