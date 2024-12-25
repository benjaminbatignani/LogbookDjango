from django.db import models

# Create your models here.
class Aircraft(models.Model):
    id_aircraft = models.SmallAutoField(primary_key=True)
    aircraft = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aircraft'


class Altitude(models.Model):
    id_altitude = models.SmallAutoField(primary_key=True)
    altitude = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'altitude'


class Jump(models.Model):
    id_jump = models.SmallAutoField(primary_key=True)
    jump_number = models.SmallIntegerField(blank=True, null=True)
    jump_date = models.DateField(blank=True, null=True)
    id_jump_type = models.ForeignKey('JumpType', models.DO_NOTHING, db_column='id_jump_type', blank=True, null=True)
    id_altitude = models.ForeignKey(Altitude, models.DO_NOTHING, db_column='id_altitude', blank=True, null=True)
    id_location = models.ForeignKey('Location', models.DO_NOTHING, db_column='id_location', blank=True, null=True)
    id_aircraft = models.ForeignKey(Aircraft, models.DO_NOTHING, db_column='id_aircraft', blank=True, null=True)
    id_parachute = models.ForeignKey('Parachute', models.DO_NOTHING, db_column='id_parachute', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jump'


class JumpType(models.Model):
    id_jump_type = models.SmallAutoField(primary_key=True)
    type = models.CharField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jump_type'


class Location(models.Model):
    id_location = models.SmallAutoField(primary_key=True)
    location_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'location'


class Parachute(models.Model):
    id_parachute = models.SmallAutoField(primary_key=True)
    harness_manufacturer = models.CharField(max_length=50, blank=True, null=True)
    harness_name = models.CharField(max_length=50, blank=True, null=True)
    harness_serial_number = models.CharField(max_length=40, blank=True, null=True)
    harness_dom = models.DateField(blank=True, null=True)
    main_canopy_manufacturer = models.CharField(max_length=50, blank=True, null=True)
    main_canopy_name = models.CharField(max_length=50, blank=True, null=True)
    main_canopy_size = models.SmallIntegerField(blank=True, null=True)
    main_canopy_serial_number = models.CharField(max_length=40, blank=True, null=True)
    main_canopy_dom = models.DateField(blank=True, null=True)
    reserve_canopy_manufacturer = models.CharField(max_length=50, blank=True, null=True)
    reserve_canopy_name = models.CharField(max_length=50, blank=True, null=True)
    reserve_canopy_size = models.SmallIntegerField(blank=True, null=True)
    reserve_canopy_serial_number = models.CharField(max_length=40, blank=True, null=True)
    reserve_canopy_dom = models.DateField(blank=True, null=True)
    aad_manufacturer = models.CharField(max_length=50, blank=True, null=True)
    aad_name = models.CharField(max_length=50, blank=True, null=True)
    aad_serial_number = models.CharField(max_length=40, blank=True, null=True)
    aad_dom = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'parachute'