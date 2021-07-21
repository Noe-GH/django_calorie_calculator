from django.shortcuts import render, redirect
from .models import Aliment, Consumption

def index(request):
    if request.method == "POST":
        food_sel = request.POST['food_sel']
        aliment = Aliment.objects.get(name=food_sel)
        user = request.user
        consumption = Consumption(user=user, aliment = aliment)
        consumption.save()
    
    aliments_selected = Consumption.objects.filter(user=request.user)
    aliments = Aliment.objects.all()
    context = {'aliments': aliments, 'aliments_selected': aliments_selected}
    
    return render(request, 'calories_app/index.html', context)

def delete_aliment(request, id):
    aliment_selected = Consumption.objects.get(id=id)
    if request.method == 'POST':
        aliment_selected.delete()
        return redirect('/')
    return render(request, 'calories_app/delete.html')