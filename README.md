# 4300-Flask-Template

## Contents

- [Summary](#summary)
- [Authentication and Login](#authentication-and-login)
- [Working with the template](#working-with-the-template)
- [MySQL functionality](#mysql-functionality)
- [Tutorial](#tutorial)
- [Causes for errors and fixes](#causes-for-errors-and-fixes)
- [General comments from the author](#general-comments-from-the-author)

## Summary

This is a template for **"CS/INFO 4300 class at Cornell University"**

You will use this template to directly add your Flask code, whose deployment you can control from http://4300showcase.infosci.cornell.edu:9090/#/login. 

## Authentication and Login

To access the dashboard above, you will need an account and password to sign in, which if you're part of the course has already been created for you. These accounts will later be suspended once you are allocated your teams, and new accounts will be provided.

Your current password is your **Net ID**. The application uses JWT to track your status and activity, so clearing localStorage could cause issues, in which case you will have to login again.

## Working with the template

You can clone a copy of this repository directly and use it, or you can use the create template option that has been provided to you. Either way, you can put the repository anywhere with the constraint that it has to be **PUBLIC**. 

You will not be able to run this directly, unless you have **Docker**. 

### Running locally (Flask/Gunicorn only)

You can run the code more easily offline by just creating a Python3.7 virtual enviornment. (You can Google these steps quite easily)
- From there, activate the environment
- Install the files from requirements.txt
- From here everything should run smoothly.

Once done with all this, you can run it using:

```
flask run --host=0.0.0.0 --port=5000
```

### Running locally with Docker (Not recommended)

> Generally, I would recommend you do not install or use Docker unless you have prior experience or expertise with it. Docker for desktop while an excellent service, is _very_ CPU and RAM intensive, and will either be too slow to run or cause a lot of lag, or both. If you still want to go ahead, try to have AT LEAST 8GB Ram and an Intel i5/Ryzen 5 for Windows, including having WSL2 installed or an M1/M2 Macbook. 

Ideally, once you form teams, at least one person on the team can run Docker on their laptop just for quick testing and development, however with the provided service this should not be required.

## MySQL functionality

- Firstly, only use MySQL. No Postgres, no MongoDB and no SQLite
  - If you decide to use these, the server can still build them and deploy them with no problem, but you will be responsible for making it work
- A helper class called **MySQLDatabaseHandler.py** has been provided.
  - This class abstracts the process of creating and managing the database, the engine and the connections.
  - It also abstracts the process of querying the database.
    - The query_executor method will handle any non-select queries, like INSERT, UPDATE, DELETE etc. This is useful for modifying the DB as required
    - The query_selector method will return any SELECT queries made on the DB.
    - Preferably, you will not use any of the above two methods and will instead just implement your own in a more efficient way, but these functions have been provided just as an example, or as support for those who may not be comfortable with SQLAlchemy. If you are comfortable with SQLAlchemy, feel free to write the methods using the ORM framework and supported methods.
    - **NOTE: Do not modify the other methods besides the two mentioned. You can add new ones, and override the above two methods, but do not delete or modify the connection class**
- A few things to keep in mind:
  - If your database does not exist, it should automatically be created by the script (if it doesn't, post it up on ED)
  - Your authentication details for the DB are fixed along with the inital DB. 
    - Do not change these params unless you're aware of how the docker-compose file works.
- The **init.sql** file is special, in that as the name suggests, it's your de-facto DB. It will always be built before your service is ready to run, and is helpful in storing pre-existing data, like test users, some configs and anything else that you may want at run-time.
  - It has the ability to detect its enviornment, and will adapt based on whether you have deployed it on the server or not
    - When running locally, it will be loaded to your local database without any import commands required, and will be re-built each time
    - When deployed on the server however, it will only be run once at the start of deployment. Any changes made to the DB from here on will be permanent, unless destroyed.


## Tutorial

### Step 1: Login and basic setup

- Login to the dashboard at http://4300showcase.infosci.cornell.edu:9090/#/login using your NET_ID and password (also your NET_ID)
- When you login, ensure your dashboard has the following data filled from the image below (check the black arrows only)
  - If it's not filled, reload the page to check if that fixes it. If it doesn't, report it via Gmail or post on ED
- Clicking the URL should re-direct you, but since no deployments will be active, it won't do anything
- Your allocated port indicates on which port your flask service will be deployed

![4300showcase infosci cornell edu_9090_ (1)](https://user-images.githubusercontent.com/55399795/223569113-e820125e-29ff-4baa-8a01-3abf22668180.png)

### Step 2: Understanding the interface

- **BUILD**: Will re-clone and build everything from your GitHub repo, and only from the master/main branch. This is a hard reset, however your data will be preserved. This includes all data from your database and tables. 
- **START**: Containers not in use will typically be turned off. To reboot these containers **WITHOUT RE-BUILDING**, use this button. This will restart your code in the exact same state as you left it, and will not clone or pull any new changes or tamper with data.
- **STOP**: Will stop containers, but not delete them. STOP just turns off your container.
- **DESTROY**: Will destroy all your containers as well as remove any data associated with them. Useful for fresh boot from scratch
- **Container Information Table**: Will show you the status of all your containers. This should tell you if they are on/off. Generally this information is just useful for debugging and for checking any port errors or mismatches, although mostly just useful for TAs
- **Logs**: Should give you an idea of what went wrong during deployment. This of course will not tell you if something is broken during build time, but only what happened when your code was deployed. 

### Step 3: Cloning repo and API creation

- Leave the dashboard for a bit and clone the template from https://github.com/MayoSR/4300-Flask-Template as you see fit, and make your repo public

### Step 4: Test deployment

- Back at the dashboard, in the provided search bar, add the URL of your template from your repository
- Click the **clone** button and wait for a bit till you get a confirmation
- Click **build**, and wait for a minute. If all goes successfully, hitting the refresh button on the Container Information table and the logs tab will show the created data from the service. If this doesn't work, logout and log back in.
- Your URL should now work and display a simple episode searching app
- If it doesn't load initially, give it a second and reload.

## Causes for errors and fixes
- After the build, wait a few seconds as the server will still be loading, especially for larger applications with a lot of setup
- **Containers will turn off midnight at 00:00 hours (12am)**
- **Do not change the Dockerfiles without permission**
- Sometimes, if a deployment doesn't work, you can try logging out and back in to see if it works
- Alternatively, checking the console will tell you what error it is. If it's a 401, then logging in and out should fix it. 
- If it isn't a 401, first try checking the logs or container status. Check if the containers are alive or not, which could cause issues. If the containers are down, try stopping and starting them. If that does not work, you can report it on ED.
- If data isn't important, destroying and then cloning and re-building containers will usually fix the issue (assuming there's no logical error)


## General comments from the author
### Mayank/ms3293

- Since this project was made in the span of a few weeks, it is very likely things will break from time to time. If things do break, you can send an email through the course email or post to ED first.
- If you would like to see stuff added to the dashboard you can send an email thorugh the course email and prefix the title with FEATURE REQUEST
- If you REALLY want to go above and beyond, you can make a request for a special Docker template. These will likely be turned down unless there is an exceptional reason to do so, and you will have to be able to debug it yourself to ensure it works.
- You can ask for allocation of extra port numbers which will be approved or denied on a case by case basis.
- You can also email regarding any questions relating to the service itself. If you think things can be improved or some better logic can be implemented for certain portions, or even just want to know more about the project then feel free to do so.
