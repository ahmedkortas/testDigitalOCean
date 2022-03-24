from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from visits.models import VisitsVisit
from visits.serializers import Visitor
from visits.serializers import VisitActivity
from visits.models import VisitsVisitactivity
from visits.serializers import AuthUserS
from visits.models import AuthUser

import xlwt
import itertools


# Create your views here.
# take a request and return a response
#the request will fetch all the data from the database in the table visits
#the response will be a list of all the data in the table visits
def vistis_view(request):
    if 'GET' == request.method:
        vistsSheetPointer=[]
        vistsSheetPointer.append(0)
        wsHolders=[]  # this will howld the sheets
        #response needs xls with multiple sheets

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=visits'+\
            datetime.now().strftime("%Y-%m-%d")+'.xls'
        wb=xlwt.Workbook(encoding='utf-8')
        wsHolders.append('x')
        # Sheet header, first row
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        font_style.col_width = 1600*200
        columns = ['Facility', 'Training Program', 'User', 'Logout', 'Visit Type', 'Comments', 'Login']
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = VisitsVisit.objects.all().values_list('facility', 'training_program', 'user', 'logout', 'visit_type', 'comments', 'login')
        for row in rows:
            if (row[4] not in vistsSheetPointer):
                vistsSheetPointer.append(row[4])
                while(len(wsHolders) < row[4]+1):
                    wsHolders.append("x")
                wsHolders[row[4]]=[wb.add_sheet('visits Type '+str(row[4])),1]
                for col_num in range(len(columns)):
                    wsHolders[row[4]][0].write(0, col_num, columns[col_num], font_style)
            for col_num in range(len(row)):
                wsHolders[row[4]][0].write(wsHolders[row[4]][1], col_num, str(row[col_num]), font_style)
            wsHolders[row[4]][1]+=1
        col_width = 256 * 20                        # 20 characters wide
        try:
            for ws in wsHolders:
                if ( ws != 'x'):
                    for i in itertools.count():
                      ws[0].col(i).width = col_width
        except ValueError:
            pass                                # ignore exception   
        wb.save(response)
        return response

        # zipped_file = zip_files(myfiles)
        # response = HttpResponse(zipped_file, content_type='application/octet-stream')
        # response['Content-Disposition'] = 'attachment; filename=my_file.zip'


def vistis_view_data(request):
    visits=VisitsVisitactivity.objects.raw("SELECT * FROM visits_visitactivity Where start_time IS NOT NULL ORDER BY visit_id DESC limit 100")
    serializer=VisitActivity(visits, many=True)
    # print(serializer.data)
    # print(serializer.data[5])
    # print("------------------**************")
    # print(serializer.data[0]["results"])
    return JsonResponse(serializer.data, safe=False)
    return response

def visits_view_all_data(request):
    # visits=VisitsVisit.objects.all()
    # serializer=Visitor(visits, many=True)
    # # 12546
    # visitsHolder=[]
    # for i in range(0,20):
    #     vists_data =VisitsVisitactivity.objects.raw("SELECT id,results FROM visits_visitactivity WHERE visit_id="+str(visits[i].id)+" AND results IS NOT NULL AND start_time IS NOT NULL ORDER BY start_time ASC LIMIT 1")
    #     serializer_data=VisitActivity(vists_data, many=True)
    #     # print(serializer_data.data)
    #     visitsHolder.append(serializer_data.data)
    # print(serializer.data[0])
    # print(serializer.data[1])
    # VisitsVisitactivity.objects.raw("SELECT * FROM visits_visitactivity WHERE visit_id="+str(visits[0].id))
    # serializer_data=VisitActivity(vists_data, many=True)
    # print(serializer_data.data)
    
    users=AuthUser.objects.all()
    serializer_users=AuthUserS(users, many=True)
    #we will create an array of objects for each user
    #each array index will hold the user id and user name and all the visit data of that user
    #the visit data will be queried from the database table visits_visits according to the user id
    array_of_users=[]
    for i in range(0,len(serializer_users.data)):
        user_visits=VisitsVisit.objects.raw("SELECT id FROM visits_visit WHERE user_id="+str(serializer_users.data[i]["id"])+" ORDER BY id ASC")
        user_visits_serializer=Visitor(user_visits, many=True)
        array_of_users.append({"user_id":serializer_users.data[i]["id"],"user_name":serializer_users.data[i]["username"],"visits":user_visits_serializer.data})
    print(len(array_of_users))
    for i in range(0,20):
        for j in range(0,len(array_of_users[i]["visits"])):
            vists_data =VisitsVisitactivity.objects.raw("SELECT id,results,start_time,end_time FROM visits_visitactivity WHERE visit_id="+str(array_of_users[i]["visits"][j]["id"])+" AND results IS NOT NULL AND start_time IS NOT NULL ORDER BY start_time ASC LIMIT 1")
            serializer_data=VisitActivity(vists_data, many=True)
            array_of_users[i]["visits"][j]["results"]=serializer_data.data

    return JsonResponse(array_of_users, safe=False)