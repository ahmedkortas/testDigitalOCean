from django.db import models

# Create your models here.
class Visit(models.Model):
    id = models.IntegerField(
        auto_created=True,
        primary_key=True,
    )
    user_id = models.IntegerField()
    facility_id = models.IntegerField()
    training_program_id = models.IntegerField()
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField()
    comments = models.CharField(max_length=255)

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
        primary_key=True,
    )
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

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
        primary_key=True,

    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

class activities_allactivity (models.Model):
    id = models.IntegerField(
        auto_created=True,
        primary_key=True,
    )
    activity_type_id = models.IntegerField()
    name = models.CharField(max_length=100)
    machine_id = models.IntegerField()
    machine_mode_id = models.IntegerField()
    description = models.CharField(max_length=255)
    activity_definition = models.CharField(max_length=255)
    picture = models.CharField(max_length=100)
    animation = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    name_fi = models.CharField(max_length=100)
    description_en = models.CharField(max_length=255)
    description_fi = models.CharField(max_length=255)
    name_es = models.CharField(max_length=100)
    name_nb = models.CharField(max_length=100)
    name_da = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100)
    name_pt = models.CharField(max_length=100)
    name_ja = models.CharField(max_length=100)
    name_zh_cn = models.CharField(max_length=100)
    name_zh_tw = models.CharField(max_length=100)
    name_sv = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    name_it = models.CharField(max_length=100)
    name_tr = models.CharField(max_length=100)
    name_nl = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_ko = models.CharField(max_length=100)
    name_cs = models.CharField(max_length=100)
    name_sk = models.CharField(max_length=100)
    name_pl = models.CharField(max_length=100)
    name_hu = models.CharField(max_length=100)
    description_es = models.CharField(max_length=255)
    description_nb = models.CharField(max_length=255)
    description_da = models.CharField(max_length=255)
    description_de = models.CharField(max_length=255)
    description_pt = models.CharField(max_length=255)
    description_ja = models.CharField(max_length=255)
    description_zh_cn = models.CharField(max_length=255)
    description_zh_tw = models.CharField(max_length=255)
    description_sv = models.CharField(max_length=255)
    description_fr = models.CharField(max_length=255)
    description_it = models.CharField(max_length=255)
    description_tr = models.CharField(max_length=255)
    description_nl = models.CharField(max_length=255)
    description_ru = models.CharField(max_length=255)
    description_ko = models.CharField(max_length=255)
    description_cs = models.CharField(max_length=255)
    description_sk = models.CharField(max_length=255)
    description_pl = models.CharField(max_length=255)
    description_hu = models.CharField(max_length=255)
    activity_group_id = models.IntegerField()
    description_th = models.CharField(max_length=255)
    name_th = models.CharField(max_length=100)
    video = models.CharField(max_length=2048)


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
        primary_key=True,
    )
    facility_id = models.IntegerField()
    all_activity_id = models.ForeignKey(activities_allactivity, on_delete=models.CASCADE)
    active = models.BooleanField()
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    animation = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)
    comments = models.CharField(max_length=255, null=True)
    use_in_training = models.BooleanField()
    limit_to_equipment_id = models.IntegerField()
    definition = models.JSONField(max_length=255, null=True)
    video = models.CharField(max_length=2048)
