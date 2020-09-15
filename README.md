# collegediary1

(college diary website for project submission in Skillenza Codeathon, a small version of collegediary with some less functionality, implemented in django.)



### TechStack:- Django, HTML, CSS, Sqlite3(in developement environment), PostreSQL in Heroku Deployment
### Storage :- None  
:wink:


College Diary is project aimed to list all the projects done in college by students, academic files (such as notes of diffrent class, files of diffrent clubs)..
But the diffrence is that storage facilities for day-to-day purpose are provided by diffrent clouds (Google Drive, DropBox, AWS and many more) and saving the files


itself also decrease the performance of Application which needs to be worked much to be improved, thus I have created this app so as of save links to such files.
Also a short description can be added but not the complete notes and with that too, it will be helpful for everyone because anyone can share technical and notechnical resources of his/her field.
:innocent:


#### Explanation of file stack:- 

-> First project is named as "collegediary1" in terms of file structure.

-> There are three apps created project, users, blog.

-> blog app is based on Post model, users app on Student model and project app on Project model.

-> Rest are views and urls as usual on running server collegediary1.urls calls <app-name>.urls then, <app-name>.urls calls <view-name> then, particular view 
  calls template rendered.  


Demonstration Link:- https://youtu.be/0VgQlKDdzLs 

We have been trying to build this using Django REST Framework but that took too much time and deadline approached so early. Thus, We have created this with Django,
as We already have some working experience with that. 

This is just a minimal model of how things can be done and what can be done with this project. I have been planning to complete this by 26th September, 2020.. and upload
in the repo:- https://github.com/hi-18-K/collegediary 
### If you are checking this repo after that do check out above link. 
:blush:

## Thanks for reading :)
## Feel free to suggest anything new..and helping with resources related with this project!
### :upside_down_face:


for running the system in your local environment follow the instructions:-

1. clone the repository in your local environment.

2. start command-line interface.

3. change path to the project directory.

4. run command - "python manage.py makemigrations blog" -> "python manage.py makemigrations users" -> "python manage.py makemigrations project"

-all (without inverted commas)

5. run the project by command:- 'python manage.py runserver'

6. on your browser open localhost:8000 to check out the functionality.


What we can do further with this site:-
1. using filters(by tags) and search (search bar)for project and blog section.

2. Implement clustring to let the user see relevant data on his/her home screen.

3. Making mobile app and using both at college level.


You can add more if can think of..!!
