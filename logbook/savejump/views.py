from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Jump, Location
from .forms import JumpForm
import datetime
from .data.savejump_data import SaveJumpData

def index(request):
    # jumps = Jump.objects.filter(location="Arcachon")
    # context = {'jumps': jumps}
    return render(request, 'savejump/index.html')

def saisie(request):
    template = loader.get_template("savejump/saisie.html")
    context = {}
    return HttpResponse(template.render(context, request))

def jumpform(request):

    numero_prochain_saut = SaveJumpData().get_last_jump_number() + 1

    if request.method == "POST":
        form = JumpForm(request.POST, initial={"number" : numero_prochain_saut})

        if form.is_valid():
            numero_saut = form.cleaned_data["number"]
            altitude = form.cleaned_data["altitude"].altitude
            aircraft = form.cleaned_data["aircraft"].aircraft
            location = form.cleaned_data["location"].location_name
            jump_type = form.cleaned_data["jump_type"].type
            parachute = form.cleaned_data["parachute"].harness_name
            jump_date = form.cleaned_data["jump_date"]
            comment = form.cleaned_data["comment"]

            data = SaveJumpData()

            id_altitude = data.get_altitude_id(altitude)
            id_aircraft = data.get_aircraft_id(aircraft)
            id_location = data.get_location_id(location)
            id_jump_type = data.get_jump_type_id(jump_type)
            id_parachute = data.get_parachute_id(parachute)

            data.add_jump(numero_saut, id_altitude, id_aircraft, id_location, id_jump_type, id_parachute, jump_date, comment)

            numero_prochain_saut += 1

            form = JumpForm(initial={"number" : numero_prochain_saut})

    else:
        form = JumpForm(initial={"number" : numero_prochain_saut})

    return render(request, "savejump/jumpform.html", {"form" : form})

def jumplist(request):
    jumps = reversed(Jump.objects.all().order_by('jump_number'))
    context = {'jumps': jumps}
    return render(request, 'savejump/jumplist.html', context)