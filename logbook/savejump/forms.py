from django import forms
from .models import Location, Parachute
from django.forms import ModelChoiceField

# Cette classe permet de dire à Django que la propriété à utiliser dans le modèle
# Location sera la propriété location_name. Sinon les valeurs dans la liste de séléction
# ne seront pas adéquates
class LocationModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.location_name

class ParachuteModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.harness_name


class JumpForm(forms.Form):
    number = forms.IntegerField(widget=forms.TextInput, label="Numéro du saut", required=True)
    location = LocationModelChoiceField(label='Lieu',
                                      queryset=Location.objects.all().order_by('location_name'),
                                      empty_label='- Lieu -')

    parachute = ParachuteModelChoiceField(label='Parachute',
                                      queryset=Parachute.objects.all().order_by('harness_name'),
                                      empty_label='- Parachute -')