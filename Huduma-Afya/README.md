# Huduma-Afya

>[Dunstan MMbehero](https://github.com/ubuntustan/Huduma-Afya.git)

  
# Description  
A web application for outpatient medical services for hospitals online .

Topics
Resources
## Presentation slides
[Presentation slides](https://docs.google.com/presentation/d/1khnG0TcjMkrqP_XgCuoQCwJCGj3wo_V5IgBv58K6oyE/edit#slide=id.g72d05592bf_2_111)

##  Live Link  
 Click [View Site]()  to visit the site


## User Story  
  
* Sign in with the application to start using.
* Set up a profile about me 
* Make an appointment online 
* Fill form to describe symptoms.
* View set appointments and time
* Find Contact Information for the health department
* Choose type of doctor for my appointments

## Admin-Home-page
<img src="https://raw.githubusercontent.com/ubuntustan/Huduma-Afya/master/Huduma-Afya/HudumaApp/static/img/admindashboard.png">

## Receptionists
<img src="https://raw.githubusercontent.com/ubuntustan/Huduma-Afya/master/Huduma-Afya/HudumaApp/static/img/reception.png">

## Doctor page
<img src="https://raw.githubusercontent.com/ubuntustan/Huduma-Afya/master/Huduma-Afya/HudumaApp/static/img/doctor.png">

## ERD Diagram
<img src=""> 

## Figma design


## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/ubuntustan/Huduma-Afya.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Huduma-Afya
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations HudumaApp
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.2.4](https://docs.djangoproject.com/en/3.2/)  
* [Heroku](https://heroku.com)  
  
    
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  

## Contact Information   
If you have any question or contributions, please email me at [dunmmbehero@gmail.com]  

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/ubuntustan/stan-awwards/blob/master/LICENSE)  
* Copyright (c) 2021 **Dunstan Mmbehero**
  
  
 
