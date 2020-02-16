from django.shortcuts import render
from .models import Excursion

# Create your views here.
def index(request):
	params = {"history":Excursion.objects.raw('SELECT * FROM excursionapp_excursion')}
	return render(request, "index.html", params)
