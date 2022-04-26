from django.shortcuts import render

# Create your views here.


def room(requset, name):
    return render(requset, 'index.html', {
        'room_name': name
    })
