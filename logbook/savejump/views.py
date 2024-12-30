from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Jump
from .forms import JumpForm

import logging

logger = logging.getLogger("savejump")

@login_required(login_url='savejump/login')
def index(request):

    logger.info("Entrée dans la vue Index")

    request.session['name'] = 'BENJI'

    return render(request, 'savejump/index.html')

def saisie(request):
    template = loader.get_template("savejump/saisie.html")

    nom = request.session['name']
    print(nom)

    context = {}
    return HttpResponse(template.render(context, request))

def jumpform(request):
    logger.debug("Entrée dans la vue JumpForm")


    is_success = False

    nbr_enregistrement = Jump.objects.count()
    if nbr_enregistrement == 0:
        last_jump_number = 0
    else:
        last_jump_number = Jump.objects.all().values()[0]['jump_number']

    numero_prochain_saut = last_jump_number + 1

    if request.method == "POST":
        form = JumpForm(request.POST, initial={"number" : numero_prochain_saut})

        if form.is_valid():
            numero_saut = form.cleaned_data["number"]
            altitude = form.cleaned_data["altitude"]
            aircraft = form.cleaned_data["aircraft"]
            location = form.cleaned_data["location"]
            jump_type = form.cleaned_data["jump_type"]
            parachute = form.cleaned_data["parachute"]
            jump_date = form.cleaned_data["jump_date"]
            comment = form.cleaned_data["comment"]

            jump = Jump(jump_number=numero_saut, jump_date=jump_date, id_altitude=altitude,
                        id_location=location, id_parachute=parachute, id_aircraft=aircraft,
                        id_jump_type=jump_type, comment=comment)

            jump.save()

            numero_prochain_saut += 1

            form = JumpForm(initial={"number" : numero_prochain_saut})

            is_success = True

    else:
        form = JumpForm(initial={"number" : numero_prochain_saut})

    return render(request, "savejump/jumpform.html", {"form" : form, "is_success" : is_success})

def jumplist(request):
    jumps = reversed(Jump.objects.all().order_by('jump_number'))

    nbr_jump = Jump.objects.count()
    nbr_page = (nbr_jump // 10) + 1

    context = {'jumps': jumps}
    return render(request, 'savejump/jumplist.html', context)