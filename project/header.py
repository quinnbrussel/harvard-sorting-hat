# Sets global variables to 0. Utilized in app.py
boujee = 0
social = 0
round_one = 0

# Used in the form four section of app.py. Sets the "matchups" of dorms that are picked against each other
winners_dict = {
    "matthews_thayer": ["Matthews Hall", "Thayer Hall"],
    "grays_strauss": ["Grays Hall", "Strauss Hall"],
    "holworthy_BU": ["Holworthy Hall", "Boston University"]
}
# Matchups of dorms that "compete" against each other in form four
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
winner_one = ""
winner_two = ""
final_winner = []

counter = 0

inn = 0
apley = 0
pres = 0
mass = 3

# Dictionary of first 10 questions that are asked to the user
questions = {
    "Do the homies want to come back to visit your hometown?": ["Spring break plans are verified", "Hell nah"],
    "Verified on the gram?": ["Flex that check", "One day I will be the influencer"],
    "How would you describe your high school?": ["Prep school all the way", "Public school 4 life"],
    "Do you have a business card with your LinkedIn?": ["Please join my cohort of 500+ connections", "I refuse to climb the ladder"],
    "Describe your financial origin": ["I may or may not have an off-shore bank account", "Pretty mid ngl", "Started from the bottom now we here"],
    "Another Friday night rolls around. What shenanigans will you be up to?": ["Dancing with sweaty dudes at Sig Chi", "Lowkey chilling in the common room"],
    "How many times have you ventured into the depths of the basement of Tasty Burger?": ["I ate too many french fries to recall the exact number", "Tasty Burger has a basement?"],
    "How many of the homies do you dap up when you walk into the Berg?": ["It takes me 5 minutes to get to my seat", "I’m an in-and-out kind of person"],
    "How many river functions did you attend in the first month of the semester?": ["One or two", "No, just no"],
    "How many times have you had to hide from that one proctor?": ["Weekly occurrence", "Me and the proctors are besties"]
}
# Dictionary of images that correspond with the first 10 questions
first_images = ["/static/images/bakersfield.jpeg", "/static/images/hudson.jpeg", "/static/images/exeter.jpeg", "/static/images/linked.jpeg", "/static/images/cayman.jpeg", "/static/images/sigma_chi.jpeg", "/static/images/tasty.jpeg", "/static/images/annenberg.jpeg", "/static/images/river.jpeg", "/static/images/zucc.jpeg"]

# Boujee Social Questions (corresponds with form two)
bs_questions = {
    "What kind of music do you listen to while wandering the yard?": ["I'm a basic bitch", "Music hasn’t gotten better since the 1940s"],
    "Legacy Kid?": ["No. Guess I'm not getting into a final club", "Thank you, parents"],
    "A Saturday afternoon of leisure rolls around. What is the activity of choice?": ["Skydiving?", "Time to hit up the South End"],
    "Hotel room or AirBnB?": ["Hotel, sir", "A spacious AirBnB"],
    "Do you own a Robinhood account?": ["I invested in GameStop", "Hell no, I'm not a sheep"]
}

# Boujee Social Images (corresponds with form two)
bs_images = ["/static/images/royals.jpeg", "/static/images/kennedys.jpeg", "/static/images/southend.jpeg", "/static/images/hotel.jpeg", "/static/images/gamestop.jpeg"]

# Boujee Non-Social Quesitons (corresponds with form three)
bn_questions = {
    "Preferred destination to live after college?": ["NYC Baby", "Ye Ole London"],
    "Finance bro bound?": ["I am Wall Street", "I promise I have more in me than that"],
    "It is a rainy Saturday afternoon in Cambridge. What activity will you be up to?": ["Look out the window and listen to lofi beats", "Reading my pleasant novel"],
    "Did you partake in the grad union strike?": ["I walked out of Sanders in solidarity", "No I love Harvard <3"],
    "How would you describe your friend circle in high school?": ["I was friends with all of the homies", "Had more of tight knit group ngl"],
    "Be honest, did you suck up to your high school teachers?": ["I had a good relationship with them, but not like that", "Had to do anything for the rec letters"]
}

# Boujee Non-Social Images (corresponds with form three)
bn_images = ["/static/images/london.jpeg", "/static/images/wallstreet.jpeg", "/static/images/lofi.jpeg", "/static/images/larry.jpeg", "/static/images/supa.jpeg", "/static/images/hermione.jpeg"]


# Non-Boujee Social Questions (corresponds with form four)
ns_questions = {
    "If you were to host a function with the homies, where would you be?": ["Trying my best to stifle the music in my dorm from the proctor", "My beautiful and sticky-floored common room"],
    "What was your activity of choice at your high school parties?": ["I ran the pong table", "Getting those snapchats"],
    "Have you ever been blitzed during the middle of the day in a school week?": ["I have larger priorities than that", "Possibly…"],
    "Jam session in the dorm or final club chasing?": ["I always love good music", "I will become the elite of the elite"],
    "How much do you actually care about knowledge, fellow first-year students?": ["the pursuit of knowledge in itself... yada yada", "Just hand me the degree tbh"]
}

# Non-Boujee Social Images (corresponds with form four)
ns_images = ["/static/images/sticky.jpeg", "/static/images/jonah.jpeg", "/static/images/john.jpeg", "/static/images/winkle.jpeg", "/static/images/lamont.jpeg"]

# Non-Boujee Non-Social Questions (corresponds with form five)
nn_questions = {
    "Grad student strike version 67621. We burning down the dorm in protest?": ["Can you light bricks on fire?", "No, I love Harvard <3"],
    "Dance party in the dorm?": ["Me dancing is a crime", "Is “I Got A Feeling” still a bop?"],
    "Thoughts on Donald Trump?": ["MAGA 2024", "Praying the Dems keep the House in 2022"],
    "Ah yes, the 1 P.M. Sunday afternoon. Lots of work remains ahead in the tumultuous night but the current moments require procrastination - because, of course. Activity of choice?": ["Family FaceTime", "Gallivanting around the Harvard Square"],
    "How many times do you need the alarm to blare in the morning to wake up?": ["I am a literal rock", "The Memorial Church bells get me every time"],
    "Are you a CS concentrator?": ["David Malan is the love of my life", "CS is literally pointless"],
    "Another Sunday brunch at Annenberg rolls around (how do the Sunday hours make any sense btw?). Who are you sitting with?": ["Whoever looks chill tbh", "Eating quickly alone and dipping to do that PSET"],
    "Library of choice during the day?": ["Cabot third-floor", "Widener quiet study room"],
    "Do you drive an electric scooter around campus?": ["I am the king of the yard", "Walking is better for my health",]
}

# Non-Boujee Non-Social Images (corresponds with form five)
nn_images = ["/static/images/larry.jpeg", "/static/images/will.jpeg", "/static/images/prick.jpeg", "/static/images/felipes.jpeg", "/static/images/sleep.jpeg", "/static/images/david.jpeg", "/static/images/annenberg.jpeg", "/static/images/bible.jpeg", "/static/images/scoot.jpeg"]
