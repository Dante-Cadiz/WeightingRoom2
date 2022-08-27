# Weighting Room -  a Full Stack Django Project

Deployed version: https://weightingroom.herokuapp.com/

## Index

## Introduction

Weighting Room is a full-stack web application, serving as the web page for a fictional gym. It aims to provide a simple interface for users to book themselves into various gym events and manage their bookings.

### UX

The priority of this project was to ensure that the site's interface and functionality is simple and clear for its users, in order for them to get the most out of the site's event booking service. 

## Development 

This project was planned and developed using Agile methodology. 
To decide upon the features that the site should possess and the relative importance of these features to each other, I first separated the full project goal into 2 main Epics; namely the user experience of the site's users and its admins. I drew up two different sets of user acceptance criteria in order to measure the completion of these Epics within the project. The site's users must be able to view the gym's wide selection of events in detail, create personal accounts to book individual event timeslots, view and cancel their existing bookings, and share, edit, and delete comments publicly on event pages. Site administrators must be able to easily create new events and manage and delete existing ones, along with approving user-submitted comments.
With these Epics defined, I then generated User Stories that worked towards these requirements.

### User Stories

I used GitHub Issues and Projects to record and track the progress on the fulfilment of each individual User Story. The User Stories were created as GitHub issues and then placed on a kanban board made with GitHub Projects. 
![GitHub project tracking user stories](https://i.imgur.com/mzsdoTV.png)
I also kept the user stories in a Google Sheet that held the development tasks associated with them, the Stories' MOSCOW ratings, and their completion status.

The following stories were satisfied through the creation of data models for Event, EventTimeslot, Booking, and Comment, and their subsequent implementation into Django's inbuilt Admin panel

- As a site admin I can post a new event listing so that site users can book themselves into the event

- As a site admin I can edit or delete previously existing events so that I can change their details as necessary to update their status

- As a site admin I can restrict the maximum amount of bookings for an event to a given number so that my events are not overbooked

- As a site admin I can post events with multiple available timeslots so that I can offer a variety of easy to access timeslot options to my users

- As a site admin I can approve and moderate comments for public viewing so that I can ensure they are appropriate and pertinent before being publicly available

The following stories were satisfied by creating the account management system using the Django AllAuth framework then providing the correct internal links in templates to navigate around the site.

- As a site user I can create an account so that I can have access to members-only site features such as event booking and commenting

- As a site user I can log in to the site with prior created account details so that I can access and use the site's member only features


Creation of relevant views and URLs

- As a site user I can book myself into an available event timeslot so that I can securely reserve my position at said event

- As a site user I can see and read about all available events and classes so that I can choose which ones to book myself into and take part in

- As a site user I can navigate across pages of the site to view events so that there is no information overload on a single unpaginated home page

- As a site user I can view my upcoming events that I have booked into so that I can keep a record of them, check for scheduling conflicts, and withdraw from events as necessary

- As a site user I can withdraw from an event I have previously booked into so that my spot is freed up for someone else

- As a site user I can select which time I want to book my event out of multiple available choices so that I can book the event that suits my schedule

- As a site user I can change which time I have booked an event slot for while maintaining my booking so that I can fit the event into my schedule

Building comment functionality

- As a site user I can comment on event pages so that I can share my interest and socialise with other people attending the event

- As a site user I can edit my previously made comments so that I can amend them if I have made a typo or forgotten something

- As a site user I can delete my previously made comments so that I can remove information that I no longer wish to share

The following user story was not satisfied:

- As a site user or admin I can view how many people are attending a given event so that I can choose whether I attend accordingly/view how many people are attending my event to provide for it accordingly

This user story ended up only being an admin feature; in fact in some cases it could be seen as undesirable for a basic user to see how many people were attending an event, as they could be reluctant to book themselves into the event if they are the first booker.


 

### Wireframes and ERD

Mobile and desktop wireframes for each web page within the application were initially drawn using pen and paper, and subsequently created and developed on using [Balsamiq](https://balsamiq.com/. Some aspects of the initial wireframes are not exactly replicated in the finished application, as requirements and design views change during development.

![Weighting Room mobile wireframe](https://i.imgur.com/6o3f3XX.png)
![Weighting Room desktop wireframe](https://i.imgur.com/7xxEFwS.png)

During the project's inception, I also put together an Entity Relationship Diagram that showed how and through what type of relationship my four data models, Event, EventTimeslot, Booking, and Comment, related to each other.



## Features

### Navbar and Footer

- All pages on the site are headed by the same navbar.
- This navbar contains links to the site's home page (by clicking the logo), and depending on whether the current site user is logged in, links to either a login and signup page, or a logout page and a 'My Bookings' page that allows the user to view all of their event bookings.
- On mobile this navbar features a 'hamburger' style dropdown menu in order to avoid overcrowding of the page.

### Home Page - Event List

- The site's home page advertises the gym's upcoming events to users in a list which paginates. The event's timeslots are shown. From there, users can click on individual events which take them 

### User login and account creation

### Event Detail

- Booking Functionality

### 'My Bookings' page

### Commenting


### Admin Functionality

- Administrators are able to create, edit, and delete events and their respective timeslots through accessing the site's admin panel

### Potential Future Features

- Email-based signup and verification to ensure that site user is a member of the Weighting Room gym
- Social media-like public user profiles in which the user can share the events they are attending and have attended, and invite others
- Admin functionality to set recurring events, e.g. 'Every Wednesday at 6.30pm'
- Alerting users to potential timing conflicts in their bookings.

## Technologies Used 

### Languages

- Python
- JQuery/Javascript
- HTML5
- CSS3

### Programs 

- GitHub - Gitpod, Git, Git issues
- Heroku
- PostgreSQL
- Cloudinary 


### Frameworks and packages

- Django
- Django Summernote
- Django Allauth
- Bootstrap

## Code Validation

### HTML Validation and Beautification
W3C HTML Validator


### CSS Validation
- No errors were found when passing through the official [W3C validator](https://jigsaw.w3.org/css-validator/validator)

### Python Validation
- All custom code is PEP8 compliant and was passed through [PEP8Online checker](http://pep8online.com/)

### JavaScript Validation
- No errors were found when passing through the official [JSHint validator](https://www.jshint.com)

## Testing

### Automated Testing

- This project has partially implemented automated unit testing, namely for the models and resolution of URLs.
- This unit testing was created using Django's TestCase class, a subclass of Python's unittest.
- All data models and their inbuilt class methods are tested, with all tests passing.
- Due to time constraints, automated testing for the views and rendering of HTML in templates is incomplete, and the comment form also lacks automated tests.

### Lighthouse

### Manual Testing 

Manually testing the application constantly took place throughout the development process to check for feature functionality.

I tested the UI for functionality and ease of use by letting a third-party user operate the application. They were able to create an account and log in easily, as well as navigating the site and its internal links on both desktop and mobile.

- After booking or commenting on an event, it felt unclear to the user whether their actions had gone through correctly or led to the expected outcome. After this feedback, I introduced the Django messages framework to the project, displaying messages to the user after an action to let them know their interaction with the site was successful.

(picture of message to user here)


## Noteworthy Bugs

### Site running/loading content very slowly

Probable cause - a variety of factors including:
- The project was loading large/excessive amount of template tags
- The project was using very large image file sizes that took too long to render
- Fixed by reducing sizes of uploaded images using [TinyPNG](https://tinypng.com/) and then further reducing image dimensions with MS Paint
Moving some script tags in base.html to the head of the document to ensure they are immediately loaded
-  

### Event timeslot booking all timeslots related to event as opposed to a specific single one

- Bug encountered early in development; when attempting to book onesself into a specific event timeslot as a user, the actual outcome was that the user would book themself into all timeslots for the event, or if they were already booked into another timeslot, cancel that existing booking.

- Fix eventually involved restructuring model concept totally to have timeslots as separate models to their event, and linking them to their respective event through a ForeignKey

### Custom static files (CSS/JavaScript) not displaying in production

- Upon deployment to Heroku, the site's custom CSS and JavaScript files were not rendering at all.
- This bug was solved by setting DEBUG to False in settings.py for deployment as well as removing the previously used DISABLE_COLLECTSTATIC config var on Heroku
- When running the server in development, I manually reset the DEBUG value to True.


## Deployment

Below are the steps to deploy this project to Heroku.

### Local Environment Setup

- Run the terminal command: `pip3 freeze --local > requirements.txt` to create a requirements.txt file for Heroku
- Create the Django project (in this case WeightingRoom) and the app (eventbooker), adding the app's name to the INSTALLED_APPS section of your settings.py file, then migrate changes with `python3 manage.py migrate`
- Create an env.py file containing these environment variables that are ignored by Git:

1. The database URL from [Heroku](https://dashboard.heroku.com/)
2. A 'SECRET_KEY' variable which can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 
3. The Cloudinary URL for storing static files and images provided by [Cloudinary](https://cloudinary.com/) 




### Deployment to Heroku

- Log into [Heroku](heroku.com) and create a new app, choosing a novel name, and choose region
- Add Heroku Postgres in Add-ons in the Resources tab to provide the app's database
- In the Settings tab of Heroku, reveal config vars and add the following keys and values:
1. SECRET_KEY - your Django secret key in your env.py file
2. CLOUDINARY_URL - your Cloudinary key in your env.py file

- Create a Procfile in your workspace containing the following 
```
web: gunicorn PROJECT_NAME.wsgi
```
to allow Heroku to recognise the app's role as a web application.

- Add Heroku to the ALLOWED_HOSTS section in your settings.py file in your workspace
- Ensure all changes are committed to Git at this point
- In the Deploy tab of Heroku, select GitHub as your deployment method and connect the app to the GitHub repository containing this project
- Either enable automatic deploys upon Git commits or manually deploy the branch
- After being notified that the deployment is successful, the app can be viewed and used in the 'View' tab

### Forking the GitHub Project

To make a copy of the GitHub repository to use on your own account, one can fork the repository by doing as follows:
- On the page for the [repository](https://github.com/Dante-Cadiz/WeightingRoom2), go to the 'Fork' button on the top right of the page, and click it to create a copy of the repository which should then be on your own GitHub account.

### Making a Local Clone

- On the page for the [repository](https://github.com/Dante-Cadiz/WeightingRoom2), click the 'Code' button
- To clone the repository using HTTPS, copy the HTTPS URL provided there
- Open your CLI application of choice and change the current working directory to the location where you want the cloned directory to be made.
- Type `git clone`, and then paste the previously copied URL to create the clone

## Credits

### Adapted/Repurposed Code

- The functionality for users adding comments along with admin approval for said comments was directly adapted from Code Institute's [Codestar Blog](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment) project.
- Aspects of the site's visual layout such as the 'hamburger' navbar and site pagination were also heavily inspired by Codestar Blog.
- HTML Components


### Online resources

- StackOverflow answers
- Images collected from [Pexels](https://www.pexels.com/)

### People

- My mentor, Sandeep Aggarwal, who advised throughout the project on both technical and functional aspects
