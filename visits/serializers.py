from rest_framework import serializers
from visits.models import VisitsVisit
from visits.models import VisitsVisittype
from visits.models import VisitsVisitactivity
from visits.models import AuthUser
from visits.models import ActivitiesAllactivity
from visits.models import TrainingsTrainingprogram
from visits.models import ActivitiesActivitygroup
from visits.models import TrainingsTrainingactivity
from visits.models import FacilitiesAvailableactivity


class VisitActivity(serializers.ModelSerializer):
    class Meta:
        model = VisitsVisitactivity
        fields = ['visit','activity','start_time','end_time','user_comments','settings','results','training_activity']
        # fields ='__all__'
        

class Visitor(serializers.ModelSerializer):
    class Meta:
        model = VisitsVisit
        # fields = [ 'facility', 'training_program', 'user', 'logout', 'visit_type', 'id', 'comments', 'login']
        fields='__all__'
        # fields = ['id','login','logout','training_program_id']

class VisitType(serializers.ModelSerializer):
    class Meta:
        model = VisitsVisittype
        fields = [ 'name','description','show_in_history']

class AuthUserS(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'


class allActivity(serializers.ModelSerializer):
    class Meta:
        model = ActivitiesAllactivity
        fields = '__all__'


class TrainingsTrainingprogramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingsTrainingprogram
        fields = '__all__'

class ActivitiesActivitytypeS(serializers.ModelSerializer):
    class Meta:
        model = ActivitiesActivitygroup
        fields = '__all__'

class Trainingprogram(serializers.ModelSerializer):
    class Meta():
        model =TrainingsTrainingprogram
        fields ='__all__'

class TrainingsTrainingActivityS(serializers.ModelSerializer):
    class Meta():
        model = TrainingsTrainingactivity
        fields =['training_program','activity','name']

class FacilitiesAvailableactivityS(serializers.ModelSerializer):
    class Meta():
        model = FacilitiesAvailableactivity
        fields =['id','all_activity','active','name','picture','animation','description','comments','limit_to_equipment','definition','video']