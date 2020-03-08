# Spending Goal
## Deployed App: https://spending-goal.herokuapp.com
## Video Demo: https://youtu.be/MB57oc4Ck6Q
A web app that lets users specify what percentage of income they want to spend. Users will be able to store a list of items they purchased, see their past goals, and create new ones.

![Home](https://i.imgur.com/jj1aXZC.png)

# To start application locally
```
$ pip3 install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```
# Other notes
## Project Background
This project was based on my personal experience of wanting a financial tracker that focused on spending percentage. Most of the finacial tracker I've encountered usually set their goals through allocating budgets on specific things (eg: dining). By focusing on spending percentage, it didn't give me the hassle to think about under or over budgeting on different things. Basically, all I have to do with the app is to make sure that I don't spend over a custom amount of % from a total amount of x paycheck.
## Project Details
Written in Django, this projects consists of 2 apps which includes the 'spending-goal' itself and a seperate authentication app. The project was then deployed in Heroku hence the external libraries contained in requirements.txt. 



