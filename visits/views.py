from ast import And
from cmath import pi
from datetime import date, datetime
from distutils import archive_util
from operator import ne
import os
import re
import time
# from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from visits.models import VisitsVisit
from visits.serializers import Visitor
from visits.serializers import VisitActivity
from visits.models import VisitsVisitactivity
from visits.serializers import AuthUserS
from visits.models import AuthUser
from django.views.decorators.csrf import csrf_exempt
import json
import xlwt
from io import BytesIO


import pandas as pd
from visits.models import FacilitiesAvailableactivity
from visits.serializers import FacilitiesAvailableactivityS

from datetime import datetime

# from visits.models import ActivitiesAllactivity #to check the activitys
# from visits.serializers import allActivity
# from visits.models import ActivitiesActivitygroup
# from visits.serializers import ActivitiesActivitytypeS
# from visits.serializers import VisitType
# from visits.serializers import VisitsVisittype

import itertools

from visits.models import TrainingsTrainingactivity
from visits.serializers import TrainingsTrainingActivityS

from visits.models import TrainingsTrainingprogram
from visits.serializers import TrainingsTrainingprogramSerializer

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

@csrf_exempt
def generateExcelForAVisit(request):
    if request.method == "POST":
      
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        extraPrames = body[0]
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=visits'+\
        datetime.now().strftime("%Y-%m-%d")+'.xls'
        wb=xlwt.Workbook(encoding='utf-8')
        ws=wb.add_sheet('visits')
        # check the value of the first cell and print it out
        print(ws.__dict__)
        ws._cell_overwrite_ok = True
        print(ws.__dict__)
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        font_style.col_width = 1600*200
        columns = ['Visit Id','Use namer', 'Training program',  'visit time ','duration', 'training saission']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
        for col_num in range(6,len(extraPrames)):
            ws.write(row_num, col_num, extraPrames[col_num], font_style)
        font_style = xlwt.XFStyle()
        font_style.col_width = 1600*200
        #pop the first sell of the body array 
        body.pop(0)
        for row in body:
            row_num +=1
            results = row[len(row)-1]
            for col_num in range(len(row)-1):
                ws.write(row_num, col_num, row[col_num], font_style)
            for res in range(len(results)):
                    for keys in results[res]:
                        if(not(keys=="")):
                            ws.write(row_num, extraPrames.index(keys)+5, results[res][keys], font_style)
                    row_num +=1
        col_width = 256 * 20                       # 20 characters wide
        col_height = 256 * 20                      # 20 characters high
        try:
            for i in itertools.count():
                ws.col(i).width = col_width
                ws.row(i).height = col_height   
        except ValueError:
            pass 
        wb.save(response)
        return response


def AllUsers():
    users = AuthUser.objects.all()
    serializer = AuthUserS(users, many=True)
    users=serializer.data
    for user in users:
        user['username'] = user['first_name']+" "+user['last_name']
    return users


def getUsers(request):
    # query all users and send them to the view
    users=AllUsers()
    return JsonResponse(users, safe=False)


@csrf_exempt
def allVisitsForUser(request):   
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user_id = body["user_id"]
        visits = VisitsVisit.objects.raw("SELECT * FROM visits_visit WHERE user_id="+str(user_id)+" ORDER BY login ASC")
        serializer=Visitor(visits, many=True)
        array_of_visits = serializer.data
        for visit in array_of_visits:
            #query the name of the training_program for each visit
            training_program = TrainingsTrainingprogram.objects.raw("SELECT * FROM trainings_trainingprogram WHERE id="+str(visit["training_program"]))
            serializer=TrainingsTrainingprogramSerializer(training_program, many=True)
            visit["training_program"]=serializer.data[0]["name"]
        return JsonResponse(array_of_visits, safe=False)

@csrf_exempt
def VisitActvityAndResults(request):
#    # query all users Visitor 
    if request.method == "POST":
        array_of_training_Activity=[]
        # get the user_id from the request body 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user_id = body["user_id"]
        visits = VisitsVisit.objects.raw("SELECT * FROM visits_visit where user_id ="+str(user_id)+" ORDER BY login ASC")
        serializer = Visitor(visits, many=True)
        array_of_training_Activity=serializer.data
        for visit in array_of_training_Activity:
            #query the visit activity where visit_id = visit["id"]
            visit_activity = VisitsVisitactivity.objects.raw("SELECT * FROM visits_visitactivity WHERE visit_id="+str(visit["id"])+"AND start_time IS NOT NULL ORDER BY start_time ASC")
            serializer=VisitActivity(visit_activity,many=True)
            visit["results"]=serializer.data
        #loop through the array of users and for each user get the visits and if the result is an empty array remove the user from the array
        i = 0
        while(i<len(array_of_training_Activity)):
            j=0
            while(j<len(array_of_training_Activity[i]["results"])):
                if(len(array_of_training_Activity[i]["results"][j]["results"])==0):
                    array_of_training_Activity[i]["results"].pop(j)
                    j-=1
                j+=1
            i+=1
        i=0
        while(i<len(array_of_training_Activity)):
            if(array_of_training_Activity[i]["results"]==[]):
                array_of_training_Activity.pop(i)
                i-=1 
            i+=1
        k=0
        while(k<len(array_of_training_Activity)):
            for j in range(0,len(array_of_training_Activity[k]["results"])):
                #query the facility with the id number 51 and get the name of the facility
                facility = FacilitiesAvailableactivity.objects.raw("SELECT * FROM facilities_availableactivity WHERE id="+str(array_of_training_Activity[k]["results"][j]["activity"]))
                serializer=FacilitiesAvailableactivityS(facility, many=True)
                print(serializer.data)
                array_of_training_Activity[k]["results"][j]["activity"]=serializer.data[0]["name"]
            k+=1
    print(array_of_training_Activity)

    return JsonResponse(array_of_training_Activity, safe=False)

#query training program with the id number 443

def arrManupulation(data):
    result = []
    holder =[]
    holder.append(data[0]);
    for i in range(0,len(data)):
            if (data[i]['user'] != holder[len(holder) - 1]["user"]):
                result.append(holder);
                holder = [];
                holder.append(data[i]);
            else:
                holder.append(data[i]);
            holder.append(data[i]);
    return result

def trainingProgramTransform(data):
    training_program_dict = {}
    #loop over the array check if the training program is a ke in training_program_dict dictionary
    # if yes add the visit to the array corresponding to the training program
    # if no add the training program to the dictionary with the value being an array with the visit
    for visit in data:
        for v in visit:
            if(v["training_program"] in training_program_dict):
                training_program_dict[v["training_program"]].append(v)
            else:
                training_program_dict[v["training_program"]] = [v]

    training_program_result = {}
    for training_program in training_program_dict:
        #query the name of the training program with the id number training_program
        training_program_name = TrainingsTrainingprogram.objects.raw("SELECT * FROM trainings_trainingprogram WHERE id="+str(training_program))
        serializer=TrainingsTrainingprogramSerializer(training_program_name, many=True)
        training_program_result[serializer.data[0]["name"]] = training_program_dict[training_program]
    return training_program_result


def extract_training_program(data):
    array_of_training_program = data.keys()
    settings = {}
    for training_program in array_of_training_program:
        settings[training_program] = {}
    for training_program in array_of_training_program:
        activity_list = []
        activity_list_name=[]
        for v in data[training_program]:
            for r in v['results']:
                obj={}
                if not(r['activity'] in activity_list_name):
                    obj['name'] = r['activity']
                    activity_list_name.append(r['activity'])
                    sett=json.loads(r['settings'])
                    if('units' in sett):
                        obj['units'] = sett['units']
                    if('sets' in r['settings']):
                        obj['setting_sets'] = sett['sets']
                    if('sets' in r['results']):
                        res=json.loads(r['results'])
                        x=res['sets']
                        obj['sets_length'] = len(x)
                    activity_list.append(obj)
            settings[training_program] = activity_list
    return settings



def userTrainingVisitFilter(settings,data, filterArray):
    arr={}
    users={}
    for i in range(0,len(filterArray)):
        users[str(filterArray[i])]=[]
    for prog in settings:
        for i in range(0,len(data[prog])):
            if(data[prog][i]['training_saission'] in filterArray):
                d= data[prog][i]
                d['training_program']=prog
                if not(prog in arr):
                    arr[prog]=[]
                else:
                    arr[prog].append(d)
    for prog in arr:
        #sort the array by training_saission
        arr[prog].sort(key=lambda x: x["training_saission"])  
    return arr  


# @csrf_exempt
# def training(request):
#     # allActivityData = VisitsVisit.objects.raw("SELECT * FROM visits_visit")
#     # serializer=Visitor(allActivityData, many=True)
#     # array_of_visits = serializer.data
#     # for visit in array_of_visits:
#     #     #query the name of the user
#     #     user = AuthUser.objects.raw("SELECT * FROM auth_user WHERE id="+str(visit["user"]))
#     #     serializer=AuthUserS(user, many=True)
#     #     visit["user"]=serializer.data[0]["username"]
#     # # sort the array by user name
#     # array_of_visits.sort(key=lambda x: x["user"])
#     # array_of_visits = arrManupulation(array_of_visits)
#     # #for each item in array_of_visits sort by login 
#     # for visit in array_of_visits:
#     #     visit.sort(key=lambda x: x["login"])
#     # print("progress")
#     # for visits in array_of_visits:
#     #     for visit in visits:
#     #         #query the visit activity where visit_id = visit["id"]
#     #         visit_activity = VisitsVisitactivity.objects.raw("SELECT * FROM visits_visitactivity WHERE visit_id="+str(visit["id"])+"AND start_time IS NOT NULL ORDER BY start_time ASC")
#     #         serializer=VisitActivity(visit_activity,many=True)
#     #         visit["results"]=serializer.data

#     # for visits in array_of_visits:
#     #     i = 0
#     #     while (i<len(visits)):
#     #         if(visits[i]['results']==[]):
#     #             visits.pop(i)
#     #             i-=1
#     #         i+=1
#     # print("here 2")
#     # for visits in array_of_visits:
#     #     j=1
#     #     while(j<len(visits)):
#     #         visits[j-1]['training_saission']=j
#     #         j+=1
#     # array_of_visits =trainingProgramTransform(array_of_visits)

#     f = open('dataFile.txt', encoding="utf8")
#     data = f.read()
#     f.close()
#     data = json.loads(data)
#     # for prog in data:
#     #     for visit in data[prog]:
#     #         #query the name of the activity
#     #         for v in visit['results']:
#     #             activity = FacilitiesAvailableactivity.objects.raw("SELECT * FROM facilities_availableactivity WHERE id="+str(v["activity"]))
#     #             serializer=FacilitiesAvailableactivityS(activity, many=True)
#     #             v["activity"]=serializer.data[0]["name"]

#     # return JsonResponse(data, safe=False)
#     settings = extract_training_program(data)
#     arr={}
#     if request.method == 'POST':
#         body=request.body.decode('utf-8')
       
#         body = json.loads(body)
#         filterArray=body
#         arr=userTrainingVisitFilter(settings,data,filterArray)

#     else:
#         arr=data
    

#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=visits.xlsx'
#     wb=xlwt.Workbook(encoding='utf-8')    
#     dictSheetHolder = {}
#     worksheetNames=[]
#     for prog in arr:
#         #in the string prog replace all the following characters : \ , / , * , ? , : , [ , ].
#         name=prog
#         prog = prog.replace("\\"," ")
#         prog = prog.replace("/"," ")
#         prog = prog.replace("*"," ")
#         prog = prog.replace("?"," ")
#         prog = prog.replace(":"," ")
#         prog = prog.replace("["," ")
#         prog = prog.replace("]"," ")
#         prog = prog.replace("."," ")
#         prog = prog.replace("-"," ")
#         prog = prog.replace("_"," ")
#         for p in worksheetNames:
#             if(str(p).capitalize() == str(prog).capitalize()):
#                 prog +=" dup"
#         if(len(prog)>30):
#             strRes =""
#             prog=prog.split(" ")
#             for i in range(0,len(prog)):
#                 if prog[i]!="":
#                     strRes+=prog[i][0]
#             prog=strRes
#         ws=wb.add_sheet(prog, cell_overwrite_ok=True)
#         worksheetNames.append(prog)
#         dictSheetHolder[name]=ws

    
    # #this will print the first row for each sheet
    # for prog in arr:
    #     default_col =["visit ID","user name","training program","login","duration","training saission"]
    #     ws=dictSheetHolder[prog]
    #     for i in range(0,len(settings[prog])):
    #         if not('units' in settings[prog][i]):
    #             continue
    #         for j in range(1,4):
    #             string="prescribed"
    #             st=""
    #             if(settings[prog][i]['units']=='kg'):
    #                 st=" Resistance"
    #                 string=string+st
    #             elif(settings[prog][i]['units']=='min'):
    #                 st=" Time"
    #                 string=string+st
    #             elif(settings[prog][i]['units']=='s/min'):
    #                 st=" Heart Rate"
    #                 string=string+st
    #             elif(settings[prog][i]['units']=='m'):
    #                 st=" Distance"
    #                 string=string+st
    #             elif(settings[prog][i]['units']=='W'):
    #                 st=" Power"
    #                 string=string+st
    #             default_col.append(settings[prog][i]['name']+" set "+str(j) + string+"["+settings[prog][i]['units']+"]")
    #             default_col.append(settings[prog][i]['name']+" set "+str(j) + st+"["+settings[prog][i]['units']+"]")
    #             default_col.append(settings[prog][i]['name']+" set "+str(j) + " prescribed reps ")
    #             default_col.append(settings[prog][i]['name']+" set "+str(j) + " reps ")
    #         if(settings[prog][i]['units']=='kg'):
    #             default_col.append(settings[prog][i]['name']+" total load"+"["+settings[prog][i]['units']+"]")
    #     for k in range(0,len(default_col)):
    #         ws.write(0,k,default_col[k])
    #     default_col.clear()


    
    # for prog in arr:
    #     row=1
    #     ws=dictSheetHolder[prog]
    #     for i in range(0,len(arr[prog])):
    #         ws.write(row,0,arr[prog][i]['id'])
    #         ws.write(row,1,arr[prog][i]['user'])
    #         ws.write(row,2,arr[prog][i]['training_program'])
    #         ws.write(row,3,arr[prog][i]['login'])
    #         #the duration will be calculated by the difference between the login and logout
    #         # "login": "2021-06-01T05:33:24.012472Z",
    #         # "logout": "2021-06-01T06:18:49.705217Z",
    #         #transform login and logout to date format
    #         # and then substract the two dates
    #         login=arr[prog][i]['login']
    #         logout=arr[prog][i]['logout']
    #         login=datetime.strptime(login, '%Y-%m-%dT%H:%M:%S.%fZ')
    #         logout=datetime.strptime(logout, '%Y-%m-%dT%H:%M:%S.%fZ')
    #         # "duration": "00:05:00"
    #         duration=logout-login
    #         duration=str(duration)
    #         duration=duration.split(".")[0]
    #         ws.write(row,4,duration)
    #         ws.write(row,5,arr[prog][i]['training_saission'])
    #         col=6
    #         initCol=18
    #         for j in arr[prog][i]['results']:
    #             for name in settings[prog]:    
    #                 if (j['activity'] == name['name']):
    #                     total=0
    #                     j['settings'] = json.loads(j['settings'])
    #                     j['results'] = json.loads(j['results'])
    #                     if ("sets" in j['results']):  
    #                         if (j['settings']['units']=='kg' or j['settings']['units']=='lb'): 
    #                             for k in range(0,len(j['results']['sets'])):
    #                                 ws.write(row,col,j['settings']['sets'][k]['load'])
    #                                 col+=1
    #                                 ws.write(row,col,j['results']['sets'][k]['load'])
    #                                 col+=1
    #                                 ws.write(row,col,j['results']['sets'][k]['reps'])
    #                                 col+=1
    #                                 ws.write(row,col,j['results']['sets'][k]['reps'])
    #                                 col+=1
    #                                 total+=j['results']['sets'][k]['reps']*j['results']['sets'][k]['load']
    #                     ws.write(row,initCol,total)
    #                     initCol+=12
    #                     col=initCol+1
                        
    #         row+=1
   
    # wb.save(response)


    # col_width = 2560 * 200                       # 20 characters wide
    # col_height = 256 * 20                      # 20 characters hight
    # try:
    #     for ws in dictSheetHolder:
    #             for i in itertools.count():
    #                 dictSheetHolder[ws].col(i).width = col_width
    #                 dictSheetHolder[ws].row(i).height = col_height
    #             dictSheetHolder[ws].write(10,0,"xxxx")        
    # except ValueError:
    #     pass                                # ignore exception   
    # wb.save(response)


    # return response




def extract_training_program_name():
    trainingProgramHolder ={}
    training_program = TrainingsTrainingprogram.objects.raw("SELECT * FROM trainings_trainingprogram")
    serializer=TrainingsTrainingprogramSerializer(training_program, many=True)
    array_of_training_program = serializer.data
    for training_program in array_of_training_program:
        x=(training_program['id'])
        trainingProgramHolder[x] = training_program['name']
    return trainingProgramHolder

def extract_activity_name():
    activityHolder ={}
    activity = FacilitiesAvailableactivity.objects.raw("SELECT * FROM facilities_availableactivity")
    serializer=FacilitiesAvailableactivityS(activity, many=True)
    array_of_activity = serializer.data
    for activity in array_of_activity:
        x=(activity['id'])
        activityHolder[x] = activity['name']
    return activityHolder

def write_the_col(training_program):
    final_col = []
    for activity in training_program:
        if activity[1] != 'W':   
            for j in range(0,3):
                setsCounter=j+1
                final_col+= [activity[0]+' Prescribed Load '+'set '+str(setsCounter) +'['+str(activity[1])+']',activity[0]+' Load '+'set '+str(setsCounter) +'['+str(activity[1])+']',activity[0]+' Prescribed Reps '+'set '+str(setsCounter) +'['+str(activity[1])+']',activity[0]+' Reps '+'set '+str(setsCounter) +'['+str(activity[1])+']']
            final_col+= [activity[0]+' Total load '+'['+str(activity[1])+']']
            final_col+= [activity[0]+' Total Prescribed load '+'['+str(activity[1])+']']
        else:
            final_col+= [activity[0]+' Prescribed time '+'[min]']
            final_col+= [activity[0]+' Time '+'[min]']
            final_col+= [activity[0]+' Prescribed Power '+'['+str(activity[1])+']']
            final_col+= [activity[0]+' Power '+'['+str(activity[1])+']']
    return final_col

#will add the data into an object of arrays for the data frame
# keys : visit ID, user name ,training program, login, duration, training saission
def addVisitsToArray(visits,objOfKeys):
    for visit in visits:
        objOfKeys['visit ID'].append(visit['id'])
        objOfKeys['user name'].append(visit['user'])
        objOfKeys['training program'].append(visit['training_program'])
        login = visit['login']
        logout = visit['logout']
        login=datetime.strptime(login, '%Y-%m-%dT%H:%M:%S.%fZ')
        logout=datetime.strptime(logout, '%Y-%m-%dT%H:%M:%S.%fZ')
        objOfKeys['login'].append(login)
        duration =str(logout-login)

        if (duration.split(".")[0].find(",")!=-1 ):
            duration = str(duration.split(".")[0])
        else:    
            duration=duration.split(".")[0].split(":")
            duration=int(duration[0])*60+int(duration[1])
        objOfKeys['duration'].append(duration)
        # objOfKeys['duration'].append()
        objOfKeys['training saission'].append(visit['training_saission'])
        for results in visit['results']:
            settings=results['settings']               
            res = results['results']
            total_load = 0
            total_prescribed_load = 0
            if('sets' not in res) or ('units' not in settings):
                continue
            else:
                        #inserting the data 
                number_of_sets=3
                for i in range(0,number_of_sets):
                    if(i>=len(res['sets'])):
                        objOfKeys[results['activity']+' Load '+'set '+str(i+1)+'['+str(settings['units'])+']'].append("")
                        objOfKeys[results['activity']+' Reps '+'set '+str(i+1)+'['+str(settings['units'])+']'].append("")
                    else:
                        total_load+=int(res['sets'][i]['load'])*int(res['sets'][i]['reps'])
                        objOfKeys[results['activity']+' Load '+'set '+str(i+1)+'['+str(settings['units'])+']'].append(res['sets'][i]['load'])
                        objOfKeys[results['activity']+' Reps '+'set '+str(i+1)+'['+str(settings['units'])+']'].append(res['sets'][i]['reps'])
                    if(i<len(settings['sets'])):
                        objOfKeys[results['activity']+' Prescribed Load '+'set '+str(i+1)+'['+str(settings['units'])+']'].append(settings['sets'][i]['load'])
                        objOfKeys[results['activity']+' Prescribed Reps '+'set '+str(i+1)+'['+str(settings['units'])+']'].append(settings['sets'][i]['reps'])
                        total_prescribed_load+=int(settings['sets'][i]['load'])*int(settings['sets'][i]['reps'])
                    else:
                        objOfKeys[results['activity']+' Prescribed Load '+'set '+str(i+1)+'['+str(settings['units'])+']'].append("")
                        objOfKeys[results['activity']+' Prescribed Reps '+'set '+str(i+1)+'['+str(settings['units'])+']'].append("")
                objOfKeys[results['activity']+' Total load '+'['+str(settings['units'])+']'].append(total_load)
                objOfKeys[results['activity']+' Total Prescribed load'+' ['+str(settings['units'])+']'].append(total_prescribed_load)
        max_len = 0
        for key in objOfKeys:
            if len(objOfKeys[key])>max_len:
                max_len = len(objOfKeys[key])
        for key in objOfKeys:
            while len(objOfKeys[key])<max_len:
                objOfKeys[key].append("")
            print(key,len(objOfKeys[key]))
    return objOfKeys









    # i=0
    # for visit_user in visits:
    #     for visit in visits[visit_user]:   
    #         if(visit['training_program']!=training_program):
    #             continue
    #         else:
    #             i+=1
    #             login = visit['login']
    #             logout = visit['logout']
    #             login=datetime.strptime(login, '%Y-%m-%dT%H:%M:%S.%fZ')
    #             logout=datetime.strptime(logout, '%Y-%m-%dT%H:%M:%S.%fZ')
    #             # "duration": "00:05:00"
    #             duration=logout-login
    #             duration=str(duration)
    #             objOfKeys['visit ID'].append(visit['id'])
    #             objOfKeys['user name'].append(visit_user)
    #             objOfKeys['training program'].append(visit['training_program'])
    #             objOfKeys['login'].append(visit['login'])
    #             objOfKeys['duration'].append(duration)
    #             objOfKeys['training saission'].append(visit['training_saission'])
    #             for results in visit['results']:
    #                 settings=results['settings']               
    #                 res = json.loads(results['results'])
    #                 total_load = 0
    #                 total_prescribed_load = 0
    #                 if('sets' not in res) or ('units' not in settings):
    #                     continue
    #                 else:
    #                     #inserting the data 
    #                     number_of_sets=3
    #                     for i in range(0,number_of_sets):
    #                         if(i>=len(res['sets'])):
    #                             objOfKeys[results['activity']+' Load '+' set '+str(i+1)+' ['+str(settings['units'])+']'].append("")
    #                             objOfKeys[results['activity']+' Reps '+' set '+str(i+1)+' ['+str(settings['units'])+']'].append("")
    #                         else:
    #                             total_load+=int(res['sets'][i]['load'])*int(res['sets'][i]['reps'])
    #                             objOfKeys[results['activity']+' Load '+' set '+str(i+1)+' ['+str(settings['units'])+']'].append(res['sets'][i]['load'])
    #                             objOfKeys[results['activity']+' Reps '+' set '+str(i+1)+' ['+str(settings['units'])+']'].append(res['sets'][i]['reps'])
    #                         if(i<len(settings['sets'])):
    #                             objOfKeys[results['activity']+' Prescribed Load  '+' set '+str(i+1)+' ['+str(settings['units'])+']'].append(settings['sets'][i]['load'])
    #                             objOfKeys[results['activity']+' Prescribed Reps '+' set '+str(i+1)+' ['+str(settings['units'])+']'].append(settings['sets'][i]['reps'])
    #                             total_prescribed_load+=int(settings['sets'][i]['load'])*int(settings['sets'][i]['reps'])
    #                         else:
    #                             objOfKeys[results['activity']+' Prescribed Load  '+' set '+str(i+1)+' ['+str(settings['units'])+']'].append("")
    #                             objOfKeys[results['activity']+' Prescribed Reps '+' set '+str(i+1)+' ['+str(settings['units'])+']'].append("")
    #                     objOfKeys[results['activity']+' Total load '+' ['+str(settings['units'])+']'].append(total_load)
    #                     objOfKeys[results['activity']+' Total Prescribed load '+' ['+str(settings['units'])+']'].append(total_prescribed_load)
    #             for obj in objOfKeys:
    #                 if(obj=='visit ID') or (obj=='user name') or (obj=='training program') or (obj=='login') or (obj=='duration') or (obj=='training saission'):
    #                     continue
    #                 elif len(objOfKeys[obj])<len(objOfKeys['visit ID']):
    #                     objOfKeys[obj].append("")                
    # return objOfKeys


def queryVisitsData(usersFilter,TrainingSessions):
    users = AllUsers()
    allActivityData = VisitsVisit.objects.raw("SELECT * FROM visits_visit")
    serializer=Visitor(allActivityData, many=True)
    array_of_visits = serializer.data
    for visit in array_of_visits:
        for user in users:
            if (visit['user'] == user['id']):
                visit['user'] = user['username']
    # sort the array by user name
    array_of_visits.sort(key=lambda x: x["user"])
    array_of_visitsTemp= []
    if(usersFilter!='all'):
        for visit in array_of_visits:
            if(visit['user'] in usersFilter):
                array_of_visitsTemp.append(visit)
        array_of_visits=array_of_visitsTemp

    userHolder={}
    for visit in array_of_visits:
        if(visit["user"] not in userHolder):
            userHolder[visit["user"]]=[]
            userHolder[visit["user"]].append(visit)
        else:
            userHolder[visit["user"]].append(visit)
    for user in userHolder:
        userHolder[user].sort(key=lambda x: x["id"])
        for visit in userHolder[user]:
            #query the name of the training program
            visit_activity = VisitsVisitactivity.objects.raw("SELECT * FROM visits_visitactivity WHERE visit_id="+str(visit["id"])+"AND start_time IS NOT NULL ORDER BY start_time ASC")
            serializer=VisitActivity(visit_activity,many=True)
            visit["results"]=serializer.data
            if (visit['results']==[]):
                indexOfVisit = userHolder[user].index(visit)
                userHolder[user].pop(indexOfVisit)


    trainingProgramHolder = extract_training_program_name()
    for user in userHolder:
        for visit in userHolder[user]:
            if visit['training_program'] in trainingProgramHolder:
                visit['training_program'] = trainingProgramHolder[visit['training_program']]

    activityHolder = extract_activity_name()
    for user in userHolder:
        for visit in userHolder[user]:
            if 'results' in visit:    
                for result in visit['results']:
                    if result['activity'] in activityHolder:
                        result['activity'] = activityHolder[result['activity']]
    newArrHolders = {}
    for user in userHolder:
        userv = []
        for visit in userHolder[user]:
            if 'results' in visit:
                userv.append(visit)
        newArrHolders[user] = userv

    for user in newArrHolders:
        for j in range(0,len(newArrHolders[user])):
            newArrHolders[user][j]['training_saission']=j+1
    
    if (TrainingSessions!='all'):
        arrHolders = {}
        for user in newArrHolders:
            arrHolders[user] = []
            for visit in newArrHolders[user]:
                if visit['training_saission'] in TrainingSessions:
                    arrHolders[user].append(visit)
        return arrHolders

    return newArrHolders

@csrf_exempt
def tr(request):
    print("start...")
    users=[]
    trainingSessions=[]
    if request.method=="POST":
        body = request.body.decode('utf-8')
        body = json.loads(body)
        if('users' in body):
            users=body['users']
        if('TrainingSessions' in body):
            print(body['TrainingSessions'])
            trainingSessions=body['TrainingSessions']

        print(users, trainingSessions)

    if(len(users)==0):
        users=['all']
    if(len(trainingSessions)==0):
        trainingSessions=['all']

    newArrHolders = queryVisitsData(users,trainingSessions)

    
    training_saission_list = {}
    for user in newArrHolders:
        for visit in newArrHolders[user] :
            key = 'training saission ' + str(visit['training_saission'])
            if key not in training_saission_list:
                training_saission_list[key] = []
            training_saission_list[key].append(visit)


    training_activity_list = {}
    
    for training_saission in training_saission_list:
        activity_list = {}
        training_activity_list[training_saission] = []
        for visit in training_saission_list[training_saission]:
            for result in visit['results']:
                result['settings']= json.loads(result['settings'])
                result['results']= json.loads(result['results'])        
                activity_and_units = []
                if('units' not in result['settings']):
                    continue
                activity_and_units.append(result['activity'])
                activity_and_units.append(result['settings']['units'])
                if(len(training_activity_list[training_saission])==0):
                    training_activity_list[training_saission].append(activity_and_units)
                    activity_list[activity_and_units[0]]=activity_and_units[1]
                elif(activity_and_units[0] not in activity_list ):
                    training_activity_list[training_saission].append(activity_and_units)
                    activity_list[activity_and_units[0]]=activity_and_units[1]
                else:
                    if(activity_list[activity_and_units[0]]!=activity_and_units[1]):
                        training_activity_list[training_saission].append(activity_and_units)
                        activity_list[activity_and_units[0]]=activity_and_units[1]

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=visits.xlsx'
    default_col =["visit ID","user name","training program","login","duration","training saission"]
    print("writing files")

    with BytesIO() as b:
        # Use the StringIO object as the filehandle.
        writer = pd.ExcelWriter(b, engine='openpyxl')
        for saission in training_saission_list:
            col_holder=[]
            col_holder=default_col+write_the_col(training_activity_list[saission])
            obj ={}
            for key in col_holder:
                obj[key] = []
            df = pd.DataFrame(addVisitsToArray(training_saission_list[saission],obj)) 
                #create a Panda dataframe from the data
                
                # Write the dataframe to the excel object.
            df.to_excel(writer, sheet_name=saission, index=False)

        writer.save()
        b.seek(0)
        response.write(b.read())
    return response
            
        

    # trainingProgramHolder=[]
    # for user in newArrHolders:
    #     for visit in newArrHolders[user]:
    #         if visit['training_program'] not in trainingProgramHolder:
    #             trainingProgramHolder.append(visit['training_program'])
    # trainingProgramHolder.sort()

    # sheetName ={}
            
    # training_program_activity_holder={}
    # for user in newArrHolders:
    #     for visit in newArrHolders[user]:
    #         if visit['training_program'] not in training_program_activity_holder:
    #             training_program_activity_holder[visit['training_program']]=[]
    #         for result in visit['results']:
    #             if result['activity'] not in training_program_activity_holder[visit['training_program']]:
    #                 #transform result['settings'] to json
    #                 # if the sets unit is in ['kg','lb','cm','m','km','mi','in','ft']
    #                 #then add the activity
    #                 if 'settings' in result:
    #                     result['settings']= json.loads(result['settings'])
    #                     if 'units' in result['settings']:
    #                         if result['settings']['units'] in ['kg','lb','cm','m','km','mi','in','ft','W']:
    #                             trAct= []
    #                             trAct.append(result['activity'])
    #                             trAct.append(result['settings']['units'])
    #                             boolean_options = True
    #                             for act in training_program_activity_holder[visit['training_program']]:
    #                                 if act[0] == result['activity'] and act[1] == result['settings']['units']:
    #                                     boolean_options = False
    #                             if boolean_options:
    #                                 training_program_activity_holder[visit['training_program']].append(trAct)
    # tpah={}
    # for training_program in training_program_activity_holder:
    #     if training_program_activity_holder[training_program] !=[]:
    #         tpah[training_program]=training_program_activity_holder[training_program]

    # for training_program in training_program_activity_holder:
    #     name = training_program
    #     name = name.replace("\\"," ")
    #     name = name.replace("/"," ")
    #     name = name.replace("*"," ")
    #     name = name.replace("?"," ")
    #     name = name.replace(":"," ")
    #     name = name.replace("["," ")
    #     name = name.replace("]"," ")
    #     name = name.replace("."," ")
    #     name = name.replace("-"," ")
    #     name = name.replace("_"," ")
    #     for key in sheetName.keys():
    #         if name.lower() == key.lower() or name.lower() == sheetName[key].lower():
    #             name +=" dup"
    #     if len(name)>30:
    #         arr=name.split(' ')
    #         name=''
    #         for el in arr:
    #             if el == "":
    #                 continue
    #             else:
    #                 name+=el[0]
    #     sheetName[training_program] = name

    


        


    


