from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Player

def index(request):
    last_joined = Player.objects.order_by("-joined")[:7]
    template = loader.get_template('livestats/index.html')
    context = {
        "last_joined" : last_joined,
    }
    return HttpResponse(template.render(context, request))

def detail(request, player_id):
    return HttpResponse("you are looking for a player with an id %s" % player_id)

def results(request, player_id):
    response = "You are looking at the description of the player with an id of %s"
    return HttpResponse(response % player_id)

def vote(request, player_id):
    return HttpResponse("You are voting on a player %s" % player_id)