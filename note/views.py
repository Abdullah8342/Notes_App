from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


class CustomSignup(FormView):
    form_class = UserCreationForm
    template_name = 'note/signup.html'
    success_url = reverse_lazy('Login')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class NoteView(LoginRequiredMixin,ListView):
    model = Note
    fields = '__all__'
    template_name = 'note/NoteView.html'
    context_object_name = 'notes'


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            content = Note.objects.filter(user = self.request.user,title__icontains = query)
        else:
            content = Note.objects.filter(user = self.request.user)
        return content

        

class NoteDetail(LoginRequiredMixin,DetailView):
    model = Note
    fields = '__all__'
    template_name = 'note/NoteDetails.html'
    context_object_name = 'note'


class NoteCreate(LoginRequiredMixin,CreateView):
    model = Note
    fields = ['title','content']
    template_name = 'note/NoteCreate.html'
    success_url = reverse_lazy('NoteView')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDelete(LoginRequiredMixin,DeleteView):
    model = Note
    template_name = 'note/DeleteNote.html'
    success_url = reverse_lazy('NoteView')


class NoteUpdate(LoginRequiredMixin,UpdateView):
    model = Note
    template_name = 'note/UpdateNote.html'
    fields = ['title','content']
    success_url = reverse_lazy('NoteView')
