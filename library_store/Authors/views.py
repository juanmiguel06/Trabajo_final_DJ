from django.shortcuts import render, redirect

# Create your views here.
from Authors.models import Author

def authors(request):
    authors_list = Author.objects.all()
    return render(request, 'authors/index.html', {'author_list': authors_list})

def change_status_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    author.status = not author.status
    author.save()
    return redirect('authors')