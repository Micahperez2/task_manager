from django.shortcuts import render

# Create your views here.
def budget(request):
    return render(request, 'budget/budget.html')
