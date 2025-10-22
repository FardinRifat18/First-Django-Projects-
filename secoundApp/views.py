from django.shortcuts import render

# Create your views here.

def l(request):
    if request.method == "POST":  
        name1 = request.POST.get('name1')  
        name2 = request.POST.get('name2')
        print(name1, name2)
    return render(request, 'ha.html',locals())