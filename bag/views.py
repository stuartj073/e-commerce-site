from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ View to see bag page """
    return render(request, 'bag/bag.html')