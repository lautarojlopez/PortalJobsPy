from django.shortcuts import render

# Create your views here.
def mi_cv(request):
    return render(request, 'mi-cv.html')