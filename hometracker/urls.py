
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
urlpatterns = [
    # path('', RedirectView.as_view(url='/dashboard/')),  # Redirect to the dashboard
    path('admin/', admin.site.urls),
    # path('assignmenttracker/', include('assignmenttracker.urls')),
    path('', include('assignmenttracker.urls')),
]
