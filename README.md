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
I also kept the user stories in a Google Sheet that held the development tasks associated with
 

### Wireframes and ERD

Mobile and desktop wireframes for each web page within the application were initially drawn using pen and paper, and subsequently created and developed on using [Balsamiq](https://balsamiq.com/. Some aspects of the initial wireframes are not exactly replicated in the finished application, as requirements and design views change during development.

![Weighting Room mobile wireframe](https://i.imgur.com/6o3f3XX.png)
![Weighting Room desktop wireframe](https://i.imgur.com/7xxEFwS.png)

I used Lucidchart to put together an Entity Relationship Diagram that showed how and through what type of relationship my four data models, Event, EventTimeslot, Booking, and Comment, related to each other.



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


### Frameworks

- Django
- Bootstrap

## Code Validation

### HTML Validation and Beautification
W3C HTML Validator


### CSS Validation

### Python Validation
PEP8 compliance

### JavaScript Validation
- No errors were found when passing through the official [JSHint validator](https://www.jshint.com)

## Testing

### Automated Testing

- This project has partially implemented automated unit testing, namely for the models and resolution of URLs.
- This unit testing was created using Django's TestCase class, a subclass of Python's unittest.
- All data models and their inbuilt class methods are tested, with all tests passing.
- Due to time constraints, automated testing for the views and rendering of templates is incomplete

### Lighthouse

### Manual Testing 

Manually testing the application constantly took place throughout the development process

Reported issues:
 - Site running very slowly

 -

## Noteworthy Bugs

### Site running/loading content very slowly

- Unfixed
- Attempted fixes: Reducing sizes of uploaded images using [TinyPNG](https://tinypng.com/)
Moving some script tags in base.html to the head of the document to ensure they are immediately loaded
- Probable cause - project loading large/excessive amount of template tags 

### Event timeslot booking all timeslots related to event as opposed to a specific single one

- Bug encountered early in development; when attempting to book onesself into a specific event timeslot as a user, the actual outcome was that the user would book themself into all timeslots for the event, or if they were already booked into another timeslot, cancel that existing booking.

- Fix eventually involved restructuring model concept totally to have timeslots as separate models to their event, and linking them to their respective event through a ForeignKey

### Custom static files (CSS/JavaScript) not displaying in production

- Upon deployment to Heroku, the site's custom CSS and JavaScript files were not rendering at all.
- This bug was solved by setting DEBUG to False in settings.py for deployment as well as removing the previously used DISABLE_COLLECTSTATIC config var on Heroku
- When running the server in production, I manually reset the DEBUG value to True.


## Deployment

### Creation of Django Project

- Gunicorn
- Psycopg2
- App creation
- requirements.txt
- Procfile
- env.py in .gitignore to hide secret keys

### Deployment to Heroku

This project was deployed to Heroku using the following steps

## Credits

### Adapted/Repurposed Code

- The functionality for users adding comments along with admin approval for said comments was directly adapted from Code Institute's Codestar Blog project.
- Aspects of the site's visual layout were also heavily inspired by Codestar Blog.


### Online resources

