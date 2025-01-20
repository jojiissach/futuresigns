from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import IndexView,ContactView,PortfolioView

urlpatterns = [
    path('', IndexView.as_view(), name='index-page'),
    path('contact-us', ContactView.as_view(), name='contact-page'),
    path('portfolio', PortfolioView.as_view(), name='portfolio-page'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

