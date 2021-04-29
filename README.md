# votingapp
 
Hello User....

*Inorder to use this application there are somethings to be done before hand.

*please install the follow requirements :
**1. Python
2. Django ( create a virtual environment and install django in it. Everytime we try to run the application it has to be done through this environment )**
**3. MySQL Client ( pip install mysqlclient )
4. Pillow ( pip install Pillow )**

*disclaimer:
Please Ignore the User Interface. I'm not so good at designing the interface.
If you didn't find any buttons or the form is visible only half the screen please reduce the zoom ratio. For better Experience set the zoom ratio to 70 - 50 %

*The Reasons why i used Django in this Project :
1. It is Simple and easy to use
2. I'm more of a JAVA person ( i use spring boot and hibernate for backend ) so Django is quite similar to the Spring Boot Architecture.
3. Django provides good support with MySQL Database
4. Django is easy to learn and implement

*what is voting application?
*Well now-a-days everyone are updating their business online , similarly the voting that is done physically can be made online.

*In this project , I used Django for developing both backend and frontend. Please go through the documentation if you want to know more about the Django

**Before using the Application ( as user ) The Admin must add the candidates**
*Steps to Add Candidates :
1. Login as Admin/superuser in **"localhost:8000/login"** ( Assuming you have already created a superuser/Admin )
2. you will be redirected to a page and there will be 2 buttons. **Add , Delete** Add will add the candidate , delete will delete the candidate from your database

*Another way of adding Candidates:
1. Login as Admin/Superuser in "localhost:8000/admin" you will see Candidates Table there and Upon clicking **"add"** you can add the candidate

*Steps to run the application: 

1. After cloning the project , open a terminal or command prompt and activate the work environment.
2. In votingapp-->votingapp you must see a **settings.py** file, edit this file through any text editor and change the  database settings to your database settings
3. The following need to be changed in settings.py file:
3.1 **USER , PASSWORD , NAME** Set user to your database username and password as your database password and name as your database name 
5. Run the following commands ( Assuming you have successfully installed the requirements ) :
**"cd votingapp"
"python manage.py makemigrations"**
You must see the structure of table or the SQL command of creating a table
**"python manage.py migrate"**
After executing this command , you must see that many tables will be created in your Database
**"python manage.py runserver"**
After executing this command , python starts the Server on port : 8000
**http://localhost:8000**
open the above link in your browser , you must see that the application will be running.

The following commands used while creating and designing this project :
**django-admin startproject votingapp
cd votingapp
python manage.py startapp votingMVT
python manage.py collectstatic
python manage.py runserver
python manage.py makemigrations
python manage.py migrate**

That's it! you can use the application now
*If you want to be the Admin/Super User of this Application then there are 2 ways :
1. In your workenvironment run the command **python manage.py createsuperuser** and enter the username , email ,  password. Hola ! You have successfully registered as superuser/Admin
2. Another way of creating superuser/Admin is.... After starting the server go to **"localhost:8000/adminregister"** this page is specially designed for registering a superuser/admin

*After registering as superuser/Admin you must be confused where to login , Don't worry inorder to avoid confusion i have used login for both normal user and superuser/Admin
if you register in the application through interface , you will be registering a normal user.
*In profile module after Logging in , you can update your password by entering the current password as "old password" and new password as "new password" and upon clicking submit you will be redirected to login again.
*The homepage is different for both admin and normal user.

*After Logging in as normal user , the user will be redirected to homepage in which the user will be asked to cast their vote. upon clicking the vote to appropriate candidate his vote will be recorded and locked. He/She can't change their vote once casted.
