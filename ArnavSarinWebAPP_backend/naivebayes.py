import xlrd
import numpy as np

from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Covid_Input(BaseModel):
    developer_data : str
    inp_fever : float
    inp_body_pain : float
    inp_age : float
    inp_runny_nose : float
    inp_diff_breath : float
    

@app.post("/")
def naive_bayes_covid(covid_inp : Covid_Input):


#    print(covid_inp.inp_fever)
#    print(covid_inp.inp_body_pain)
#    print(covid_inp.inp_age)
#    print(covid_inp.inp_runny_nose)
#    print(covid_inp.inp_diff_breath)

    #Location of the file
    loc = "/Users/arnavsarin/Desktop/chatbot_backend/data.xlsx"

    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    # For row 0 and column 0
    #print(sheet.cell_value(row, column))

    print("\nWELCOME TO NAIVE-BAYES CLASSIFIER BACKEND FOR COVID BY ARNAV SARIN")

#    print("\nDO YOU WANT DEVELOPER DATA: input yes or no")
#    extra_data = str(input())
    extra_data = covid_inp.developer_data
    extra_data = extra_data.strip()
    extra_data = extra_data.upper()
    if(extra_data=="YES"):
        extra_data_bool=True
    else:
        extra_data_bool = False
        

    prob_scenario = { '98.0' : 0.0, '99.0' : 0.0, '100.0' : 0.0, '101.0' : 0.0, '102.0' : 0.0, 'yes_body_pain' : 0.0, 'no_body_pain' : 0.0, '1' : 0.0, '2' : 0.0, '3' : 0.0, '4' : 0.0, '5' : 0.0, 'yes_runny' : 0.0, 'no_runny' : 0.0, 'yes_diff' : 0.0, 'no_diff' : 0.0, 'undef_diff' : 0.0 }


    count_infected = 0
    count_healthy =0
    total =0
    for i in range (1,2000):
        if(sheet.cell_value(i,5)==0):
            count_healthy +=1
        else:
            count_infected +=1
        total+=1
        
    if(extra_data_bool==True):
        print("\nHealthy individuals: " + str(count_healthy))
        print("Infected individuals: " + str(count_infected))
        print("Total: " + str(total))


    #FEVER VARIABLE
    fever_arr = np.array([[98.0,0.0,0.0],[99.0,0.0,0.0],[100.0,0.0,0.0],[101.0,0.0,0.0],[102.0,0.0,0.0]])

    if(extra_data_bool==True):
        print("\nFever_arr Before Fill: ")
        print(fever_arr)

    for i in range (1,2000):
        if(round(sheet.cell_value(i,0))==98.0 and sheet.cell_value(i,5)==1):
            fever_arr[0][1] +=1
        elif(round(sheet.cell_value(i,0))==98.0 and sheet.cell_value(i,5)==0):
            fever_arr[0][2] +=1
        elif(round(sheet.cell_value(i,0))==99.0 and sheet.cell_value(i,5)==1):
            fever_arr[1][1] +=1
        elif(round(sheet.cell_value(i,0))==99.0 and sheet.cell_value(i,5)==0):
            fever_arr[1][2] +=1
        elif(round(sheet.cell_value(i,0))==100.0 and sheet.cell_value(i,5)==1):
            fever_arr[2][1] +=1
        elif(round(sheet.cell_value(i,0))==100.0 and sheet.cell_value(i,5)==0):
            fever_arr[2][2] +=1
        elif(round(sheet.cell_value(i,0))==101.0 and sheet.cell_value(i,5)==1):
            fever_arr[3][1] +=1
        elif(round(sheet.cell_value(i,0))==101.0 and sheet.cell_value(i,5)==0):
            fever_arr[3][2] +=1
        elif(round(sheet.cell_value(i,0))==102.0 and sheet.cell_value(i,5)==1):
            fever_arr[4][1] +=1
        elif(round(sheet.cell_value(i,0))==102.0 and sheet.cell_value(i,5)==0):
            fever_arr[4][2] +=1
            

    #UPDATING PROBABILITY OF EACH FEVER SCENARIO OCCURING
    upd = {'98.0' : ((fever_arr[0][1] + fever_arr[0][2])/total)}
    prob_scenario.update(upd)

    upd = {'99.0' : ((fever_arr[1][1] + fever_arr[1][2])/total)}
    prob_scenario.update(upd)

    upd = {'100.0' : ((fever_arr[2][1] + fever_arr[2][2])/total)}
    prob_scenario.update(upd)

    upd = {'101.0' : ((fever_arr[3][1] + fever_arr[3][2])/total)}
    prob_scenario.update(upd)

    upd = {'102.0' : ((fever_arr[4][1] + fever_arr[4][2])/total)}
    prob_scenario.update(upd)

    if(extra_data_bool==True):
        print("\nFever_arr After fill: ")
        print(fever_arr)

    for i in range (0,5):
        for j in range (1,3):
            if(j==1):
                fever_arr[i][j] = fever_arr[i][j] / count_infected
            if(j==2):
                fever_arr[i][j] = fever_arr[i][j] / count_healthy
       
    if(extra_data_bool==True):
        print("\nFever_arr After probability change: ")
        print(fever_arr)


    #BODY PAIN VARIABLE
    #yes = 1, no = 0
    body_pain_arr = np.array([[1.0,0.0,0.0],[0.0,0.0,0.0]])

    for i in range (1,2000):
        if(sheet.cell_value(i,1)==1 and sheet.cell_value(i,5)==1):
            body_pain_arr[0][1] +=1
        elif(sheet.cell_value(i,1)==1 and sheet.cell_value(i,5)==0):
            body_pain_arr[0][2] +=1
        elif(sheet.cell_value(i,1)==0 and sheet.cell_value(i,5)==1):
            body_pain_arr[1][1] +=1
        elif(sheet.cell_value(i,1)==0 and sheet.cell_value(i,5)==0):
            body_pain_arr[1][2] +=1

    #UPDATING PROBABILITY OF EACH BODY PAIN SCENARIO OCCURING
    upd = {'yes_body_pain' : ((body_pain_arr[0][1] + body_pain_arr[0][2])/total)}
    prob_scenario.update(upd)

    upd = {'no_body_pain' : ((body_pain_arr[1][1] + body_pain_arr[1][2])/total)}
    prob_scenario.update(upd)


    if(extra_data_bool==True):
        print("\nbody_pain_arr After fill: ")
        print(body_pain_arr)

    for i in range (0,2):
        for j in range (1,3):
            if(j==1):
                body_pain_arr[i][j] = body_pain_arr[i][j] / count_infected
            if(j==2):
                body_pain_arr[i][j] = body_pain_arr[i][j] / count_healthy
       
    if(extra_data_bool==True):
        print("\nbody_pain_arr After probability change: ")
        print(body_pain_arr)

    #AGE VARIABLE
    #Age groups:
    #1: 1-18
    #2: 19-30
    #3: 30-45
    #4: 45-60
    #5: 60+
    age_arr = np.array([[1.0,0.0,0.0],[2.0,0.0,0.0],[3.0,0.0,0.0],[4.0,0.0,0.0],[5.0,0.0,0.0]])

    for i in range (1,2000):
        if(sheet.cell_value(i,2)<=18 and sheet.cell_value(i,5)==1):
            age_arr[0][1] +=1
        elif(sheet.cell_value(i,2)<=18 and sheet.cell_value(i,5)==0):
            age_arr[0][2] +=1
        elif(sheet.cell_value(i,2)>18 and sheet.cell_value(i,2)<=30 and sheet.cell_value(i,5)==1):
            age_arr[1][1] +=1
        elif(sheet.cell_value(i,2)>18 and sheet.cell_value(i,2)<=30 and sheet.cell_value(i,5)==0):
            age_arr[1][2] +=1
        elif(sheet.cell_value(i,2)>30 and sheet.cell_value(i,2)<=45 and sheet.cell_value(i,5)==1):
            age_arr[2][1] +=1
        elif(sheet.cell_value(i,2)>30 and sheet.cell_value(i,2)<=45 and sheet.cell_value(i,5)==0):
            age_arr[2][2] +=1
        elif(sheet.cell_value(i,2)>45 and sheet.cell_value(i,2)<=60 and sheet.cell_value(i,5)==1):
            age_arr[3][1] +=1
        elif(sheet.cell_value(i,2)>45 and sheet.cell_value(i,2)<=60 and sheet.cell_value(i,5)==0):
            age_arr[3][2] +=1
        elif(sheet.cell_value(i,2)>60 and sheet.cell_value(i,5)==1):
            age_arr[4][1] +=1
        elif(sheet.cell_value(i,2)>60 and sheet.cell_value(i,5)==0):
            age_arr[4][2] +=1


    #UPDATING PROBABILITY OF EACH AGE SCENARIO OCCURING
    upd = {'1' : ((age_arr[0][1] + age_arr[0][2])/total)}
    prob_scenario.update(upd)

    upd = {'2' : ((age_arr[1][1] + age_arr[1][2])/total)}
    prob_scenario.update(upd)

    upd = {'3' : ((age_arr[2][1] + age_arr[2][2])/total)}
    prob_scenario.update(upd)

    upd = {'4' : ((age_arr[3][1] + age_arr[3][2])/total)}
    prob_scenario.update(upd)

    upd = {'5' : ((age_arr[4][1] + age_arr[4][2])/total)}
    prob_scenario.update(upd)

    if(extra_data_bool==True):
        print("\nage_arr After fill: ")
        print(age_arr)

    for i in range (0,5):
        for j in range (1,3):
            if(j==1):
                age_arr[i][j] = age_arr[i][j] / count_infected
            if(j==2):
                age_arr[i][j] = age_arr[i][j] / count_healthy
          
    if(extra_data_bool==True):
        print("\nage_arr After probability change: ")
        print(age_arr)

    #RUNNY NOSE VARIABLE
    #yes = 1, no = 0
    runny_nose_arr = np.array([[1.0,0.0,0.0],[0.0,0.0,0.0]])

    for i in range (1,2000):
        if(sheet.cell_value(i,3)==1 and sheet.cell_value(i,5)==1):
            runny_nose_arr[0][1] +=1
        elif(sheet.cell_value(i,3)==1 and sheet.cell_value(i,5)==0):
            runny_nose_arr[0][2] +=1
        elif(sheet.cell_value(i,3)==0 and sheet.cell_value(i,5)==1):
            runny_nose_arr[1][1] +=1
        elif(sheet.cell_value(i,3)==0 and sheet.cell_value(i,5)==0):
            runny_nose_arr[1][2] +=1


    #UPDATING PROBABILITY OF EACH RUNNY NOSE SCENARIO OCCURING
    upd = {'yes_runny' : ((runny_nose_arr[0][1] + runny_nose_arr[0][2])/total)}
    prob_scenario.update(upd)

    upd = {'no_runny' : ((runny_nose_arr[1][1] + runny_nose_arr[1][2])/total)}
    prob_scenario.update(upd)

    if(extra_data_bool==True):
        print("\nrunny_nose_arr After fill: ")
        print(runny_nose_arr)

    for i in range (0,2):
        for j in range (1,3):
            if(j==1):
                runny_nose_arr[i][j] = runny_nose_arr[i][j] / count_infected
            if(j==2):
                runny_nose_arr[i][j] = runny_nose_arr[i][j] / count_healthy
        
    if(extra_data_bool==True):
        print("\nrunny_nose_arr After probability change: ")
        print(runny_nose_arr)

    #Difficult Breathing VARIABLE
    #yes = 1, no = 0, undefined = 2
    diff_breath_arr = np.array([[1.0,0.0,0.0],[0.0,0.0,0.0],[2.0,0.0,0.0]])

    for i in range (1,2000):
        if(sheet.cell_value(i,4)==1 and sheet.cell_value(i,5)==1):
            diff_breath_arr[0][1] +=1
        elif(sheet.cell_value(i,4)==1 and sheet.cell_value(i,5)==0):
            diff_breath_arr[0][2] +=1
        elif(sheet.cell_value(i,4)==0 and sheet.cell_value(i,5)==1):
            diff_breath_arr[1][1] +=1
        elif(sheet.cell_value(i,4)==0 and sheet.cell_value(i,5)==0):
            diff_breath_arr[1][2] +=1
        elif(sheet.cell_value(i,4)==-1 and sheet.cell_value(i,5)==1):
            diff_breath_arr[2][1] +=1
        elif(sheet.cell_value(i,4)==-1 and sheet.cell_value(i,5)==0):
            diff_breath_arr[2][2] +=1

    #UPDATING PROBABILITY OF EACH RUNNY NOSE SCENARIO OCCURING
    upd = {'yes_diff' : ((diff_breath_arr[0][1] + diff_breath_arr[0][2])/total)}
    prob_scenario.update(upd)

    upd = {'no_diff' : ((diff_breath_arr[1][1] + diff_breath_arr[1][2])/total)}
    prob_scenario.update(upd)

    upd = {'undef_diff' : ((diff_breath_arr[2][1] + diff_breath_arr[2][2])/total)}
    prob_scenario.update(upd)

    if(extra_data_bool==True):
        print("\ndiff_breath_arr After fill: ")
        print(diff_breath_arr)

    for i in range (0,3):
        for j in range (1,3):
            if(j==1):
                diff_breath_arr[i][j] = diff_breath_arr[i][j] / count_infected
            if(j==2):
                diff_breath_arr[i][j] = diff_breath_arr[i][j] / count_healthy
       
    if(extra_data_bool==True):
        print("\ndiff_breath_arr After probability change: ")
        print(diff_breath_arr)

    if(extra_data_bool==True):
        print("\n PROBABILITY OF ALL THE SCENARIOS OCCURING ")
        print(prob_scenario)


#    print("\nEnter patients information in the format specified")
#    print("\nFever: 98.0, 99.0, 100.0, 101.0, 102.0")
#    inp_fever = float(input())
#    print("\nBody Pain: 1.0(yes), 0.0(no)")
#    inp_body_pain = float(input())
#    print("\nAge: 1.0 (1-18), 2.0 (19-30), 3.0 (30-45), 4.0 (45-60), 5.0 (60+)")
#    inp_age = float(input())
#    print("\nRunny Nose: 1.0(yes), 0.0(no)")
#    inp_runny_nose = float(input())
#    print("\nDifficult Breathing: 1.0(yes), 0.0(no), 2.0(undefined)")
#    inp_diff_breath = float(input())


    #ROW AND COLUMN OF INPUTTED FEVER
    row, column = np.where(fever_arr == covid_inp.inp_fever)
    row_fever = row[0]
    column_fever = column[0]
    #print("\nFEVER INPUT ROW & COLUMN")
    #print(row_fever)
    #print(column_fever)

    #ROW AND COLUMN OF INPUTTED BODY PAIN
    row, column = np.where(body_pain_arr == covid_inp.inp_body_pain)
    row_body_pain = row[0]
    column_body_pain = column[0]
    #print("\nBODY PAIN INPUT ROW & COLUMN")
    #print(row_body_pain)
    #print(column_body_pain)

    #ROW AND COLUMN OF INPUTTED AGE
    row, column = np.where(age_arr == covid_inp.inp_age)
    row_age = row[0]
    column_age = column[0]
    #print("\nAGE INPUT ROW & COLUMN")
    #print(row_age)
    #print(column_age)

    #ROW AND COLUMN OF INPUTTED RUNNY NOSE
    row, column = np.where(runny_nose_arr == covid_inp.inp_runny_nose)
    row_runny_nose = row[0]
    column_runny_nose = column[0]
    #print("\nRUNNY NOSE INPUT ROW & COLUMN")
    #print(row_runny_nose)
    #print(column_runny_nose)

    #ROW AND COLUMN OF INPUTTED DIFFICULTY BREATHING
    row, column = np.where(diff_breath_arr == covid_inp.inp_diff_breath)
    row_diff_breath = row[0]
    column_diff_breath = column[0]
    #print("\nDIFFICULTY BREATHING INPUT ROW & COLUMN")
    #print(row_diff_breath)
    #print(column_diff_breath)

    probability_of_infected_given_events = fever_arr[row_fever][column_fever+1] * body_pain_arr[row_body_pain][column_body_pain+1] * age_arr[row_age][column_age+1] * runny_nose_arr[row_runny_nose][column_runny_nose+1] * diff_breath_arr[row_diff_breath][column_diff_breath+1] * (count_infected/total)
    if(extra_data_bool==True):
        print("\nPROBABILITY OF INFECTED GIVEN EVENTS: " + str(probability_of_infected_given_events))


    probability_of_healthy_given_events = fever_arr[row_fever][column_fever+2] * body_pain_arr[row_body_pain][column_body_pain+2] * age_arr[row_age][column_age+2] * runny_nose_arr[row_runny_nose][column_runny_nose+2] * diff_breath_arr[row_diff_breath][column_diff_breath+2] * (count_healthy/total)
    if(extra_data_bool==True):
        print("\nPROBABILITY OF HEALTHY GIVEN EVENTS: " + str(probability_of_healthy_given_events))


    #TO FIND TOTAL PROBABILITY OF ALL SCENARIOS
    prob_fever_scenario = prob_scenario.get(str(covid_inp.inp_fever))

    if(covid_inp.inp_body_pain==1.0):
        prob_body_pain_scenario = prob_scenario.get('yes_body_pain')
    else:
        prob_body_pain_scenario = prob_scenario.get('no_body_pain')
        
    prob_age_scenario = prob_scenario.get(str(int(covid_inp.inp_age)))

    if(covid_inp.inp_runny_nose==1.0):
        prob_runny_nose_scenario = prob_scenario.get('yes_runny')
    else:
        prob_runny_nose_scenario = prob_scenario.get('no_runny')
        
    if(covid_inp.inp_diff_breath==1.0):
        prob_diff_breath_scenario = prob_scenario.get('yes_diff')
    elif(covid_inp.inp_diff_breath==0.0):
        prob_diff_breath_scenario = prob_scenario.get('no_diff')
    else:
        prob_diff_breath_scenario = prob_scenario.get('undef_diff')
        
    total_prob_scenarios = prob_fever_scenario * prob_body_pain_scenario * prob_age_scenario * prob_runny_nose_scenario * prob_diff_breath_scenario

    if(extra_data_bool==True):
        print("\nTOTAL PROBABILITY SCENARIO OR P(X) TO NORMALIZE is: " + str(total_prob_scenarios))

    probability_of_infected_given_events = probability_of_infected_given_events/ total_prob_scenarios

    probability_of_healthy_given_events = probability_of_healthy_given_events/total_prob_scenarios

    if(extra_data_bool==True):
        print("\nNORMALIZED PROBABILITY OF INFECTED: " + str(probability_of_infected_given_events))

    if(extra_data_bool==True):
        print("\nNORMALIZED PROBABILITY OF HEALTHY: " + str(probability_of_healthy_given_events))


    print("\n\nFINAL RESULTS: ")
    if(probability_of_healthy_given_events>probability_of_infected_given_events):
        print("----------------------")
        print("| PATIENT IS HEALTHY |")
        print("----------------------")
        print("\n")
        return {"patient" : "Healthy"}
#        return "Healthy"
    else:
        print("-----------------------")
        print("| PATIENT IS INFECTED |")
        print("-----------------------")
        print("\n")
        return {"patient" : "Infected"}
#        return "Infected"

    
