    https://youtu.be/mex0Zsod98M
    
    Quinn Brussels and Henry Weiland's (I) project is titled the "Harvard Sorting Hat" with the aim of making a quiz that enables the user to answer a series of questions about their personality, and other characteristics, that ultimately sorts them into a dorm that matches those characteristics (to our intepretation).

    To form our questions and overall impressions of the dorms, we surveyed residents of each of the dorms to find out what they consider the defining characteristics of their living space.
    
    The dorm directory contians 21 text files that each have a description of each dorm that appears on the results page (will be explained in DESIGN.md) after the user is matched with a dorm. The purpose of these text files is to jokingly mock the user's dorm matching and give them a brief description of what lies ahead for them.
    
    The static directory contains all of the images that are loaded in various HTML pages throughout the quiz. These images are referenced using <img src=""> instead of using a link (as the link could be faulty later on). There also is the styles.css file that contains numerous style classes that we created that are referenced throuhghout the HTML projects of the process using class=""

    The template directory contains all of our HTML pages that are utilized in the program. The first, index.html, is our homepage that contains the "Get Started" button that leads to form_one.html. layout.html contains the html four our background and nav bar (bootsrap) which is extended with {% extends "layout.html" %} for each html page. Each other form (one, two, three, four, and five) are loaded based on the results of the users's choices (will be explained in DESIGN.md). Each of these forms contains a question prompt along with answer buttons and an image. New questions are loaded into the form using jinja. Ultimately, at the end, the user is guided to results.html that presents the name of the dorm, a brief descriotion, and an image.

    The requirements.txt is the standard procedure so flask can run.

    app.py is where the algorithim that sorts each user lies. Though the specifics will be explained in DESIGN.md, here is the layout breifly. At the top, numerous files (including os, flask, header, and helpers) are imported to ensure functionality for the program. Helpers is a file that contains the load_results function (utilized in the algorithim) to prevent clutter in app.py. From header, numerous global variables and dictionaries of the questions, dorms, and the image files are imported again to prevent clutter in app.py. In the def index():, we load the home page. This route is called on when the site is opened. The index function also calls on the var_reset function which sets all of the variables back to 0 when the user clicks on the navbar to redirect back to the homepage.

    The algorithim works by first prompting the user with 10 questions (in form_one.html) to sort the user into one of four dorm categories: Boujee-Social Dorm, Boujee-Non-Social Dorm, Non-Boujee-Social Dorm, and the Non-Boujee Non-Social Dorm. Each of these categories contains a bucket of dorms that enables a user to be matched to a specific one. 
    If the user is matched to Boujee-Social from form_one, they will be directed to form_two where they can be matched with the Inn or DeWolfe.
    If the user is matched to Boujee-Non-Social from form_one, they will be directed to form_three where they can be matched with the Apley Court, the Prescotts, or Mass Hall.
    If the user is matched to Non-Boujee-Social from form_one, they will be directed to form_four where they can be matched with Matthews, Thayer, Grays, Strauss, Holworthy or Boston University.
    If the user is matched to Non-Boujee-Non-Social from form_one, they will be directed to form_five where they can be matched with Canaday, Hurlbut, Greenough, Penny, Weld, Wigg, Hollis, Stoughton, Lionel-Mower, or The University of Chicago).

    In each of the respective def forms(), there exists the algorithim that sorts them into the specific dorm (will be elaborated upon extensively in DESIGN.md). After the user is sorted into a specific dorm from their category, they will be directed to the results.html page that contains their dorm name, description, and image. Again, the questions and description is a fun and comical way to personify each dorm; **The descriptions are meant to poke fun at the user, and are not a serious critique**.

    The end of the app.py file contains the var_reset function which resets all of the variables back to 0. This is called back in the index function so the program essentially "resets" when it is restarted.
    
    The program can be run using flask run in the terminal which will launch a website with all of the questions pre-loaded.
    

