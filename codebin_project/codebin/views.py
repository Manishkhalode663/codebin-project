from django.shortcuts import render,redirect
from  .forms import SnippetForm
from . import models

# Create your views here.
def home(request):    
    snippets = models.Snippet.objects.all()
    return render(request, 'codebin/home.html', {'snippets': snippets})
 


def create_snippet_view(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            
            snippet.save()
            return redirect('home')
    else:
        form = SnippetForm()
    return render(request, 'codebin/create_snippet.html', {'form': form})


def view_snippet(request,id):
    snippet = models.Snippet.objects.get(id=id)
    return render(request, 'codebin/view_snippet.html', {'snippet': snippet})


def delete_snippet(request,id):
    snippet = models.Snippet.objects.get(id=id)
    snippet.delete()
    return redirect('home')


def edit_snippet(request,id):
    snippet = models.Snippet.objects.get(id=id)
    if request.method == 'POST':
         
        form = SnippetForm(request.POST,instance=snippet)
        if form.is_valid():
                              
            form.save()
            return redirect('home')
    
    else:
        form = SnippetForm(instance=snippet)
        
        return render(request, 'codebin/edit_snippet.html', {'form': form})