from django.shortcuts import render
from django.db.models import Q
from project2.books.models import Book

def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(title__icontains=query)|
			Q(authors__first_name__icona=tains=query) |
			Q(authors__last_name__icontians=query)
		)
		results = Book.objects.filter(qset).distinct()
	else:
		result = []
	return render("books/search.html", {
		"result": results,
		"query": query
	})

# Create your views here.
