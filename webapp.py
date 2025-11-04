from flask import Flask, url_for, render_template, request
from markupsafe import Markup
import json

app = Flask(__name__)



@app.route('/')
def render_main():

    return render_template('home.html')


@app.route('/yearData1')
def render_fact1():
    years = get_year_options()
    if "year" in request.args:
        year = request.args.get('year')
        state = request.args.get('state')
        year1 = year_highest_average_math(year)
        fact1 = "In " + year + ", the state with the highest average math is " + str(year1) + "."
        year2 = year_highest_average_verbal(year)
        fact2 = "In " + year + ", the state with the highest average verbal is " + str(year2) + "."
        DataGPA = year_highest_average_GPA(year)
        fact3 = "In " + year + ", the state with the highest average GPA among all academic subjects is " + DataGPA[0] + " and the GPA is " + str(DataGPA[1]) +  "."
        # TotalTakers = total_test_takers_per_year(year)
        # fact4 = "In " + year + ", the total amount of test takers was " + TotalTakers + "."
        return render_template('page1.html', year_options = years, funFact1 = fact1, funFact2 = fact2, funFact3 = fact3)
    return render_template('page1.html', year_options = years)


@app.route('/yearData2')
def render_fact2():
    states = get_state_options()
    if "state" in request.args:
        state = request.args.get('state')
        state1 = average_math_state(state)
        fact1 = "In " + state + ", the total average of math for all years is "+ str(state1) + "."
        state2 = average_math_males(state)
        fact2 = "In " + state + ", the total average of math for males for all years is " + str(state2) + "."
        state3 = average_math_females(state)
        fact3 = "In " + state + ", the total average of math for females for all years is " + str(state3) + "."
        state4 = average_verbal_state(state)
        fact4 = "In " + state + ", the total average of verbal for all years is " + str(state4) + "."
        state5 = average_verbal_males(state)
        fact5 = "In " + state + ", the total average of verbal for males for all years is " + str(state5) + "."
        state6 = average_verbal_females(state)
        fact6 = "In " + state + ", the total average of verbal for females for all years is " + str(state6) + "."
        state7 = average_GPA_by_state(state)
        fact7 = "In " + state + ", the total average GPA among all subjects for all years is " + str(state7) + "."
        return render_template('page2.html', state_options = states, funFact1 = fact1, funFact2 = fact2, funFact3 = fact3, funFact4 = fact4, funFact5 = fact5, funFact6 = fact6, funFact7 = fact7)
    return render_template('page2.html', state_options = states) 

@app.route('/yearData3')
def render_fact3():
    #
    #
    #
    return render_template('page3.html')
    



def get_year_options(): 
    """Return the html code for the drop down menu.  Each option is a state abbreviation from the demographic data."""
    with open('school_scores.json') as school_scores:
        data = json.load(school_scores)
    years=[]
    for d in data:
        if d["Year"] not in years:
            years.append(d["Year"])
    options=""
    for y in years:
        options += Markup("<option value=\"" + str(y) + "\">" + str(y) + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options



def get_state_options():
    with open('school_scores.json') as school_scores:
        data = json.load(school_scores)
    states=[]
    for d in data:
        if d["State"]["Name"] not in states:
            states.append(d["State"]['Name'])
    options=""
    for s in states:
        options +=Markup("<option value=\"" + str(s) + "\">" + str(s) + "</option>")
    return options



def year_highest_average_math(year): # FIX THE SHOWING OF "NONE" AS RESULT
    """Return the name of a state in the given year with the highest average math score."""
    with open('school_scores.json') as school_scores:
        states = json.load(school_scores)
    highest=0
    state = ""
    for s in states:
        if s["Year"] == year:
            if s["Total"]["Math"] > highest:
                highest = s["Total"]["Math"]
                states = s["Year"]
    return year



def year_highest_average_verbal(year): #FIX THE SHOWING OF "NONE" AS RESULT
    with open('school_scores.json') as school_scores:
        states = json.load(school_scores)
    highest=0
    state = ""
    for s in states:
        if s["Year"] == year:
            if s["Total"]["Verbal"] > highest:
                highest = s["Total"]["Verbal"]
                states = s["Year"]
    return year



def year_highest_average_GPA(year): #figure out  how to format decimals
    with open('school_scores.json') as school_scores:
        states = json.load(school_scores)
    highest=0
    state = ""
    for s in states:
        if str(s["Year"]) == year:
            average_GPA = avg_GPA(s["Academic Subjects"])
            if average_GPA > highest:
                highest = average_GPA
                state = s["State"]["Name"]
    return [state, highest]
 

 
def avg_GPA(subjects):
    total= 0
    for subject, data in subjects.items():
        print(subject)
        total += data["Average GPA"]
    return total/6



def average_math_state(state):
    with open ('school_scores.json') as school_scores:
        math_average = json.load(school_scores)
        total = 0
        for d in math_average:
            if d['State']['Name'] == state:
                total += d['Total']['Math']
    return total/10



def average_math_males(state):
    with open('school_scores.json') as school_scores:
        males_math = json.load(school_scores)
        total = 0
        for d in males_math:
            if d['State']['Name'] == state:
                total += d['Gender']['Male']['Math']
    return total/10



def average_math_females(state):
    with open('school_scores.json') as school_scores:
        females_math = json.load(school_scores)
        total = 0
        for d in females_math:
            if d['State']['Name'] == state:
                total += d['Gender']['Female']['Math']  
    return total/10
  

  
def average_verbal_state(state):
    with open('school_scores.json') as school_scores:
        verbal_average = json.load(school_scores)
        total = 0
        for d in verbal_average:
            if d['State']['Name'] == state:
                total += d['Total']['Verbal']
    return total/10



def average_verbal_males(state):
    with open('school_scores.json') as school_scores:
        males_verbal = json.load(school_scores)
        total = 0
        for d in males_verbal:
            if d['State']['Name'] == state:
                total += d['Gender']['Male']['Verbal']  
    return total/10


def average_verbal_females(state):
    with open('school_scores.json') as school_scores:
        females_verbal = json.load(school_scores)
        total = 0
        for d in females_verbal:
            if d['State']['Name'] == state:
                total += d['Gender']['Female']['Verbal']  
    return total/10



def average_GPA_by_state(state):
    with open('school_scores.json') as school_scores:
        GPA_average = json.load(school_scores)
        total = 0
        for d in GPA_average:
            if str(d["State"]["Name"]) == state:
                average_GPA = avg_GPA_state(d["Academic Subjects"])
                total += average_GPA
    return total/10

def avg_GPA_state(subjects):
    total = 0
    for subject, data in subjects.items():
        total += data["Average GPA"]
    return total/6


def avg_by_income_level(Income_level, section):
    with open('school_scores.json') as school_scores:
        family_incomes = json.load(school_scores)
        total = 0
        count = 0
        for d in family_incomes:
            total += d['Family Income'][Income_level][section]
            count += 1
    return total/count



if __name__ == '__main__':
    app.run(debug=True)