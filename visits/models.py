from django.db import models

class FacilitiesFacility(models.Model):
    id = models.IntegerField(primary_key=True)
    slug = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.TextField()
    web_site = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=254)
    contact_phone = models.CharField(max_length=64)
    activation_date = models.DateTimeField()
    time_zone = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'facilities_facility'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class TrainingsTrainingcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    defaul_training_picture = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainings_trainingcategory'


class ConceptsConcept(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    stage_amount = models.IntegerField()
    concept_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'concepts_concept'

class TrainingsTrainingprogram(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    facility = models.ForeignKey(FacilitiesFacility, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    fast_mode = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    update_1rm_values = models.BooleanField()
    training_category = models.ForeignKey(TrainingsTrainingcategory, models.DO_NOTHING)
    training_picture = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField()
    current = models.BooleanField()
    parameters = models.TextField(blank=True, null=True)
    concept = models.ForeignKey(ConceptsConcept, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainings_trainingprogram'

class VisitsVisittype(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    show_in_history = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'visits_visittype'

class VisitsVisit(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    visit_type = models.ForeignKey('VisitsVisittype', models.DO_NOTHING)
    facility = models.ForeignKey(FacilitiesFacility, models.DO_NOTHING)
    training_program = models.ForeignKey(TrainingsTrainingprogram, models.DO_NOTHING, blank=True, null=True)
    login = models.DateTimeField()
    logout = models.DateTimeField(blank=True, null=True)
    comments = models.TextField()

    class Meta:
        managed = False
        db_table = 'visits_visit'

class ActivitiesActivitytype(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'activities_activitytype'
        


class ActivitiesActivitygroup(models.Model):
    name = models.CharField(max_length=100)
    member_activity_name = models.CharField(max_length=100)
    description = models.TextField()
    name_en = models.CharField(max_length=100, blank=True, null=True)
    name_fi = models.CharField(max_length=100, blank=True, null=True)
    name_es = models.CharField(max_length=100, blank=True, null=True)
    name_nb = models.CharField(max_length=100, blank=True, null=True)
    name_da = models.CharField(max_length=100, blank=True, null=True)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_pt = models.CharField(max_length=100, blank=True, null=True)
    name_ja = models.CharField(max_length=100, blank=True, null=True)
    name_zh_cn = models.CharField(max_length=100, blank=True, null=True)
    name_zh_tw = models.CharField(max_length=100, blank=True, null=True)
    name_sv = models.CharField(max_length=100, blank=True, null=True)
    name_fr = models.CharField(max_length=100, blank=True, null=True)
    name_it = models.CharField(max_length=100, blank=True, null=True)
    name_tr = models.CharField(max_length=100, blank=True, null=True)
    name_nl = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    name_ko = models.CharField(max_length=100, blank=True, null=True)
    name_cs = models.CharField(max_length=100, blank=True, null=True)
    name_sk = models.CharField(max_length=100, blank=True, null=True)
    name_pl = models.CharField(max_length=100, blank=True, null=True)
    name_hu = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_en = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_fi = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_es = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_nb = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_da = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_de = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_pt = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_ja = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_zh_cn = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_zh_tw = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_sv = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_fr = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_it = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_tr = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_nl = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_ru = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_ko = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_cs = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_sk = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_pl = models.CharField(max_length=100, blank=True, null=True)
    member_activity_name_hu = models.CharField(max_length=100, blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_fi = models.TextField(blank=True, null=True)
    description_es = models.TextField(blank=True, null=True)
    description_nb = models.TextField(blank=True, null=True)
    description_da = models.TextField(blank=True, null=True)
    description_de = models.TextField(blank=True, null=True)
    description_pt = models.TextField(blank=True, null=True)
    description_ja = models.TextField(blank=True, null=True)
    description_zh_cn = models.TextField(blank=True, null=True)
    description_zh_tw = models.TextField(blank=True, null=True)
    description_sv = models.TextField(blank=True, null=True)
    description_fr = models.TextField(blank=True, null=True)
    description_it = models.TextField(blank=True, null=True)
    description_tr = models.TextField(blank=True, null=True)
    description_nl = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    description_ko = models.TextField(blank=True, null=True)
    description_cs = models.TextField(blank=True, null=True)
    description_sk = models.TextField(blank=True, null=True)
    description_pl = models.TextField(blank=True, null=True)
    description_hu = models.TextField(blank=True, null=True)
    description_th = models.TextField(blank=True, null=True)
    member_activity_name_th = models.CharField(max_length=100, blank=True, null=True)
    name_th = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activities_activitygroup'

class MachinesMachine(models.Model):
    manufacturer = models.ForeignKey('MachinesManufacturer', models.DO_NOTHING)
    machine_id = models.IntegerField()
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    body = models.CharField(max_length=1)
    description = models.TextField()
    has_modes = models.BooleanField()
    picture = models.CharField(max_length=100)
    animation = models.CharField(max_length=100)
    parameters = models.TextField(blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    name_fi = models.CharField(max_length=100, blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_fi = models.TextField(blank=True, null=True)
    name_es = models.CharField(max_length=100, blank=True, null=True)
    name_nb = models.CharField(max_length=100, blank=True, null=True)
    name_da = models.CharField(max_length=100, blank=True, null=True)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_pt = models.CharField(max_length=100, blank=True, null=True)
    name_ja = models.CharField(max_length=100, blank=True, null=True)
    name_zh_cn = models.CharField(max_length=100, blank=True, null=True)
    name_zh_tw = models.CharField(max_length=100, blank=True, null=True)
    name_sv = models.CharField(max_length=100, blank=True, null=True)
    name_fr = models.CharField(max_length=100, blank=True, null=True)
    name_it = models.CharField(max_length=100, blank=True, null=True)
    name_tr = models.CharField(max_length=100, blank=True, null=True)
    name_nl = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    name_ko = models.CharField(max_length=100, blank=True, null=True)
    name_cs = models.CharField(max_length=100, blank=True, null=True)
    name_sk = models.CharField(max_length=100, blank=True, null=True)
    name_pl = models.CharField(max_length=100, blank=True, null=True)
    name_hu = models.CharField(max_length=100, blank=True, null=True)
    description_es = models.TextField(blank=True, null=True)
    description_nb = models.TextField(blank=True, null=True)
    description_da = models.TextField(blank=True, null=True)
    description_de = models.TextField(blank=True, null=True)
    description_pt = models.TextField(blank=True, null=True)
    description_ja = models.TextField(blank=True, null=True)
    description_zh_cn = models.TextField(blank=True, null=True)
    description_zh_tw = models.TextField(blank=True, null=True)
    description_sv = models.TextField(blank=True, null=True)
    description_fr = models.TextField(blank=True, null=True)
    description_it = models.TextField(blank=True, null=True)
    description_tr = models.TextField(blank=True, null=True)
    description_nl = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    description_ko = models.TextField(blank=True, null=True)
    description_cs = models.TextField(blank=True, null=True)
    description_sk = models.TextField(blank=True, null=True)
    description_pl = models.TextField(blank=True, null=True)
    description_hu = models.TextField(blank=True, null=True)
    description_th = models.TextField(blank=True, null=True)
    name_th = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machines_machine'
        unique_together = (('manufacturer', 'machine_id'),)

class MachinesMachinemode(models.Model):
    mode_id = models.IntegerField()
    machine = models.ForeignKey(MachinesMachine, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    animation = models.CharField(max_length=100)
    description = models.TextField()
    parameters = models.TextField(blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    name_fi = models.CharField(max_length=100, blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_fi = models.TextField(blank=True, null=True)
    name_es = models.CharField(max_length=100, blank=True, null=True)
    name_nb = models.CharField(max_length=100, blank=True, null=True)
    name_da = models.CharField(max_length=100, blank=True, null=True)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_pt = models.CharField(max_length=100, blank=True, null=True)
    name_ja = models.CharField(max_length=100, blank=True, null=True)
    name_zh_cn = models.CharField(max_length=100, blank=True, null=True)
    name_zh_tw = models.CharField(max_length=100, blank=True, null=True)
    name_sv = models.CharField(max_length=100, blank=True, null=True)
    name_fr = models.CharField(max_length=100, blank=True, null=True)
    name_it = models.CharField(max_length=100, blank=True, null=True)
    name_tr = models.CharField(max_length=100, blank=True, null=True)
    name_nl = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    name_ko = models.CharField(max_length=100, blank=True, null=True)
    name_cs = models.CharField(max_length=100, blank=True, null=True)
    name_sk = models.CharField(max_length=100, blank=True, null=True)
    name_pl = models.CharField(max_length=100, blank=True, null=True)
    name_hu = models.CharField(max_length=100, blank=True, null=True)
    description_es = models.TextField(blank=True, null=True)
    description_nb = models.TextField(blank=True, null=True)
    description_da = models.TextField(blank=True, null=True)
    description_de = models.TextField(blank=True, null=True)
    description_pt = models.TextField(blank=True, null=True)
    description_ja = models.TextField(blank=True, null=True)
    description_zh_cn = models.TextField(blank=True, null=True)
    description_zh_tw = models.TextField(blank=True, null=True)
    description_sv = models.TextField(blank=True, null=True)
    description_fr = models.TextField(blank=True, null=True)
    description_it = models.TextField(blank=True, null=True)
    description_tr = models.TextField(blank=True, null=True)
    description_nl = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    description_ko = models.TextField(blank=True, null=True)
    description_cs = models.TextField(blank=True, null=True)
    description_sk = models.TextField(blank=True, null=True)
    description_pl = models.TextField(blank=True, null=True)
    description_hu = models.TextField(blank=True, null=True)
    description_th = models.TextField(blank=True, null=True)
    name_th = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machines_machinemode'

class FacilitiesEquipment(models.Model):
    facility = models.ForeignKey('FacilitiesFacility', models.DO_NOTHING)
    machine = models.ForeignKey('MachinesMachine', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100)
    install_date = models.DateField(blank=True, null=True)
    last_service = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey('FacilitiesLocation', models.DO_NOTHING, blank=True, null=True)
    position = models.TextField()
    picture = models.CharField(max_length=100, blank=True, null=True)
    animation = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    auth_as = models.OneToOneField(AuthUser, models.DO_NOTHING, blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facilities_equipment'



class ActivitiesAllactivity(models.Model):
    activity_type = models.ForeignKey(ActivitiesActivitytype, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    machine = models.ForeignKey('MachinesMachine', models.DO_NOTHING, blank=True, null=True)
    machine_mode = models.ForeignKey('MachinesMachinemode', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField()
    activity_definition = models.TextField(blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    animation = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    name_fi = models.CharField(max_length=100, blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_fi = models.TextField(blank=True, null=True)
    name_es = models.CharField(max_length=100, blank=True, null=True)
    name_nb = models.CharField(max_length=100, blank=True, null=True)
    name_da = models.CharField(max_length=100, blank=True, null=True)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_pt = models.CharField(max_length=100, blank=True, null=True)
    name_ja = models.CharField(max_length=100, blank=True, null=True)
    name_zh_cn = models.CharField(max_length=100, blank=True, null=True)
    name_zh_tw = models.CharField(max_length=100, blank=True, null=True)
    name_sv = models.CharField(max_length=100, blank=True, null=True)
    name_fr = models.CharField(max_length=100, blank=True, null=True)
    name_it = models.CharField(max_length=100, blank=True, null=True)
    name_tr = models.CharField(max_length=100, blank=True, null=True)
    name_nl = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    name_ko = models.CharField(max_length=100, blank=True, null=True)
    name_cs = models.CharField(max_length=100, blank=True, null=True)
    name_sk = models.CharField(max_length=100, blank=True, null=True)
    name_pl = models.CharField(max_length=100, blank=True, null=True)
    name_hu = models.CharField(max_length=100, blank=True, null=True)
    description_es = models.TextField(blank=True, null=True)
    description_nb = models.TextField(blank=True, null=True)
    description_da = models.TextField(blank=True, null=True)
    description_de = models.TextField(blank=True, null=True)
    description_pt = models.TextField(blank=True, null=True)
    description_ja = models.TextField(blank=True, null=True)
    description_zh_cn = models.TextField(blank=True, null=True)
    description_zh_tw = models.TextField(blank=True, null=True)
    description_sv = models.TextField(blank=True, null=True)
    description_fr = models.TextField(blank=True, null=True)
    description_it = models.TextField(blank=True, null=True)
    description_tr = models.TextField(blank=True, null=True)
    description_nl = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    description_ko = models.TextField(blank=True, null=True)
    description_cs = models.TextField(blank=True, null=True)
    description_sk = models.TextField(blank=True, null=True)
    description_pl = models.TextField(blank=True, null=True)
    description_hu = models.TextField(blank=True, null=True)
    activity_group = models.ForeignKey(ActivitiesActivitygroup, models.DO_NOTHING, blank=True, null=True)
    description_th = models.TextField(blank=True, null=True)
    name_th = models.CharField(max_length=100, blank=True, null=True)
    video = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activities_allactivity'

class MachinesManufacturer(models.Model):
    manufacturer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    name_en = models.CharField(max_length=100, blank=True, null=True)
    name_fi = models.CharField(max_length=100, blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_fi = models.TextField(blank=True, null=True)
    name_es = models.CharField(max_length=100, blank=True, null=True)
    name_nb = models.CharField(max_length=100, blank=True, null=True)
    name_da = models.CharField(max_length=100, blank=True, null=True)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_pt = models.CharField(max_length=100, blank=True, null=True)
    name_ja = models.CharField(max_length=100, blank=True, null=True)
    name_zh_cn = models.CharField(max_length=100, blank=True, null=True)
    name_zh_tw = models.CharField(max_length=100, blank=True, null=True)
    name_sv = models.CharField(max_length=100, blank=True, null=True)
    name_fr = models.CharField(max_length=100, blank=True, null=True)
    name_it = models.CharField(max_length=100, blank=True, null=True)
    name_tr = models.CharField(max_length=100, blank=True, null=True)
    name_nl = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    name_ko = models.CharField(max_length=100, blank=True, null=True)
    name_cs = models.CharField(max_length=100, blank=True, null=True)
    name_sk = models.CharField(max_length=100, blank=True, null=True)
    name_pl = models.CharField(max_length=100, blank=True, null=True)
    name_hu = models.CharField(max_length=100, blank=True, null=True)
    description_es = models.TextField(blank=True, null=True)
    description_nb = models.TextField(blank=True, null=True)
    description_da = models.TextField(blank=True, null=True)
    description_de = models.TextField(blank=True, null=True)
    description_pt = models.TextField(blank=True, null=True)
    description_ja = models.TextField(blank=True, null=True)
    description_zh_cn = models.TextField(blank=True, null=True)
    description_zh_tw = models.TextField(blank=True, null=True)
    description_sv = models.TextField(blank=True, null=True)
    description_fr = models.TextField(blank=True, null=True)
    description_it = models.TextField(blank=True, null=True)
    description_tr = models.TextField(blank=True, null=True)
    description_nl = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    description_ko = models.TextField(blank=True, null=True)
    description_cs = models.TextField(blank=True, null=True)
    description_sk = models.TextField(blank=True, null=True)
    description_pl = models.TextField(blank=True, null=True)
    description_hu = models.TextField(blank=True, null=True)
    description_th = models.TextField(blank=True, null=True)
    name_th = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machines_manufacturer'




class FacilitiesLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=50)
    facility = models.ForeignKey(FacilitiesFacility, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'facilities_location'


class FacilitiesAvailableactivity(models.Model):
    facility = models.ForeignKey('FacilitiesFacility', models.DO_NOTHING)
    all_activity = models.ForeignKey(ActivitiesAllactivity, models.DO_NOTHING)
    active = models.BooleanField()
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100, blank=True, null=True)
    animation = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    use_in_fining = models.BooleanField()
    limit_to_equipment = models.ForeignKey('FacilitiesEquipment', models.DO_NOTHING, blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    video = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facilities_availableactivity'

class FacilitiesAvailablescheduledactivity(models.Model):
        facility = models.ForeignKey('FacilitiesFacility', models.DO_NOTHING)
        location = models.ForeignKey('FacilitiesLocation', models.DO_NOTHING)
        available_activity = models.ForeignKey(FacilitiesAvailableactivity, models.DO_NOTHING)
        name = models.CharField(max_length=100)
        supervisor = models.ForeignKey(AuthUser, models.DO_NOTHING)
        start_date = models.DateField()
        start_time = models.TimeField(blank=True, null=True)
        end_date = models.DateField(blank=True, null=True)
        end_time = models.TimeField(blank=True, null=True)
        lasts_all_day = models.BooleanField()
        visability = models.IntegerField()
        status = models.IntegerField()
        max_persons = models.IntegerField(blank=True, null=True)
        persons_signed = models.IntegerField(blank=True, null=True)
        picture = models.CharField(max_length=100, blank=True, null=True)
        description = models.TextField(blank=True, null=True)
        comments = models.TextField(blank=True, null=True)
        event_color = models.CharField(max_length=32, blank=True, null=True)
        prevent_client_signup = models.BooleanField()
        cancellations_by = models.IntegerField(blank=True, null=True)
        reservation_expires = models.IntegerField(blank=True, null=True)
        reservation_facility_restrict = models.BooleanField()
        reservations_at = models.IntegerField(blank=True, null=True)
        reservations_by = models.IntegerField(blank=True, null=True)

        class Meta:
            managed = False
            db_table = 'facilities_availablescheduledactivity'

class TrainingsTrainingactivity(models.Model):
    activity = models.ForeignKey(FacilitiesAvailableactivity, models.DO_NOTHING)
    training_program = models.ForeignKey('TrainingsTrainingprogram', models.DO_NOTHING)
    order_index = models.IntegerField(blank=True, null=True)
    active = models.BooleanField()
    instruction = models.TextField(blank=True, null=True)
    settings = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainings_trainingactivity'

class VisitsVisitactivity(models.Model):
    visit = models.ForeignKey(VisitsVisit, models.DO_NOTHING)
    activity = models.ForeignKey(FacilitiesAvailableactivity, models.DO_NOTHING)
    scheduled_activity = models.ForeignKey(FacilitiesAvailablescheduledactivity, models.DO_NOTHING, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    supervised_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    instruction = models.TextField(blank=True, null=True)
    supervisor_comments = models.TextField()
    user_comments = models.TextField()
    settings = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    results = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1)
    training_activity = models.ForeignKey(TrainingsTrainingactivity, models.DO_NOTHING, blank=True, null=True)
    raw_data_file = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visits_visitactivity'