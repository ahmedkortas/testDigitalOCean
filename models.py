# # # This is an auto-generated Django model module.
# # # You'll have to do the following manually to clean this up:
# # #   * Rearrange models' order
# # #   * Make sure each model has one field with primary_key=True
# # #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# # #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# # class AccountsCard(models.Model):
# #     user = models.ForeignKey('AuthUser', models.DO_NOTHING)
# #     rfid_number = models.CharField(unique=True, max_length=64)
# #     card_type = models.IntegerField()
# #     expiry_date = models.DateField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'accounts_card'


# # class AccountsMembership(models.Model):
# #     user = models.OneToOneField('AuthUser', models.DO_NOTHING)
# #     facility = models.ForeignKey('FacilitiesFacility', models.DO_NOTHING)
# #     membership_type = models.ForeignKey('AccountsMembershiptype', models.DO_NOTHING)
# #     start_date = models.DateField()
# #     end_date = models.DateField(blank=True, null=True)
# #     start_time = models.TimeField(blank=True, null=True)
# #     end_time = models.TimeField(blank=True, null=True)
# #     visit_count = models.IntegerField(blank=True, null=True)
# #     visits_left = models.IntegerField(blank=True, null=True)
# #     price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
# #     on_hold = models.BooleanField()
# #     payment_period = models.IntegerField(blank=True, null=True)
# #     last_payment_date = models.DateField(blank=True, null=True)
# #     personal_trainer = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'accounts_membership'


# # class AccountsMembershiptype(models.Model):
# #     name = models.CharField(max_length=100)
# #     default_duration = models.IntegerField(blank=True, null=True)
# #     default_end_date = models.DateField(blank=True, null=True)
# #     default_start_time = models.TimeField(blank=True, null=True)
# #     default_end_time = models.TimeField(blank=True, null=True)
# #     default_visit_count = models.IntegerField(blank=True, null=True)
# #     default_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
# #     default_payment_period = models.IntegerField(blank=True, null=True)
# #     use_duration_or_end_date = models.BooleanField()
# #     description = models.TextField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'accounts_membershiptype'


# # class AccountsProfile(models.Model):
# #     mugshot = models.CharField(max_length=100)
# #     privacy = models.CharField(max_length=15)
# #     user = models.OneToOneField('AuthUser', models.DO_NOTHING)
# #     language = models.CharField(max_length=5)
# #     gender = models.CharField(max_length=1)
# #     date_of_birth = models.DateField(blank=True, null=True)
# #     welcome_name = models.CharField(max_length=100)
# #     custom_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
# #     comments = models.TextField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'accounts_profile'


# # class ActivitiesActivitygroup(models.Model):
# #     name = models.CharField(max_length=100)
# #     member_activity_name = models.CharField(max_length=100)
# #     description = models.TextField()
# #     name_en = models.CharField(max_length=100, blank=True, null=True)
# #     name_fi = models.CharField(max_length=100, blank=True, null=True)
# #     name_es = models.CharField(max_length=100, blank=True, null=True)
# #     name_nb = models.CharField(max_length=100, blank=True, null=True)
# #     name_da = models.CharField(max_length=100, blank=True, null=True)
# #     name_de = models.CharField(max_length=100, blank=True, null=True)
# #     name_pt = models.CharField(max_length=100, blank=True, null=True)
# #     name_ja = models.CharField(max_length=100, blank=True, null=True)
# #     name_zh_cn = models.CharField(max_length=100, blank=True, null=True)
# #     name_zh_tw = models.CharField(max_length=100, blank=True, null=True)
# #     name_sv = models.CharField(max_length=100, blank=True, null=True)
# #     name_fr = models.CharField(max_length=100, blank=True, null=True)
# #     name_it = models.CharField(max_length=100, blank=True, null=True)
# #     name_tr = models.CharField(max_length=100, blank=True, null=True)
# #     name_nl = models.CharField(max_length=100, blank=True, null=True)
# #     name_ru = models.CharField(max_length=100, blank=True, null=True)
# #     name_ko = models.CharField(max_length=100, blank=True, null=True)
# #     name_cs = models.CharField(max_length=100, blank=True, null=True)
# #     name_sk = models.CharField(max_length=100, blank=True, null=True)
# #     name_pl = models.CharField(max_length=100, blank=True, null=True)
# #     name_hu = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_en = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_fi = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_es = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_nb = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_da = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_de = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_pt = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_ja = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_zh_cn = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_zh_tw = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_sv = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_fr = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_it = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_tr = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_nl = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_ru = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_ko = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_cs = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_sk = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_pl = models.CharField(max_length=100, blank=True, null=True)
# #     member_activity_name_hu = models.CharField(max_length=100, blank=True, null=True)
# #     description_en = models.TextField(blank=True, null=True)
# #     description_fi = models.TextField(blank=True, null=True)
# #     description_es = models.TextField(blank=True, null=True)
# #     description_nb = models.TextField(blank=True, null=True)
# #     description_da = models.TextField(blank=True, null=True)
# #     description_de = models.TextField(blank=True, null=True)
# #     description_pt = models.TextField(blank=True, null=True)
# #     description_ja = models.TextField(blank=True, null=True)
# #     description_zh_cn = models.TextField(blank=True, null=True)
# #     description_zh_tw = models.TextField(blank=True, null=True)
# #     description_sv = models.TextField(blank=True, null=True)
# #     description_fr = models.TextField(blank=True, null=True)
# #     description_it = models.TextField(blank=True, null=True)
# #     description_tr = models.TextField(blank=True, null=True)
# #     description_nl = models.TextField(blank=True, null=True)
# #     description_ru = models.TextField(blank=True, null=True)
# #     description_ko = models.TextField(blank=True, null=True)
# #     description_cs = models.TextField(blank=True, null=True)
# #     description_sk = models.TextField(blank=True, null=True)
# #     description_pl = models.TextField(blank=True, null=True)
# #     description_hu = models.TextField(blank=True, null=True)
# #     description_th = models.TextField(blank=True, null=True)
# #     member_activity_name_th = models.CharField(max_length=100, blank=True, null=True)
# #     name_th = models.CharField(max_length=100, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'activities_activitygroup'


# # class ActivitiesActivityimage(models.Model):
# #     file = models.CharField(max_length=100)
# #     description = models.TextField()
# #     order_index = models.IntegerField(blank=True, null=True)
# #     activity = models.ForeignKey('ActivitiesAllactivity', models.DO_NOTHING)
# #     description_cs = models.TextField(blank=True, null=True)
# #     description_da = models.TextField(blank=True, null=True)
# #     description_de = models.TextField(blank=True, null=True)
# #     description_en = models.TextField(blank=True, null=True)
# #     description_es = models.TextField(blank=True, null=True)
# #     description_fi = models.TextField(blank=True, null=True)
# #     description_fr = models.TextField(blank=True, null=True)
# #     description_hu = models.TextField(blank=True, null=True)
# #     description_it = models.TextField(blank=True, null=True)
# #     description_ja = models.TextField(blank=True, null=True)
# #     description_ko = models.TextField(blank=True, null=True)
# #     description_nb = models.TextField(blank=True, null=True)
# #     description_nl = models.TextField(blank=True, null=True)
# #     description_pl = models.TextField(blank=True, null=True)
# #     description_pt = models.TextField(blank=True, null=True)
# #     description_ru = models.TextField(blank=True, null=True)
# #     description_sk = models.TextField(blank=True, null=True)
# #     description_sv = models.TextField(blank=True, null=True)
# #     description_tr = models.TextField(blank=True, null=True)
# #     description_zh_cn = models.TextField(blank=True, null=True)
# #     description_zh_tw = models.TextField(blank=True, null=True)
# #     description_th = models.TextField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'activities_activityimage'


# # class ActivitiesActivitytag(models.Model):
# #     name = models.CharField(max_length=100)
# #     description = models.TextField(blank=True, null=True)
# #     description_cs = models.TextField(blank=True, null=True)
# #     description_da = models.TextField(blank=True, null=True)
# #     description_de = models.TextField(blank=True, null=True)
# #     description_en = models.TextField(blank=True, null=True)
# #     description_es = models.TextField(blank=True, null=True)
# #     description_fi = models.TextField(blank=True, null=True)
# #     description_fr = models.TextField(blank=True, null=True)
# #     description_hu = models.TextField(blank=True, null=True)
# #     description_it = models.TextField(blank=True, null=True)
# #     description_ja = models.TextField(blank=True, null=True)
# #     description_ko = models.TextField(blank=True, null=True)
# #     description_nb = models.TextField(blank=True, null=True)
# #     description_nl = models.TextField(blank=True, null=True)
# #     description_pl = models.TextField(blank=True, null=True)
# #     description_pt = models.TextField(blank=True, null=True)
# #     description_ru = models.TextField(blank=True, null=True)
# #     description_sk = models.TextField(blank=True, null=True)
# #     description_sv = models.TextField(blank=True, null=True)
# #     description_tr = models.TextField(blank=True, null=True)
# #     description_zh_cn = models.TextField(blank=True, null=True)
# #     description_zh_tw = models.TextField(blank=True, null=True)
# #     name_cs = models.CharField(max_length=100, blank=True, null=True)
# #     name_da = models.CharField(max_length=100, blank=True, null=True)
# #     name_de = models.CharField(max_length=100, blank=True, null=True)
# #     name_en = models.CharField(max_length=100, blank=True, null=True)
# #     name_es = models.CharField(max_length=100, blank=True, null=True)
# #     name_fi = models.CharField(max_length=100, blank=True, null=True)
# #     name_fr = models.CharField(max_length=100, blank=True, null=True)
# #     name_hu = models.CharField(max_length=100, blank=True, null=True)
# #     name_it = models.CharField(max_length=100, blank=True, null=True)
# #     name_ja = models.CharField(max_length=100, blank=True, null=True)
# #     name_ko = models.CharField(max_length=100, blank=True, null=True)
# #     name_nb = models.CharField(max_length=100, blank=True, null=True)
# #     name_nl = models.CharField(max_length=100, blank=True, null=True)
# #     name_pl = models.CharField(max_length=100, blank=True, null=True)
# #     name_pt = models.CharField(max_length=100, blank=True, null=True)
# #     name_ru = models.CharField(max_length=100, blank=True, null=True)
# #     name_sk = models.CharField(max_length=100, blank=True, null=True)
# #     name_sv = models.CharField(max_length=100, blank=True, null=True)
# #     name_tr = models.CharField(max_length=100, blank=True, null=True)
# #     name_zh_cn = models.CharField(max_length=100, blank=True, null=True)
# #     name_zh_tw = models.CharField(max_length=100, blank=True, null=True)
# #     concept_template = models.ForeignKey('ConceptsConcepttemplate', models.DO_NOTHING, blank=True, null=True)
# #     description_th = models.TextField(blank=True, null=True)
# #     name_th = models.CharField(max_length=100, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'activities_activitytag'


# # class ActivitiesActivitytype(models.Model):
# #     name = models.CharField(max_length=100)
# #     description = models.TextField()

# #     class Meta:
# #         managed = False
# #         db_table = 'activities_activitytype'


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


# # class ActivitiesAllactivityActivityTags(models.Model):
# #     allactivity = models.ForeignKey(ActivitiesAllactivity, models.DO_NOTHING)
# #     activitytag = models.ForeignKey(ActivitiesActivitytag, models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'activities_allactivity_activity_tags'
# #         unique_together = (('allactivity', 'activitytag'),)


# # class AuthGroup(models.Model):
# #     name = models.CharField(unique=True, max_length=80)

# #     class Meta:
# #         managed = False
# #         db_table = 'auth_group'


# # class AuthGroupPermissions(models.Model):
# #     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
# #     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'auth_group_permissions'
# #         unique_together = (('group', 'permission'),)


# # class AuthPermission(models.Model):
# #     name = models.CharField(max_length=255)
# #     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
# #     codename = models.CharField(max_length=100)

# #     class Meta:
# #         managed = False
# #         db_table = 'auth_permission'
# #         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     id = models.IntegerField(primary_key=True)
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# # class AuthUserGroups(models.Model):
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'auth_user_groups'
# #         unique_together = (('user', 'group'),)


# # class AuthUserUserPermissions(models.Model):
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'auth_user_user_permissions'
# #         unique_together = (('user', 'permission'),)


# class ConceptsConcept(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     stage_amount = models.IntegerField()
#     concept_status = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'concepts_concept'


# # class ConceptsConceptstage(models.Model):
# #     name = models.CharField(max_length=100)
# #     description = models.TextField(blank=True, null=True)
# #     duration_in_days = models.IntegerField()
# #     stage_index = models.IntegerField()
# #     parameters = models.TextField(blank=True, null=True)
# #     concept = models.ForeignKey(ConceptsConcept, models.DO_NOTHING)
# #     current = models.BooleanField()
# #     start_date = models.DateField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'concepts_conceptstage'


# # class ConceptsConcepttemplate(models.Model):
# #     name = models.CharField(max_length=100)
# #     description = models.TextField()
# #     stage_amount = models.IntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'concepts_concepttemplate'


# # class ConceptsConcepttemplatestage(models.Model):
# #     name = models.CharField(max_length=100)
# #     description = models.TextField(blank=True, null=True)
# #     duration_in_days = models.IntegerField()
# #     stage_index = models.IntegerField()
# #     parameters = models.TextField(blank=True, null=True)
# #     concept_template = models.ForeignKey(ConceptsConcepttemplate, models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'concepts_concepttemplatestage'


# # class DjangoAdminLog(models.Model):
# #     action_time = models.DateTimeField()
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
# #     object_id = models.TextField(blank=True, null=True)
# #     object_repr = models.CharField(max_length=200)
# #     action_flag = models.SmallIntegerField()
# #     change_message = models.TextField()

# #     class Meta:
# #         managed = False
# #         db_table = 'django_admin_log'


# # class DjangoContentType(models.Model):
# #     app_label = models.CharField(max_length=100)
# #     model = models.CharField(max_length=100)

# #     class Meta:
# #         managed = False
# #         db_table = 'django_content_type'
# #         unique_together = (('app_label', 'model'),)


# # class DjangoMigrations(models.Model):
# #     app = models.CharField(max_length=255)
# #     name = models.CharField(max_length=255)
# #     applied = models.DateTimeField()

# #     class Meta:
# #         managed = False
# #         db_table = 'django_migrations'


# # class DjangoSession(models.Model):
# #     session_key = models.CharField(primary_key=True, max_length=40)
# #     session_data = models.TextField()
# #     expire_date = models.DateTimeField()

# #     class Meta:
# #         managed = False
# #         db_table = 'django_session'


# # class DjangoSite(models.Model):
# #     domain = models.CharField(max_length=100)
# #     name = models.CharField(max_length=50)

# #     class Meta:
# #         managed = False
# #         db_table = 'django_site'


# # class EasyThumbnailsSource(models.Model):
# #     name = models.CharField(max_length=255)
# #     modified = models.DateTimeField()
# #     storage_hash = models.CharField(max_length=40)

# #     class Meta:
# #         managed = False
# #         db_table = 'easy_thumbnails_source'
# #         unique_together = (('name', 'storage_hash'),)


# # class EasyThumbnailsThumbnail(models.Model):
# #     name = models.CharField(max_length=255)
# #     modified = models.DateTimeField()
# #     source = models.ForeignKey(EasyThumbnailsSource, models.DO_NOTHING)
# #     storage_hash = models.CharField(max_length=40)

# #     class Meta:
# #         managed = False
# #         db_table = 'easy_thumbnails_thumbnail'
# #         unique_together = (('source', 'name', 'storage_hash'),)


# # class EasyThumbnailsThumbnaildimensions(models.Model):
# #     thumbnail = models.OneToOneField(EasyThumbnailsThumbnail, models.DO_NOTHING)
# #     width = models.IntegerField(blank=True, null=True)
# #     height = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'easy_thumbnails_thumbnaildimensions'


# # class EquipmentEvent(models.Model):
# #     created = models.DateTimeField()
# #     equipment = models.ForeignKey('FacilitiesEquipment', models.DO_NOTHING)
# #     event_type = models.IntegerField()
# #     event_level = models.IntegerField()
# #     causer = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
# #     description = models.TextField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'equipment_event'


# # class EquipmentHurmachinemetrics(models.Model):
# #     created = models.DateTimeField()
# #     equipment = models.ForeignKey('FacilitiesEquipment', models.DO_NOTHING)
# #     on_time = models.IntegerField()
# #     idle_time = models.IntegerField()
# #     lifetime_logins = models.IntegerField()
# #     network_failure = models.IntegerField()
# #     lifetime_reps = models.IntegerField()
# #     average_load = models.IntegerField()
# #     max_load = models.IntegerField()
# #     fcm2_version = models.CharField(max_length=100, blank=True, null=True)
# #     fcm2_setup_version = models.CharField(max_length=100, blank=True, null=True)
# #     fcm2_ina_version = models.CharField(max_length=100, blank=True, null=True)
# #     image_version = models.CharField(max_length=100, blank=True, null=True)
# #     em3_hardware_version = models.CharField(max_length=100, blank=True, null=True)
# #     em3_firmware_version = models.CharField(max_length=100, blank=True, null=True)
# #     dc_hardware_version = models.CharField(max_length=100, blank=True, null=True)
# #     dc_firmware_version = models.CharField(max_length=100, blank=True, null=True)
# #     secondary_dc_hardware_version = models.CharField(max_length=100, blank=True, null=True)
# #     secondary_dc_firmware_version = models.CharField(max_length=100, blank=True, null=True)
# #     local_ip = models.GenericIPAddressField(blank=True, null=True)
# #     app_version = models.CharField(max_length=100, blank=True, null=True)
# #     mvu_hw_version = models.CharField(max_length=100, blank=True, null=True)
# #     mvu_sw_version = models.CharField(max_length=100, blank=True, null=True)
# #     sensors = models.TextField(blank=True, null=True)
# #     tablet_serial = models.CharField(max_length=100, blank=True, null=True)
# #     mvu_serial = models.CharField(max_length=100, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'equipment_hurmachinemetrics'


# # class FacilitiesAvailableactivity(models.Model):
# #     facility = models.ForeignKey('FacilitiesFacility', models.DO_NOTHING)
# #     all_activity = models.ForeignKey(ActivitiesAllactivity, models.DO_NOTHING)
# #     active = models.BooleanField()
# #     name = models.CharField(max_length=100)
# #     picture = models.CharField(max_length=100, blank=True, null=True)
# #     animation = models.CharField(max_length=100, blank=True, null=True)
# #     description = models.TextField(blank=True, null=True)
# #     comments = models.TextField(blank=True, null=True)
# #     use_in_training = models.BooleanField()
# #     limit_to_equipment = models.ForeignKey('FacilitiesEquipment', models.DO_NOTHING, blank=True, null=True)
# #     definition = models.TextField(blank=True, null=True)
# #     video = models.CharField(max_length=2048, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'facilities_availableactivity'


# # class FacilitiesAvailablescheduledactivity(models.Model):
# #     facility = models.ForeignKey('FacilitiesFacility', models.DO_NOTHING)
# #     location = models.ForeignKey('FacilitiesLocation', models.DO_NOTHING)
# #     available_activity = models.ForeignKey(FacilitiesAvailableactivity, models.DO_NOTHING)
# #     name = models.CharField(max_length=100)
# #     supervisor = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     start_date = models.DateField()
# #     start_time = models.TimeField(blank=True, null=True)
# #     end_date = models.DateField(blank=True, null=True)
# #     end_time = models.TimeField(blank=True, null=True)
# #     lasts_all_day = models.BooleanField()
# #     visability = models.IntegerField()
# #     status = models.IntegerField()
# #     max_persons = models.IntegerField(blank=True, null=True)
# #     persons_signed = models.IntegerField(blank=True, null=True)
# #     picture = models.CharField(max_length=100, blank=True, null=True)
# #     description = models.TextField(blank=True, null=True)
# #     comments = models.TextField(blank=True, null=True)
# #     event_color = models.CharField(max_length=32, blank=True, null=True)
# #     prevent_client_signup = models.BooleanField()
# #     cancellations_by = models.IntegerField(blank=True, null=True)
# #     reservation_expires = models.IntegerField(blank=True, null=True)
# #     reservation_facility_restrict = models.BooleanField()
# #     reservations_at = models.IntegerField(blank=True, null=True)
# #     reservations_by = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'facilities_availablescheduledactivity'


# # class FacilitiesEquipment(models.Model):
# #     facility = models.ForeignKey('FacilitiesFacility', models.DO_NOTHING)
# #     machine = models.ForeignKey('MachinesMachine', models.DO_NOTHING, blank=True, null=True)
# #     name = models.CharField(max_length=100)
# #     install_date = models.DateField(blank=True, null=True)
# #     last_service = models.DateTimeField(blank=True, null=True)
# #     location = models.ForeignKey('FacilitiesLocation', models.DO_NOTHING, blank=True, null=True)
# #     position = models.TextField()
# #     picture = models.CharField(max_length=100, blank=True, null=True)
# #     animation = models.CharField(max_length=100, blank=True, null=True)
# #     description = models.TextField(blank=True, null=True)
# #     comments = models.TextField(blank=True, null=True)
# #     auth_as = models.OneToOneField(AuthUser, models.DO_NOTHING, blank=True, null=True)
# #     parameters = models.TextField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'facilities_equipment'


# class FacilitiesFacility(models.Model):
#     id = models.IntegerField(primary_key=True)
#     slug = models.CharField(max_length=50)
#     name = models.CharField(max_length=100)
#     address = models.TextField()
#     web_site = models.CharField(max_length=200)
#     contact_name = models.CharField(max_length=100)
#     contact_email = models.CharField(max_length=254)
#     contact_phone = models.CharField(max_length=64)
#     activation_date = models.DateTimeField()
#     time_zone = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'facilities_facility'


# # class FacilitiesLocation(models.Model):
# #     name = models.CharField(max_length=100)
# #     description = models.TextField(blank=True, null=True)
# #     slug = models.CharField(max_length=50)
# #     facility = models.ForeignKey(FacilitiesFacility, models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'facilities_location'


# # class FacilitiesOpeninghours(models.Model):
# #     facility = models.ForeignKey(FacilitiesFacility, models.DO_NOTHING)
# #     name = models.CharField(max_length=100)
# #     show_index = models.IntegerField()
# #     description = models.TextField()

# #     class Meta:
# #         managed = False
# #         db_table = 'facilities_openinghours'


# # class GuardianGroupobjectpermission(models.Model):
# #     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
# #     content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
# #     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
# #     object_pk = models.CharField(max_length=255)

# #     class Meta:
# #         managed = False
# #         db_table = 'guardian_groupobjectpermission'
# #         unique_together = (('object_pk', 'group', 'content_type', 'permission'),)


# # class GuardianUserobjectpermission(models.Model):
# #     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
# #     content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     object_pk = models.CharField(max_length=255)

# #     class Meta:
# #         managed = False
# #         db_table = 'guardian_userobjectpermission'
# #         unique_together = (('object_pk', 'user', 'content_type', 'permission'),)


# # class MachinesMachine(models.Model):
# #     manufacturer = models.ForeignKey('MachinesManufacturer', models.DO_NOTHING)
# #     machine_id = models.IntegerField()
# #     name = models.CharField(max_length=100)
# #     product = models.CharField(max_length=100)
# #     body = models.CharField(max_length=1)
# #     description = models.TextField()
# #     has_modes = models.BooleanField()
# #     picture = models.CharField(max_length=100)
# #     animation = models.CharField(max_length=100)
# #     parameters = models.TextField(blank=True, null=True)
# #     name_en = models.CharField(max_length=100, blank=True, null=True)
# #     name_fi = models.CharField(max_length=100, blank=True, null=True)
# #     description_en = models.TextField(blank=True, null=True)
# #     description_fi = models.TextField(blank=True, null=True)
# #     name_es = models.CharField(max_length=100, blank=True, null=True)
# #     name_nb = models.CharField(max_length=100, blank=True, null=True)
# #     name_da = models.CharField(max_length=100, blank=True, null=True)
# #     name_de = models.CharField(max_length=100, blank=True, null=True)
# #     name_pt = models.CharField(max_length=100, blank=True, null=True)
# #     name_ja = models.CharField(max_length=100, blank=True, null=True)
# #     name_zh_cn = models.CharField(max_length=100, blank=True, null=True)
# #     name_zh_tw = models.CharField(max_length=100, blank=True, null=True)
# #     name_sv = models.CharField(max_length=100, blank=True, null=True)
# #     name_fr = models.CharField(max_length=100, blank=True, null=True)
# #     name_it = models.CharField(max_length=100, blank=True, null=True)
# #     name_tr = models.CharField(max_length=100, blank=True, null=True)
# #     name_nl = models.CharField(max_length=100, blank=True, null=True)
# #     name_ru = models.CharField(max_length=100, blank=True, null=True)
# #     name_ko = models.CharField(max_length=100, blank=True, null=True)
# #     name_cs = models.CharField(max_length=100, blank=True, null=True)
# #     name_sk = models.CharField(max_length=100, blank=True, null=True)
# #     name_pl = models.CharField(max_length=100, blank=True, null=True)
# #     name_hu = models.CharField(max_length=100, blank=True, null=True)
# #     description_es = models.TextField(blank=True, null=True)
# #     description_nb = models.TextField(blank=True, null=True)
# #     description_da = models.TextField(blank=True, null=True)
# #     description_de = models.TextField(blank=True, null=True)
# #     description_pt = models.TextField(blank=True, null=True)
# #     description_ja = models.TextField(blank=True, null=True)
# #     description_zh_cn = models.TextField(blank=True, null=True)
# #     description_zh_tw = models.TextField(blank=True, null=True)
# #     description_sv = models.TextField(blank=True, null=True)
# #     description_fr = models.TextField(blank=True, null=True)
# #     description_it = models.TextField(blank=True, null=True)
# #     description_tr = models.TextField(blank=True, null=True)
# #     description_nl = models.TextField(blank=True, null=True)
# #     description_ru = models.TextField(blank=True, null=True)
# #     description_ko = models.TextField(blank=True, null=True)
# #     description_cs = models.TextField(blank=True, null=True)
# #     description_sk = models.TextField(blank=True, null=True)
# #     description_pl = models.TextField(blank=True, null=True)
# #     description_hu = models.TextField(blank=True, null=True)
# #     description_th = models.TextField(blank=True, null=True)
# #     name_th = models.CharField(max_length=100, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'machines_machine'
# #         unique_together = (('manufacturer', 'machine_id'),)


# # class MachinesMachinemode(models.Model):
# #     mode_id = models.IntegerField()
# #     machine = models.ForeignKey(MachinesMachine, models.DO_NOTHING)
# #     name = models.CharField(max_length=100)
# #     picture = models.CharField(max_length=100)
# #     animation = models.CharField(max_length=100)
# #     description = models.TextField()
# #     parameters = models.TextField(blank=True, null=True)
# #     name_en = models.CharField(max_length=100, blank=True, null=True)
# #     name_fi = models.CharField(max_length=100, blank=True, null=True)
# #     description_en = models.TextField(blank=True, null=True)
# #     description_fi = models.TextField(blank=True, null=True)
# #     name_es = models.CharField(max_length=100, blank=True, null=True)
# #     name_nb = models.CharField(max_length=100, blank=True, null=True)
# #     name_da = models.CharField(max_length=100, blank=True, null=True)
# #     name_de = models.CharField(max_length=100, blank=True, null=True)
# #     name_pt = models.CharField(max_length=100, blank=True, null=True)
# #     name_ja = models.CharField(max_length=100, blank=True, null=True)
# #     name_zh_cn = models.CharField(max_length=100, blank=True, null=True)
# #     name_zh_tw = models.CharField(max_length=100, blank=True, null=True)
# #     name_sv = models.CharField(max_length=100, blank=True, null=True)
# #     name_fr = models.CharField(max_length=100, blank=True, null=True)
# #     name_it = models.CharField(max_length=100, blank=True, null=True)
# #     name_tr = models.CharField(max_length=100, blank=True, null=True)
# #     name_nl = models.CharField(max_length=100, blank=True, null=True)
# #     name_ru = models.CharField(max_length=100, blank=True, null=True)
# #     name_ko = models.CharField(max_length=100, blank=True, null=True)
# #     name_cs = models.CharField(max_length=100, blank=True, null=True)
# #     name_sk = models.CharField(max_length=100, blank=True, null=True)
# #     name_pl = models.CharField(max_length=100, blank=True, null=True)
# #     name_hu = models.CharField(max_length=100, blank=True, null=True)
# #     description_es = models.TextField(blank=True, null=True)
# #     description_nb = models.TextField(blank=True, null=True)
# #     description_da = models.TextField(blank=True, null=True)
# #     description_de = models.TextField(blank=True, null=True)
# #     description_pt = models.TextField(blank=True, null=True)
# #     description_ja = models.TextField(blank=True, null=True)
# #     description_zh_cn = models.TextField(blank=True, null=True)
# #     description_zh_tw = models.TextField(blank=True, null=True)
# #     description_sv = models.TextField(blank=True, null=True)
# #     description_fr = models.TextField(blank=True, null=True)
# #     description_it = models.TextField(blank=True, null=True)
# #     description_tr = models.TextField(blank=True, null=True)
# #     description_nl = models.TextField(blank=True, null=True)
# #     description_ru = models.TextField(blank=True, null=True)
# #     description_ko = models.TextField(blank=True, null=True)
# #     description_cs = models.TextField(blank=True, null=True)
# #     description_sk = models.TextField(blank=True, null=True)
# #     description_pl = models.TextField(blank=True, null=True)
# #     description_hu = models.TextField(blank=True, null=True)
# #     description_th = models.TextField(blank=True, null=True)
# #     name_th = models.CharField(max_length=100, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'machines_machinemode'


# # class MachinesManufacturer(models.Model):
# #     manufacturer_id = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=100)
# #     description = models.TextField()
# #     name_en = models.CharField(max_length=100, blank=True, null=True)
# #     name_fi = models.CharField(max_length=100, blank=True, null=True)
# #     description_en = models.TextField(blank=True, null=True)
# #     description_fi = models.TextField(blank=True, null=True)
# #     name_es = models.CharField(max_length=100, blank=True, null=True)
# #     name_nb = models.CharField(max_length=100, blank=True, null=True)
# #     name_da = models.CharField(max_length=100, blank=True, null=True)
# #     name_de = models.CharField(max_length=100, blank=True, null=True)
# #     name_pt = models.CharField(max_length=100, blank=True, null=True)
# #     name_ja = models.CharField(max_length=100, blank=True, null=True)
# #     name_zh_cn = models.CharField(max_length=100, blank=True, null=True)
# #     name_zh_tw = models.CharField(max_length=100, blank=True, null=True)
# #     name_sv = models.CharField(max_length=100, blank=True, null=True)
# #     name_fr = models.CharField(max_length=100, blank=True, null=True)
# #     name_it = models.CharField(max_length=100, blank=True, null=True)
# #     name_tr = models.CharField(max_length=100, blank=True, null=True)
# #     name_nl = models.CharField(max_length=100, blank=True, null=True)
# #     name_ru = models.CharField(max_length=100, blank=True, null=True)
# #     name_ko = models.CharField(max_length=100, blank=True, null=True)
# #     name_cs = models.CharField(max_length=100, blank=True, null=True)
# #     name_sk = models.CharField(max_length=100, blank=True, null=True)
# #     name_pl = models.CharField(max_length=100, blank=True, null=True)
# #     name_hu = models.CharField(max_length=100, blank=True, null=True)
# #     description_es = models.TextField(blank=True, null=True)
# #     description_nb = models.TextField(blank=True, null=True)
# #     description_da = models.TextField(blank=True, null=True)
# #     description_de = models.TextField(blank=True, null=True)
# #     description_pt = models.TextField(blank=True, null=True)
# #     description_ja = models.TextField(blank=True, null=True)
# #     description_zh_cn = models.TextField(blank=True, null=True)
# #     description_zh_tw = models.TextField(blank=True, null=True)
# #     description_sv = models.TextField(blank=True, null=True)
# #     description_fr = models.TextField(blank=True, null=True)
# #     description_it = models.TextField(blank=True, null=True)
# #     description_tr = models.TextField(blank=True, null=True)
# #     description_nl = models.TextField(blank=True, null=True)
# #     description_ru = models.TextField(blank=True, null=True)
# #     description_ko = models.TextField(blank=True, null=True)
# #     description_cs = models.TextField(blank=True, null=True)
# #     description_sk = models.TextField(blank=True, null=True)
# #     description_pl = models.TextField(blank=True, null=True)
# #     description_hu = models.TextField(blank=True, null=True)
# #     description_th = models.TextField(blank=True, null=True)
# #     name_th = models.CharField(max_length=100, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'machines_manufacturer'


# # class MailerDontsendentry(models.Model):
# #     to_address = models.CharField(max_length=254)
# #     when_added = models.DateTimeField()

# #     class Meta:
# #         managed = False
# #         db_table = 'mailer_dontsendentry'


# # class MailerMessage(models.Model):
# #     message_data = models.TextField()
# #     when_added = models.DateTimeField()
# #     priority = models.CharField(max_length=1)

# #     class Meta:
# #         managed = False
# #         db_table = 'mailer_message'


# # class MailerMessagelog(models.Model):
# #     message_data = models.TextField()
# #     when_added = models.DateTimeField()
# #     priority = models.CharField(max_length=1)
# #     when_attempted = models.DateTimeField()
# #     result = models.CharField(max_length=1)
# #     log_message = models.TextField()
# #     message_id = models.TextField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'mailer_messagelog'


# # class NotificationNoticequeuebatch(models.Model):
# #     pickled_data = models.TextField()

# #     class Meta:
# #         managed = False
# #         db_table = 'notification_noticequeuebatch'


# # class NotificationNoticesetting(models.Model):
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     notice_type = models.ForeignKey('NotificationNoticetype', models.DO_NOTHING)
# #     medium = models.CharField(max_length=1)
# #     send = models.BooleanField()

# #     class Meta:
# #         managed = False
# #         db_table = 'notification_noticesetting'
# #         unique_together = (('user', 'notice_type', 'medium'),)


# # class NotificationNoticetype(models.Model):
# #     label = models.CharField(max_length=40)
# #     display = models.CharField(max_length=50)
# #     description = models.CharField(max_length=100)
# #     default = models.IntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'notification_noticetype'


# # class Oauth2ProviderAccesstoken(models.Model):
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
# #     token = models.CharField(max_length=255)
# #     application = models.ForeignKey('Oauth2ProviderApplication', models.DO_NOTHING)
# #     expires = models.DateTimeField()
# #     scope = models.TextField()

# #     class Meta:
# #         managed = False
# #         db_table = 'oauth2_provider_accesstoken'


# # class Oauth2ProviderApplication(models.Model):
# #     client_id = models.CharField(unique=True, max_length=100)
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     redirect_uris = models.TextField()
# #     client_type = models.CharField(max_length=32)
# #     authorization_grant_type = models.CharField(max_length=32)
# #     client_secret = models.CharField(max_length=255)
# #     name = models.CharField(max_length=255)
# #     skip_authorization = models.BooleanField()

# #     class Meta:
# #         managed = False
# #         db_table = 'oauth2_provider_application'


# # class Oauth2ProviderGrant(models.Model):
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     code = models.CharField(max_length=255)
# #     application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
# #     expires = models.DateTimeField()
# #     redirect_uri = models.CharField(max_length=255)
# #     scope = models.TextField()

# #     class Meta:
# #         managed = False
# #         db_table = 'oauth2_provider_grant'


# # class Oauth2ProviderRefreshtoken(models.Model):
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     token = models.CharField(max_length=255)
# #     application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
# #     access_token = models.OneToOneField(Oauth2ProviderAccesstoken, models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'oauth2_provider_refreshtoken'


# # class PersonsContact(models.Model):
# #     user = models.OneToOneField(AuthUser, models.DO_NOTHING)
# #     street_address = models.CharField(max_length=200, blank=True, null=True)
# #     post_code = models.CharField(max_length=15, blank=True, null=True)
# #     city = models.CharField(max_length=50, blank=True, null=True)
# #     state = models.CharField(max_length=50, blank=True, null=True)
# #     country = models.CharField(max_length=50, blank=True, null=True)
# #     phone = models.CharField(max_length=100, blank=True, null=True)
# #     email = models.CharField(max_length=254, blank=True, null=True)
# #     updated = models.DateTimeField()

# #     class Meta:
# #         managed = False
# #         db_table = 'persons_contact'


# # class PersonsPhysicalattributes(models.Model):
# #     user = models.OneToOneField(AuthUser, models.DO_NOTHING)
# #     height = models.IntegerField(blank=True, null=True)
# #     weight = models.IntegerField(blank=True, null=True)
# #     max_hr = models.IntegerField(blank=True, null=True)
# #     rest_hr = models.IntegerField(blank=True, null=True)
# #     body_fat = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
# #     waist = models.IntegerField(blank=True, null=True)
# #     hip = models.IntegerField(blank=True, null=True)
# #     blood_pressure_dia = models.IntegerField(blank=True, null=True)
# #     blood_pressure_sys = models.IntegerField(blank=True, null=True)
# #     updated = models.DateTimeField()

# #     class Meta:
# #         managed = False
# #         db_table = 'persons_physicalattributes'


# # class PostmanMessage(models.Model):
# #     subject = models.CharField(max_length=120)
# #     body = models.TextField()
# #     sender = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
# #     recipient = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
# #     email = models.CharField(max_length=75)
# #     parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
# #     thread = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
# #     sent_at = models.DateTimeField()
# #     read_at = models.DateTimeField(blank=True, null=True)
# #     replied_at = models.DateTimeField(blank=True, null=True)
# #     sender_archived = models.BooleanField()
# #     recipient_archived = models.BooleanField()
# #     sender_deleted_at = models.DateTimeField(blank=True, null=True)
# #     recipient_deleted_at = models.DateTimeField(blank=True, null=True)
# #     moderation_status = models.CharField(max_length=1)
# #     moderation_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
# #     moderation_date = models.DateTimeField(blank=True, null=True)
# #     moderation_reason = models.CharField(max_length=120)

# #     class Meta:
# #         managed = False
# #         db_table = 'postman_message'


# # class QuestionairesQuestionaire(models.Model):
# #     name = models.CharField(max_length=100)
# #     description = models.TextField(blank=True, null=True)
# #     language = models.CharField(max_length=5)
# #     active = models.BooleanField()
# #     score = models.BooleanField()
# #     editable = models.BooleanField()
# #     created = models.DateTimeField()
# #     updated = models.DateTimeField()
# #     filled = models.BooleanField()
# #     filled_at = models.DateTimeField(blank=True, null=True)
# #     expiration_date = models.DateField()
# #     schema = models.TextField(blank=True, null=True)
# #     options = models.TextField(blank=True, null=True)
# #     data = models.TextField(blank=True, null=True)
# #     created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     filling_user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     template = models.ForeignKey('QuestionairesQuestionairetemplate', models.DO_NOTHING)
# #     updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     concept = models.ForeignKey(ConceptsConcept, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'questionaires_questionaire'


# # class QuestionairesQuestionairetemplate(models.Model):
# #     name = models.CharField(max_length=100)
# #     description = models.TextField(blank=True, null=True)
# #     language = models.CharField(max_length=5, blank=True, null=True)
# #     active = models.BooleanField()
# #     score = models.BooleanField()
# #     created = models.DateTimeField()
# #     updated = models.DateTimeField()
# #     schema = models.TextField(blank=True, null=True)
# #     options = models.TextField(blank=True, null=True)
# #     data = models.TextField(blank=True, null=True)
# #     created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     facility = models.ForeignKey(FacilitiesFacility, models.DO_NOTHING)
# #     updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'questionaires_questionairetemplate'


# # class QuestionairesQuestionairetemplateConcept(models.Model):
# #     questionairetemplate = models.ForeignKey(QuestionairesQuestionairetemplate, models.DO_NOTHING)
# #     concepttemplate = models.ForeignKey(ConceptsConcepttemplate, models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'questionaires_questionairetemplate_concept'
# #         unique_together = (('questionairetemplate', 'concepttemplate'),)


# # class SocialAuthAssociation(models.Model):
# #     server_url = models.CharField(max_length=255)
# #     handle = models.CharField(max_length=255)
# #     secret = models.CharField(max_length=255)
# #     issued = models.IntegerField()
# #     lifetime = models.IntegerField()
# #     assoc_type = models.CharField(max_length=64)

# #     class Meta:
# #         managed = False
# #         db_table = 'social_auth_association'


# # class SocialAuthCode(models.Model):
# #     email = models.CharField(max_length=254)
# #     code = models.CharField(max_length=32)
# #     verified = models.BooleanField()

# #     class Meta:
# #         managed = False
# #         db_table = 'social_auth_code'
# #         unique_together = (('email', 'code'),)


# # class SocialAuthNonce(models.Model):
# #     server_url = models.CharField(max_length=255)
# #     timestamp = models.IntegerField()
# #     salt = models.CharField(max_length=65)

# #     class Meta:
# #         managed = False
# #         db_table = 'social_auth_nonce'
# #         unique_together = (('server_url', 'timestamp', 'salt'),)


# # class SocialAuthUsersocialauth(models.Model):
# #     provider = models.CharField(max_length=32)
# #     uid = models.CharField(max_length=255)
# #     extra_data = models.TextField()
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'social_auth_usersocialauth'
# #         unique_together = (('provider', 'uid'),)


# # class SouthMigrationhistory(models.Model):
# #     app_name = models.CharField(max_length=255)
# #     migration = models.CharField(max_length=255)
# #     applied = models.DateTimeField()

# #     class Meta:
# #         managed = False
# #         db_table = 'south_migrationhistory'


# # class TaggitTag(models.Model):
# #     name = models.CharField(unique=True, max_length=100)
# #     slug = models.CharField(unique=True, max_length=100)

# #     class Meta:
# #         managed = False
# #         db_table = 'taggit_tag'


# # class TaggitTaggeditem(models.Model):
# #     tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)
# #     object_id = models.IntegerField()
# #     content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'taggit_taggeditem'


# # class TrainingParametersOnerepmaxestimation(models.Model):
# #     updated = models.DateTimeField()
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     activity = models.ForeignKey(FacilitiesAvailableactivity, models.DO_NOTHING)
# #     value = models.IntegerField()
# #     estimation_type = models.CharField(max_length=1)
# #     visit_activity = models.ForeignKey('VisitsVisitactivity', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'training_parameters_onerepmaxestimation'
# #         unique_together = (('user', 'activity'),)


# # class TrainingTemplatesTemplatecategory(models.Model):
# #     name = models.CharField(max_length=100)
# #     description = models.TextField()

# #     class Meta:
# #         managed = False
# #         db_table = 'training_templates_templatecategory'


# # class TrainingTemplatesTrainingtemplate(models.Model):
# #     facility_id = models.IntegerField()
# #     name = models.CharField(max_length=100)
# #     fast_mode = models.BooleanField()
# #     description = models.TextField(blank=True, null=True)
# #     update_1rm_values = models.BooleanField()
# #     template_category = models.ForeignKey(TrainingTemplatesTemplatecategory, models.DO_NOTHING)
# #     template_picture = models.CharField(max_length=100, blank=True, null=True)
# #     active = models.BooleanField()
# #     created = models.DateField()
# #     updated = models.DateTimeField(blank=True, null=True)
# #     created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
# #     updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
# #     parameters = models.TextField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'training_templates_trainingtemplate'


# # class TrainingTemplatesTrainingtemplateactivity(models.Model):
# #     activity_id = models.IntegerField()
# #     training_template = models.ForeignKey(TrainingTemplatesTrainingtemplate, models.DO_NOTHING)
# #     order_index = models.IntegerField(blank=True, null=True)
# #     active = models.BooleanField()
# #     instruction = models.TextField(blank=True, null=True)
# #     parameters_names = models.TextField(blank=True, null=True)
# #     settings_template = models.TextField(blank=True, null=True)
# #     comments = models.TextField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'training_templates_trainingtemplateactivity'


# # class TrainingsScheduledactivity(models.Model):
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     available_scheduled_activity = models.ForeignKey(FacilitiesAvailablescheduledactivity, models.DO_NOTHING)
# #     active = models.BooleanField()
# #     instruction = models.TextField(blank=True, null=True)
# #     comments = models.TextField(blank=True, null=True)
# #     settings = models.TextField(blank=True, null=True)
# #     status = models.CharField(max_length=1)
# #     ended = models.DateTimeField(blank=True, null=True)
# #     started = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'trainings_scheduledactivity'


# # class TrainingsTrainingactivity(models.Model):
# #     activity = models.ForeignKey(FacilitiesAvailableactivity, models.DO_NOTHING)
# #     training_program = models.ForeignKey('TrainingsTrainingprogram', models.DO_NOTHING)
# #     order_index = models.IntegerField(blank=True, null=True)
# #     active = models.BooleanField()
# #     instruction = models.TextField(blank=True, null=True)
# #     settings = models.TextField(blank=True, null=True)
# #     comments = models.TextField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'trainings_trainingactivity'


# class TrainingsTrainingcategory(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     defaul_training_picture = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'trainings_trainingcategory'


# # class TrainingsTrainingmanager(models.Model):
# #     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
# #     training_program = models.ForeignKey('TrainingsTrainingprogram', models.DO_NOTHING)
# #     start_date = models.DateField()
# #     end_date = models.DateField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'trainings_trainingmanager'


# class TrainingsTrainingprogram(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     facility = models.ForeignKey(FacilitiesFacility, models.DO_NOTHING)
#     name = models.CharField(max_length=100)
#     fast_mode = models.BooleanField()
#     description = models.TextField(blank=True, null=True)
#     update_1rm_values = models.BooleanField()
#     training_category = models.ForeignKey(TrainingsTrainingcategory, models.DO_NOTHING)
#     training_picture = models.CharField(max_length=100, blank=True, null=True)
#     active = models.BooleanField()
#     current = models.BooleanField()
#     parameters = models.TextField(blank=True, null=True)
#     concept = models.ForeignKey(ConceptsConcept, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'trainings_trainingprogram'


# # class UserenaUserenasignup(models.Model):
# #     user = models.OneToOneField(AuthUser, models.DO_NOTHING)
# #     last_active = models.DateTimeField(blank=True, null=True)
# #     activation_key = models.CharField(max_length=40)
# #     activation_notification_send = models.BooleanField()
# #     email_unconfirmed = models.CharField(max_length=254)
# #     email_confirmation_key = models.CharField(max_length=40)
# #     email_confirmation_key_created = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'userena_userenasignup'


# class VisitsVisit(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     visit_type = models.ForeignKey('VisitsVisittype', models.DO_NOTHING)
#     facility = models.ForeignKey(FacilitiesFacility, models.DO_NOTHING)
#     training_program = models.ForeignKey(TrainingsTrainingprogram, models.DO_NOTHING, blank=True, null=True)
#     login = models.DateTimeField()
#     logout = models.DateTimeField(blank=True, null=True)
#     comments = models.TextField()

#     class Meta:
#         managed = False
#         db_table = 'visits_visit'


# # class VisitsVisitactivity(models.Model):
# #     visit = models.ForeignKey(VisitsVisit, models.DO_NOTHING)
# #     activity = models.ForeignKey(FacilitiesAvailableactivity, models.DO_NOTHING)
# #     scheduled_activity = models.ForeignKey(FacilitiesAvailablescheduledactivity, models.DO_NOTHING, blank=True, null=True)
# #     start_time = models.DateTimeField(blank=True, null=True)
# #     end_time = models.DateTimeField(blank=True, null=True)
# #     supervised_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
# #     instruction = models.TextField(blank=True, null=True)
# #     supervisor_comments = models.TextField()
# #     user_comments = models.TextField()
# #     settings = models.TextField(blank=True, null=True)
# #     comments = models.TextField(blank=True, null=True)
# #     results = models.TextField(blank=True, null=True)
# #     status = models.CharField(max_length=1)
# #     training_activity = models.ForeignKey(TrainingsTrainingactivity, models.DO_NOTHING, blank=True, null=True)
# #     raw_data_file = models.CharField(max_length=100, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'visits_visitactivity'


# # class VisitsVisittraining(models.Model):
# #     visit = models.OneToOneField(VisitsVisit, models.DO_NOTHING)
# #     training_program_data = models.TextField()

# #     class Meta:
# #         managed = False
# #         db_table = 'visits_visittraining'


# # class VisitsVisittype(models.Model):
# #     name = models.CharField(max_length=100)
# #     description = models.TextField()
# #     show_in_history = models.BooleanField()

# #     class Meta:
# #         managed = False
# #         db_table = 'visits_visittype'
