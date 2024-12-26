from django import forms
from .models import Location, Parachute, Aircraft, Altitude, JumpType
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

class AltitudeModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.altitude

class AircraftModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.aircraft

class JumpTypeModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.type


class JumpForm(forms.Form):
    number = forms.IntegerField(label="Numéro du saut",
                                widget=forms.TextInput(attrs={"class" : "input is-normal",
                                                              "readonly" : ""}))
    # number.widget.attrs.update(attrs={"class" : "input"})

    location = LocationModelChoiceField(label='Lieu',
                                      queryset=Location.objects.all().order_by('location_name'),
                                      empty_label='- Lieu -',
                                      widget=forms.Select(attrs={"class" : "select is-small"})
                                        )

    altitude = AltitudeModelChoiceField(label='Hauteur',
                                      queryset=Altitude.objects.all().order_by('altitude'),
                                      empty_label='- Hauteur -',
                                      widget=forms.Select(attrs={"class" : "select is-small"})
                                        )

    aircraft = AircraftModelChoiceField(label='Avion',
                                      queryset=Aircraft.objects.all().order_by('aircraft'),
                                      empty_label='- Avion -',
                                      widget=forms.Select(attrs={"class" : "select is-small"})
                                        )

    jump_type = JumpTypeModelChoiceField(label='Type de saut',
                                      queryset=JumpType.objects.all().order_by('type'),
                                      empty_label='- Type -',
                                      widget=forms.Select(attrs={"class" : "select is-small"})
                                        )

    parachute = ParachuteModelChoiceField(label='Parachute',
                                      queryset=Parachute.objects.all().order_by('harness_name'),
                                      widget=forms.Select(attrs={"class": "select is-small"}),
                                      empty_label='- Parachute -')

    jump_date = forms.DateField(label="Date",
                                widget=forms.SelectDateWidget)

    comment = forms.CharField(label="Commentaire",
                              required=False
                              )
