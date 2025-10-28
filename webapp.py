from flask import Flask, url_for, render_template, request
from markupsafe import Markup
import json

app = Flask(__name__)



@app.route('/')



@app.route('/yearData1')
def render_fact1():
    years = get_year_options()
    # state = request.args.get('state')
    # year = year_highest_average_math(years)
    # fact1 = "In" + year + ", the state with the highest average math is " + state + "."
    # year2 = year_highest_average_verbal(years)
    # fact2 = "In" + year + ", the state with the highest average verbal is " + state + "."
    # year3 = year_highest_average_GPA(years)
    # fact3 = "In" + year + ", the state with the highest average GPA among all academic subjects is " + state "."
    return render_template('page1.html', year_options = years) # funFactA=fact1, funFactB = fact2, funFactC = fact3, funfactD = fact4)

@app.route('/yearData2')
def render_fact2():
    states = get_state_options()
    # years = request.args.net('year')
    # state = final_total_avg_math()
    # fact = "In" + state + ", the total average of math for all years is "+ ___ + "."
    # state2 = final_total_avg_math_males()
    # fact2 = "In" + state2 + ", the total average of verbal for all years is" + ____ + "."
    # state3 = final_total_avg_math_females()
    # fact3 = "In" + state3 + ", the total average of verbal for all years is" + ____ + "."
    # state4 = final_total_avg_verbal()
    # fact4 = "In" + state4 + ", the total average of verbal for all years is" + ____ + "."
    # state5 = final_total_avg_verbal_males()
    # fact5 = "In" + state5 + ", the total average of verbal for all years is" + ____ + "."
    # state6 = final_total_avg_verbal_females()
    # fact6 = "In" + state6 + ", the total average of verbal for all years is" + ____ + "."
    # state7 = final_total_avg_GPA()
    # fact7 = "In" + state7 + ", the total average GPA among all subjects for all years is" + ____ + "."

    return render_template('page2.html', state_options = states) # funFactA = fact1, funFactB = fact2, funFactC = fact3, funfactD = fact4, funFactE = fact5, funFactF = fact6, funFactG = fact7)

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

def get_state_options(): #Fix amount of states showing
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


def year_highest_average_math(year):
    """Return the name of a state in the given year with the highest average math score."""
    with open('school_scores.json') as school_scores:
        states = json.load(school_scores)
    highest=0
    states = ""
    for s in states:
        if s["Years"] == year:
            if s["Total"]["Math"] > highest:
                highest = s["Total"]["Math"]
                states = s["Year"]
    return year

def year_highest_average_verbal(year):
    with open('school_scores.json') as school_scores:
        states = json.load(school_scores)
    highest=0
    states = ""
    for s in states:
        if s["Years"] == year:
            if s["Total"]["Verbal"] > highest:
                highest = s["Total"]["Verbal"]
                states = s["Year"]
    return year

def year_highest_average_GPA(year): #work back on this
    with open('school_scores.json') as school_scores:
        states = json.load(school_scores)
    highest=0
    states = ""
    for s in states:
        if s["Year"] == year:
            if s["Academic Subjects"] > highest:
                highest = s["Academic Subjects"]
                states = s["Year"]
    return
    
    



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