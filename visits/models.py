from django.db import models
from django.db.models.fields.reverse_related import ForeignObjectRel

# Create your models here.
class Visit(models.Model):
    id = models.IntegerField(
        auto_created=True,
        null=True,
        auto_increment=True,
    )
    user_id = models.IntegerField(null=True)
    facility_id = models.IntegerField(null=True)
    training_program_id = models.IntegerField(null=True)
    login_time = models.DateTimeField(null=True)
    logout_time = models.DateTimeField(null=True)
    comments = models.CharField(max_length=255, null=True)

#     id integer NOT NULL,
#    user_id integer NOT NULL,
#    visit_type_id integer NOT NULL,
#    facility_id integer NOT NULL,
#    training_program_id integer,
#    login timestamp with time zone NOT NULL,
#    logout timestamp with time zone,
#    comments text NOT NULL
    

class auth_user(models.Model):
    id = models.IntegerField(
        auto_created=True,
        null=True,
        auto_increment=True,
    )
    password = models.CharField(max_length=128, null=True)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField(null=True)
    username = models.CharField(max_length=150, null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=254, null=True)
    is_staff = models.BooleanField(null=True)
    is_active = models.BooleanField(null=True)
    date_joined = models.DateTimeField(null=True)

  #  id integer NOT NULL,
  #  password character varying(128) NOT NULL,
  #  last_login timestamp with time zone,
 #   is_superuser boolean NOT NULL,
 #   username character varying(30) NOT NULL,
  #  first_name character varying(30) NOT NULL,
 #   last_name character varying(30) NOT NULL,
 #   email character varying(254) NOT NULL,
  #  is_staff boolean NOT NULL,
  #  is_active boolean NOT NULL,
  #  date_joined timestamp with time zone NOT NULL

class activities_activitytype (models.Model):
    #id integer NOT NULL,
    #name character varying(100) NOT NULL,
    #description text NOT NULL
    id = models.IntegerField(
        auto_created=True,
        null=True,  
        auto_increment=True,
    )
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)

class activities_allactivity (models.Model):
    id = models.IntegerField(
        auto_created=True,
        null=True,
        auto_increment=True,
        primary_key=True,
    )
    activity_type_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    machine_id = models.IntegerField(null=True)
    machine_mode_id = models.IntegerField(null=True)
    description = models.CharField(max_length=255, null=True)
    activity_definition = models.CharField(max_length=255, null=True)
    picture = models.CharField(max_length=100, null=True)
    animation = models.CharField(max_length=100, null=True)
    name_en = models.CharField(max_length=100, null=True)
    name_fi = models.CharField(max_length=100, null=True)
    description_en = models.CharField(max_length=255, null=True)
    description_fi = models.CharField(max_length=255, null=True)
    name_es = models.CharField(max_length=100, null=True)
    name_nb = models.CharField(max_length=100, null=True)
    name_da = models.CharField(max_length=100, null=True)
    name_de = models.CharField(max_length=100, null=True)
    name_pt = models.CharField(max_length=100, null=True)
    name_ja = models.CharField(max_length=100, null=True)
    name_zh_cn = models.CharField(max_length=100, null=True)
    name_zh_tw = models.CharField(max_length=100, null=True)
    name_sv = models.CharField(max_length=100, null=True)
    name_fr = models.CharField(max_length=100, null=True)
    name_it = models.CharField(max_length=100, null=True)
    name_tr = models.CharField(max_length=100, null=True)
    name_nl = models.CharField(max_length=100, null=True)
    name_ru = models.CharField(max_length=100, null=True)
    name_ko = models.CharField(max_length=100, null=True)
    name_cs = models.CharField(max_length=100, null=True)
    name_sk = models.CharField(max_length=100, null=True)
    name_pl = models.CharField(max_length=100, null=True)
    name_hu = models.CharField(max_length=100, null=True)
    description_es = models.CharField(max_length=255, null=True)
    description_nb = models.CharField(max_length=255, null=True)
    description_da = models.CharField(max_length=255, null=True)
    description_de = models.CharField(max_length=255, null=True)
    description_pt = models.CharField(max_length=255, null=True)
    description_ja = models.CharField(max_length=255, null=True)
    description_zh_cn = models.CharField(max_length=255, null=True)
    description_zh_tw = models.CharField(max_length=255, null=True)
    description_sv = models.CharField(max_length=255, null=True)
    description_fr = models.CharField(max_length=255, null=True)
    description_it = models.CharField(max_length=255, null=True)
    description_tr = models.CharField(max_length=255, null=True)
    description_nl = models.CharField(max_length=255, null=True)
    description_ru = models.CharField(max_length=255, null=True)
    description_ko = models.CharField(max_length=255, null=True)
    description_cs = models.CharField(max_length=255, null=True)
    description_sk = models.CharField(max_length=255, null=True)
    description_pl = models.CharField(max_length=255, null=True)
    description_hu = models.CharField(max_length=255, null=True)
    activity_group_id = models.IntegerField(null=True)
    description_th = models.CharField(max_length=255, null=True)
    name_th = models.CharField(max_length=100, null=True)
    video = models.CharField(max_length=2048, null=True)


class facility_availableday (models.Model):
#    id integer NOT NULL,
#    facility_id integer NOT NULL,
#    all_activity_id integer NOT NULL,
#    active boolean NOT NULL,
#    name character varying(100) NOT NULL,
#    picture character varying(100),
#    animation character varying(100),
 #   description text,
 #   comments text,
#    use_in_training boolean NOT NULL,
 #   limit_to_equipment_id integer,
 #   definition json,
 #   video character varying(2048)

    id = models.IntegerField(
        auto_created=True,
        null=True,
        auto_increment=True,
    )
    facility_id = models.IntegerField(null=True)
    all_activity_id = models.IntegerField(null=True, foreign_key=activities_allactivity)
    active = models.BooleanField(null=True)
    name = models.CharField(max_length=100, null=True)
    picture = models.CharField(max_length=100, )
    animation = models.CharField(max_length=100, )
    description = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    use_in_training = models.BooleanField(null=True)
    limit_to_equipment_id = models.IntegerField()
    definition = models.JSONField(max_length=255)
    video = models.CharField(max_length=2048, null=True)