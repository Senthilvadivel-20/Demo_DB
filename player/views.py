from django.shortcuts import redirect, render
from .models import player
from .substring import Substr
#IPL players

from Backend.Runs import runs_info

def home(request):
    if request.method == 'POST':
        name=request.POST['name']
        team=request.POST['team']
        no=request.POST['no']
        image=request.FILES['image']

        obj = player()
        obj.Name = name
        obj.Team = team
        obj.No = no
        obj.Image = image
        obj.save()
        data=player.objects.all()
        return render(request,'home.html',locals())
    data = player.objects.all()
    return render(request,'home.html',locals())


def update(request,id):
    data=player.objects.get(id=id)
    if request.method == "POST":
        name=request.POST['name']
        team=request.POST['team']
        no=request.POST['no']
        try:
            image=request.FILES['image']
        except:
            image = data.Image

        data.Name = name
        data.Team = team
        data.No = no
        data.Image = image
        data.save()
        return redirect('home')

    return render(request,'update.html',locals())


def delete(request,id):
    data = player.objects.get(id=id)
    data.delete()
    return redirect('home')

def table(request):
    if request.method == "POST":
        name = request.POST['search']
        Db = player.objects.all()

        player_list = []
        for n in Db:
            player_list.append(n.Name)

        sorted_list = []
        for crew in player_list:
            str_obj = Substr()
            if str_obj.Search(crew.lower(),name.lower()) != "":
                sorted_list.append(crew)

        data=[]
        for i in sorted_list:
            details = player.objects.get(Name = i)
            data.append(details)
        return render(request,'table.html',locals())

    data = player.objects.all()
    return render (request,'table.html',locals())


def generate_player_info(request,id):
    data = player.objects.get(id=id)
    name = data.Name
    obj = runs_info(name)
    print(obj.total_runs())
    return render(request,'players.html',locals())