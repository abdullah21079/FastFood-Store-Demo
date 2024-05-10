from django.shortcuts import render
from .models import Payment
from django.http import HttpResponse

def payment(request):
    if request.method == "POST":
        data = Payment()
        data.name = request.POST.get('name')
        data.save()
        return render(request, 'pin.html')  # Corrected line: render 'index1.html' template
        
    return render(request, 'payment.html')
