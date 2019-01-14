from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Paste


class PasteCreate(CreateView):
	model = Paste
	fields = ['text','name']
	
		
