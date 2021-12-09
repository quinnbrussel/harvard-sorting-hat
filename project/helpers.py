# Import neccessary items for functionality
from header import boujee, social, inn, pres, mass, counter, round_one, winner_one, winner_two, final_winner

# The load_results function will take a dorm name and return the specific dorm name and description from the list of txt files
def load_results(dorm_name):
    # Creates an open dictionary
    links = {}

    # Opens csv file
    file = open("dorms/names.csv")
    
    #Goes through each row of the file
    for row in file:
        # Removes the , from the file
        arr = row.split(",")
        # Opens the second argument of the dictionary
        text = open("dorms/" + arr[1].rstrip())
        image = arr[2]
        # Calls the dictionary value by its first value
        links[arr[0]] = [text.read(), image]
    
    # Programs the descrption based off of the dorm name
    description = links[dorm_name][0]
    image = links[dorm_name][1]

    # Returns the dorm name and description
    return [dorm_name, description, image]
