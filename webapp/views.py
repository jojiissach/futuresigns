from django.shortcuts import render
from django.views import View

# Create your views here.

class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        """
        Render the custom login page.
        """
        return render(request, self.template_name)
    
class ContactView(View):
    template_name = "contact/contact.html"

    def get(self, request):
        """
        Render the custom login page.
        """
        return render(request, self.template_name)

class PortfolioView(View):
    template_name = "portfolio/portfolio.html"

    def get(self, request):
        """
        Render the custom login page.
        """
        return render(request, self.template_name)