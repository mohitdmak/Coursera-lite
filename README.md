# Coursera-lite

## A simple educational website where people can teach and from each other in the form of structured Courses.
### Accessible at 

Here, you can login via your gmail account and create an Instructor/Student account as per your requirement.
You can create courses with multiple short modules and provide your own content. Students will enroll for your courses and will rate and provide feedback for your course upon completion, which will be reflected in your profile. 
While students can follow up on instructor to be notified via emails for any updates regarding their courses. 

### To replicate this project on your local machine:

1. Fork and Clone the repo into your working dir
```
git clone <forked_repo_url>
```
**Make sure you have virtualenv and pip modules installed (based on python3.8)**

2. Create a virtualenv
```
virtualenv env
```
3. Install dependencies
```
source env/bin/activate && pip install -r req.txt
```
4. Create a 'secret.py' file under the folder Coursera, containing variables for :
- A django string used for hashing sensitive data
- Your Oauth2 API key
- Your Oauth2 API secret
- Your Sendgrid API key
- Your email sender's email address and password

**Make sure you have installed postgres client for python**

5. Create your migrations
```
python manage.py makemigrations Home
```
6. Migrate your models to create tables in postgres db
```
python manage.py migrate
```
7. Create a superuser for local project
```
python manage.py createsuperuser
```
Run the code in your local machine
```
8. python manage.py runserver
```
**You can now view from the port 8000 of localhost :** http://localhost:8000

###**If you have Docker runtime installed in your machine, skip steps other than 1,4,7 **

9. Start the compose file to run the app in containerized mode
```
docker-compose up
```

10. Also set the Debug=True if any errors crop up during development.
