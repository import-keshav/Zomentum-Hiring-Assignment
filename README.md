# Zomentum-Hiring-Assignment 
<h3>A REST interface for a movie theatre ticket booking system</h3>
 
<h4> TechStack Used</h4>
1. Python (Programming Language)<br>
2. Django (Web Framework)<br>
3. SQLite (Database)<br>

<h5> Entity–Relationship Model </h5>
<img src="https://user-images.githubusercontent.com/34139754/91654777-6ad6a780-eac9-11ea-82eb-905f8e1d10cc.png" align="centre">

<h5> Flow Of Booking A Ticket</h5>
<img src="https://user-images.githubusercontent.com/34139754/91655107-f94c2880-eacb-11ea-9fab-fa39a7ec2973.png">

<h5><a href="https://documenter.getpostman.com/view/6434629/TVCcXUxr"> Postman API's Documentation</a></h5>
<h5><a href="https://www.getpostman.com/collections/43e938bf72db717465fb"> Postman Collection</a></h5>

<h5> API's Postman ScreenShots </h5>
<h6> 1. Book Ticket API (POST Request)</h6>
<img src="https://user-images.githubusercontent.com/34139754/91655541-f1da4e80-eace-11ea-8f27-7dd9ac7d15ca.png">
<h6> 2. Update Ticket Time/Movie Show Time (PUT Request)
<img src="https://user-images.githubusercontent.com/34139754/91655592-585f6c80-eacf-11ea-9e49-1ebaea24ac76.png">
<h6> 3. Tickets for a particular time (GET Request)
<img src="https://user-images.githubusercontent.com/34139754/91655700-2ef31080-ead0-11ea-85af-fa17a75b7edb.png">
<h6> 4. Delete a particular ticket (Delete Request) </h6>
<img src="https://user-images.githubusercontent.com/34139754/91655771-e556f580-ead0-11ea-843a-0c5d70887530.png">
<h6> 5. User’s details based on the ticket id (Get Ticket) </h6>
<img src="https://user-images.githubusercontent.com/34139754/91655829-775efe00-ead1-11ea-8f9e-45a8ffbff429.png">

<h5> Cron Job</h5>
<p>
  For deleting all the tickets which are expired, cron job is created.<br>
  It's Present in Ticket/cron.py
</p>

<h5> API Test Status (All API's are running successfully)</h5>
<img src="https://user-images.githubusercontent.com/34139754/91655427-0833da80-eace-11ea-9e0a-2a80f4f89e91.png">
<p> 
  <b>Tests are present in</b> <br>
  1. Ticket/tests.py<br> 
  2. Movie/tests.py
</p>

<h5> How to setup and run locally </h5>
<p>
  1. Download Codebase <br>
  2. Create python virtual env and activate it <br>
  3. Redirect to Project Home Directory <br>
  4. Install all dependencies of codebase
</p>

    $ pip install -r requirements.txt
<br>
<p>
  5. Setup Database and run migrations
</p>

    $ python manage.py migrate
<br>
<p>
  6. Start the server and run api's successfulluy
</p>

    $ python manage.py runserver

<h5> How to start Cron Job </h5>
<p> After successfully setting up the codebase, run </p>


    $ python manage.py migrate django_cron

    $ python manage.py runcrons

<p>to start the cron job</p>
