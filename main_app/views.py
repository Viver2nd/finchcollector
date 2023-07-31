from django.shortcuts import render

# Create your views here.

finches = [
  {'name': 'Brambling', 'color': 'Orange / Brown'},
  {'name': 'Crossbill', 'color': 'Red / Black'},
  {'name': 'Goldfinch', 'color': 'Yellow / Red'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches,
    })