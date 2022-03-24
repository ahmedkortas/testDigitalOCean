from rest_framework import serializers
from visits.models import VisitsVisit
from visits.models import VisitsVisittype
from visits.models import VisitsVisitactivity
from visits.models import AuthUser

class VisitActivity(serializers.ModelSerializer):
    class Meta:
        model = VisitsVisitactivity
        # fields = ['visit','activity','scheduled_activity','start_time','end_time','supervised_by','instruction','supervisor_comments','user_comments','settings','comments','results','status','training_activity','raw_data_file']
        fields =['start_time','results','end_time']

class Visitor(serializers.ModelSerializer):
    class Meta:
        model = VisitsVisit
        # fields = [ 'facility', 'training_program', 'user', 'logout', 'visit_type', 'id', 'comments', 'login']
        fields=['id']
class VisitType(serializers.ModelSerializer):
    class Meta:
        model = VisitsVisittype
        fields = [ 'name','description','show_in_history']

class AuthUserS(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = [ 'username','id']