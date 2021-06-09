# Huduma-Afya

>[Dunstan MMbehero](https://github.com/ubuntustan/Huduma-Afya.git)

  
# Description  
A web application for outpatient medical services for hospitals online .

Topics
Resources

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

## Home-page
<img src="">

## Profile 
<img src="">

## ERD Diagram
<img src=""> 

## Figma design

## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/ubuntustan/Huduma-Afya.gi
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
