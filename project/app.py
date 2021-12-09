# Imports os for functionality
import os

# Imports essential functions for program. Helpers references the load_results function
from helpers import load_results
from flask import Flask, redirect, render_template, request
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

app = Flask(__name__)
# Imports dictionary of questions and images from header
from header import questions, first_images, boujee, social, bs_questions, bs_images, inn, bn_questions, bn_images, pres, mass, counter, round_one, ns_questions, ns_images, winners_dict, keys, nn_questions, nn_images, winners_five_one, winners_five_two, keys_five_one, keys_five_two, winner_one, winner_two, final_winner

@app.route("/", methods=["GET", "POST"])
def index():
    # Resets Global Variables
    var_reset()
    
    # If request.method is GET, return to index and reset variables
    if request.method == "GET":
        return render_template("index.html")
    else:
        # If request.method is POST, go to first 10 questions
        return redirect("/form_one")


@app.route("/form_one", methods=["GET", "POST"])
# Determines if the user is Boujee-Social, Boujee-Non-Social, Non-Boujee-Social, or Non-Boujee-Non-Social
def form_one():
    # Calls on all of the global variables
    global boujee
    global social
    global counter
    global first_images
    
    # Retrieves the first 10 questions and answers
    question = list(questions.keys())[counter]
    answers = questions[question]

    # Loads of all the questions, images, and answers is request.method is GET
    if request.method == "GET":
        return render_template("form_one.html", question = question, answers = answers, images = first_images[counter])

    else:
        # Adds to boujee or social
        if request.form[question] == '1':
            # First 5 questions deal with Boujee category, adds to Boujee Counter if first answer is selected
            if counter < 5:
                boujee += 1
            # Last 5 questions deal with Social category, adds to Social Counter if first answer is selected
            else:
                social += 1

        # Increments counter and reloads the page
        if counter < 9:
            counter += 1
            return redirect("/form_one")

        # Resets counter for future usage
        counter = 0

        if boujee > 2:
            if social > 2:
                # Sends user to Boujee-Social if both Boujee and Social indexes are above 2 (3/5 questions selected)
                return redirect("/form_two")
            # Sends user to Boujee Non-Social if Boujee index is above 2 and Social index is not above 2
            return redirect("/form_three")
        if social > 2:
            # Sends user to Non-Boujee Social if Boujee index is not above 2 and Social index is above 2
            return redirect("/form_four")
        # Sends user to Non-Boujee Non-Social if both Boujee and Social index is not above 2
        return redirect("/form_five")


# Boujee Social
# We have a simple algorithm where points are given to our inn variable if the user selects a particular option
# Points that are not given the inn are effectively given to DeWolfe, even though there is no variable
# If the inn has the majority of the points at the end, then we load the Inn results page
# If not, then we load the DeWolfe page
@app.route("/form_two", methods=["GET", "POST"])
def form_two():

    global counter
    global inn
    global bs_questions
    question = list(bs_questions.keys())[counter]
    answers = bs_questions[question]

    if request.method == "GET":
        return render_template("form_two.html", question = question, answers = answers, images = bs_images[counter])

    else:
        # If they click question one, the inn indicator, then we add a point to the Inn
        if request.form[question] == '1':
            inn += 1

        # Update counter and reload the page
        if counter < 4:
            counter += 1
            return redirect("/form_two")

        # If the Inn indicator has the majority of the points, then load the Inn results page
        if inn > 2:
            values = load_results("The Inn")
            return render_template("results.html", dorm_name = values[0], description = values[1], image = values[2])

        # Else load the DeWolfe results page
        values = load_results("DeWolfe")
        return render_template("results.html", dorm_name = values[0], description = values[1], image = values[2])

        # At this point, the quiz is done


# Boujee Non-Social
# This algorithm is similar to the previous one, but a bit more complex.
# This time, the first three questions decide between The Prescotts and Apley Court
# This uses the same algorithm as last time
# Then, the result from the first three faces off agains Massachusetts Hall
# Again, this uses a similar algorithm to previous
@app.route("/form_three", methods=["GET", "POST"])
def form_three():
    global counter
    global bn_questions
    global bn_images
    global pres
    global mass
    global round_one
    
    question = list(bn_questions.keys())[counter]
    answers = bn_questions[question]

    if request.method == "GET":
        return render_template("form_three.html", question = question, answers = answers, images = bn_images[counter])

    else:
        # If button one is pressed, 
        if request.form[question] == '1':
            # For the first three questions, add points to the Prescotts
            if counter < 3:
                pres += 1

            # For the second three questions, subtract from Mass Hall
            # Mass hall starts at three. This was easier for funtionality
            else:
                mass -= 1
        
        # After the first three questions, decide the winner between The Prescotts and Apley Court
        # If round_one equals 0, Apley is the winner, else prescotts is the winner
        if counter == 2:
            if pres > 1:
                round_one += 1

        # increment counter and reload the page every time
        if counter < 5:
            counter += 1
            return redirect("/form_three")
        
        # Load results pages depending on the answers
        if mass > 1:
            values = load_results("Massachusetts Hall")
            return render_template("results.html", dorm_name = values[0], description = values[1], image = values[2])
        if round_one == 0:
            values = load_results("Apley Court")
            return render_template("results.html", dorm_name = values[0], description = values[1], image = values[2])
        
        values = load_results("The Prescotts")
        return render_template("results.html", dorm_name = values[0], description = values[1], image = values[2])


# Non-Boujee Social
# We now have a very different algorithm, as there are more dorms to deal with
# This algorithm is essentially a tournament between dorms
# View winners_dict in header.py
# winners_dict has three keys, the value for which is a list with two dorms
# In the first round, we eliminate a dorm from each key in the list
# Now winners_dict has three keys, the value of which contains one dorm
# In the second round, the first two keys face off, and one is eliminated
# Now down to two keys
# In the final round, one of the two remaining keys is eliminated
# The final remaining key contains the resulting dorm
@app.route("/form_four", methods=["GET", "POST"])
def form_four():
    global counter
    global ns_questions
    global ns_images
    global winners_dict
    global keys

    question = list(ns_questions.keys())[counter]
    answers = ns_questions[question]

    if request.method == "GET":
        return render_template("form_four.html", question = question, answers = answers, images = ns_images[counter])

    else:
        # If the user selects option one, set id to 1
        # Otherwise set id to 0
        if request.form[question] == '1':
            id = 1
        else:
            id = 0

        # For the first round of the questioning, delete the option from the counter-th entry of winners_dict that was not selected
        if counter < 3:
            winners_list = winners_dict[keys[counter]]
            winners_list.remove(winners_list[id])

        elif counter < 5:
            # For the second round of questioning, delete the entry of the winners_dict that was not selected
            winners_dict.pop(keys[id])
            keys.remove(keys[id])
            # At the end, winners_dict only has one key that's value is one dorm

        # Reload the form at the end and increment counter
        if counter < 4:
            counter += 1

            return redirect("/form_four")

        # Store the winner
        winner = winners_dict[keys[0]]

        # Load the restults form
        values = load_results(winner[0])
        return render_template("results.html", dorm_name = values[0], description = values[1], image = values[2])

        # At this point, the quiz is over


# Non-Boujee Non-Social
# The algorithm is similar two non-boujee social (ns), but more complex
# View winners_five_one and winners_five_two in header.py
# We essentially execute the algorithm in ns twice, resulting in two winners
# We then have the two winners face off in a final round
# The final element left is loaded into the results page
@app.route("/form_five", methods=["GET", "POST"])
def form_five():
    global counter
    global nn_questions
    global nn_images
    global winners_five_one
    global winners_five_two
    global keys_five_one
    global keys_five_two
    global winner_one
    global winner_two
    global final_winner

    question = list(nn_questions.keys())[counter]
    answers = nn_questions[question]

    if request.method == "GET":
        return render_template("form_five.html", question = question, answers = answers, images = nn_images[counter])

    else:
        # We use the same id method as last time
        if request.form[question] == '1':
            id = 1
        else:
            id = 0

        # For the first round of the questioning, delete the option from the counter-th entry of winners_five_one that was not selected
        if counter < 2:
            winners_list = winners_five_one[keys_five_one[counter]]
            winners_list.remove(winners_list[id])

        # For the second round of questioning, delete the entry of winners_five_one that was not selected
        elif counter == 2:
            winners_five_one.pop(keys_five_one[id])
            keys_five_one.remove(keys_five_one[id])

            # Store the winners from the first and second rounds of questioning as winner_one
            winner_one = winners_five_one[keys_five_one[0]]

        # For the third round of questioning, delete the option from the (counter - 3)-th entry of winners_five_two that was not selected
        # Counter minus three, because we want it to be zero indexed
        elif counter < 6:
            winners_list = winners_five_two[keys_five_two[counter - 3]]
            winners_list.remove(winners_list[id])
            
        # For the fourth round of questioning, delete the entry of winners_five_two that was not selected
        elif counter < 8:
            winners_five_two.pop(keys_five_two[id])
            keys_five_two.remove(keys_five_two[id])
        
        # store the winner from the third and fourth rounds as winner_two
        winner_two = winners_five_two[keys_five_two[0]]

        # final_winner is a list of the two winners, winner_one and winner_two
        final_winner = [winner_one, winner_two]

        # For the final round of questioning, delete the entry from final_winner that was not selected
        if counter == 8:
            final_winner.remove(final_winner[id])
        
        # Reload the form and increment counter every time.
        if counter < 8:
            counter += 1
            return redirect("/form_five")

        # Load the final winner in the restults page
        values = load_results(final_winner[0][0])
        return render_template("results.html", dorm_name = values[0], description = values[1], image = values[2])

        # The quiz is now complete

# Function to reset variables
def var_reset():
    # Calls all of the variables
    global boujee
    global social
    global inn
    global pres
    global mass
    global counter
    global round_one
    global winner_one
    global winner_two
    global final_winner
    global winners_dict
    global keys
    global winners_five_one
    global winners_five_two
    global keys_five_one
    global keys_five_two

    # Resets all of the variables and dictionaries so user can retake the quiz when home button is pressed
    boujee = 0
    social = 0
    inn = 0
    pres = 0
    mass = 3
    counter = 0
    round_one = 0
    winner_one = ""
    winner_two = ""
    final_winner = []
    winners_dict = {
        "matthews_thayer": ["Matthews Hall", "Thayer Hall"],
        "grays_strauss": ["Grays Hall", "Strauss Hall"],
        "holworthy_BU": ["Holworthy Hall", "Boston University"]
    }
    keys = ["matthews_thayer", "grays_strauss", "holworthy_BU"]
    winners_five_one = {
        "canaday_hurlbut": ["Canaday Hall", "Hurlbut Hall"],
        "greenough_penny": ["Greenough", "Pennypacker Hall"]
    }
    winners_five_two = {
        "weld_wigg": ["Weld Hall", "Wigglesworth Hall"],
        "hollis_stoughton": ["Hollis Hall", "Stoughton Hall"],
        "lionelmower_uchicago": ["Lionel/Mower Hall", "The University of Chicago"]
    }
    keys_five_one = ["canaday_hurlbut", "greenough_penny"]
    keys_five_two = ["weld_wigg", "hollis_stoughton", "lionelmower_uchicago"]
    return