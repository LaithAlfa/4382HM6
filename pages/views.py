

# Create your views here.
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'Index.html'
	
class AboutPageView(TemplateView):
	template_name = 'About.html'