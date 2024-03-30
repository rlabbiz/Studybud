from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'first room'},
    {'id': 2, 'name': 'second room'},
]

def home(request):
    return render(request, 'index.html', {'rooms': rooms})

def room(request, pk):

    for single in rooms:
        if single['id'] == int(pk):
            roomName = single['name']

    return render(request, 'room.html', {'rooms': rooms, 'roomName': roomName})
