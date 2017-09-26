from flask import Flask, render_template
import random

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template('basic.html', browser_title = 'Homepage', body = 'This is the root')
@my_app.route('/occupations')
def occupations():
    csv = open("occupations.csv","r")
    list_of_lines = csv.readlines()

    del list_of_lines[0]

    jobs = {}

    for line in list_of_lines:
        if line[0] == '"':
            delimited = line.split('",')
            
            delimited[0] = delimited[0][1::]
            
            percent = delimited[len(delimited)-1]
            del delimited[len(delimited)-1]
            
            jobs[''.join(delimited)] = float(percent)
        else:
            delimited = line.split(",")
            jobs[delimited[0]] = float(delimited[1].strip())
        
    jobs.pop("Total") # Removes the now unnecessary footer of the csv
    
    while True:
        for key, value in jobs.items(): # For loop that goes through each value for each key in the dictionary
            #print chance
            ran_num = random.random() * 99.8 # Generates a random number between [0, 1) * total chance.
            #print ran_num
            if ran_num <= value:
                return render_template('occ.html', browser_title = 'Occupations', body = jobs, joblist = jobs.items(), random_occ = key)
        
if __name__ == '__main__':
    my_app.debug = True
    my_app.run()