from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')
 
def error_404(request):
    data = {}
    return render(request,'404.html', data)
 
def error_500(request):
    data = {}
    return render(request,'500.html', data)