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
            location = form.cleaned_data["location"].location_name
            parachute = form.cleaned_data["parachute"].harness_name
            jump_date = datetime.date.today()

            data = SaveJumpData()

            id_location = data.get_location_id(location)
            id_parachute = data.get_parachute_id(parachute)

            data.add_jump(numero_saut, jump_date, id_location, id_parachute)

            numero_prochain_saut += 1

            form = JumpForm(initial={"number" : numero_prochain_saut})

    else:
        form = JumpForm(initial={"number" : numero_prochain_saut})

    return render(request, "savejump/jumpform.html", {"form" : form})

def jumplist(request):
    jumps = Jump.objects.all().order_by('jump_number')
    location = Location.objects.all()

    context = {'jumps': jumps}
    return render(request, 'savejump/jumplist.html', context)