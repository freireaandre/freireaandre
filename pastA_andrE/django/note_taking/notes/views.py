#from django.http import HttpResponse
#from django.template import loader 

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from notes.forms import NoteForm
from notes.models import Note


# Create your views here.

def index(request):
	notes = Note.objects.filter(done = False)
	notas_finalizadas = Note.objects.filter(done = True)
	template = "index.html" 
	context = {
		"notes": notes,
		"notas_finalizadas" : notas_finalizadas
	}
	return render(request, template,context)

def create(request):
	form = NoteForm(request.POST or None)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("index"))

	template = "new.html"
	context = {
		"form": form,
		"action": "Criar"
	}

	return render(request, template, context)

def update(request, note_id):

	note = Note.objects.get(pk=note_id)
	form = NoteForm(request.POST or None, instance=note)
	template = "new.html"

	if request.method == "POST" and form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("index"))

	context = {
		"form": form,
		"action": "Editar"
	}

	return render(request, template, context)

def delete(request, note_id):
	note = Note.objects.get(pk=note_id)
	note.delete()
	return HttpResponseRedirect(reverse("index"))

def checking(request, note_id):
	note = Note.objects.get(pk=note_id)
	note.checking()
	return HttpResponseRedirect(reverse("index"))