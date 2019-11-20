Travis Testing
  
  [![Build Status](https://travis-ci.org/debapriya9b/onlineShop.svg?branch=master)](https://travis-ci.org/debapriya9b/onlineShop)
  
Deployed project below:

[Creative Jewelry](https://)

## UX

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies, specifically the **Full Stack Frameworks** module. 

- Project Purpose: In this project, I need to build a full-stack site based around business logic used to control a centrally-owned dataset. I need to set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

### User Stories
"**_As a customer, I would like to_** _______________"

- *view the site* from **any device** *(mobile, tablet, desktop)*. 
- get a jewelry website that can be searched by category, similar items and using text search, making it easy to find specific things or enjoy browsing categories that interest me
- payment procedure should be easy to handle
- have a jewelry website where I can get new designs, fun to wear
- have a jewelry website where I can get custom designed jewelry
- have a jewelry website where I can order customized gift

### Design and Color Scheme

Since the website sells jewelry, I chose bright, vibrant colors.

#### Framework

- [Bootstrap 4]( https://getbootstrap.com/ )
- [jQuery 3.4.1](https://code.jquery.com/jquery/)
    - In an effort to keep the JavaScript minimal, I have decided to use jQuery as foundation to my scripts framework.
- [Django 1.11](https://www.djangoproject.com/download/)
    - Django is a free and open-source web framework that I've used to render the back-end Python with the front-end Bootstrap. We were taught how to use Django 1.11 in the lessons, despite Django 2.0 being the current version,I used Django 1.11

#### Icons

- [Font Awesome 5.8.2](https://fontawesome.com/)

#### Typography
 -  2[Google Fonts](https://fonts.google.com/) were used across the site:
   - 'Liu Jian Mao Cao', cursive
   - 'Quicksand', sans-serif

### Wireframes


## Features

## Features Left to Implement

## Technologies Used

Languages:
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python 3](https://www.python.org/download/releases/3.0/)
- [SQL](https://en.wikipedia.org/wiki/SQL)

Framework / Libraries
- [jQuery](https://jquery.com/)
- [Django](https://docs.djangoproject.com/en/2.2/)
- [Font Awesome](https://fontawesome.com/)
- [Stripe](https://stripe.com/gb)
- [Bootstrap](https://getbootstrap.com/)

Tools:
- [Git](https://en.wikipedia.org/wiki/Git)

Databases:
- [SQLite](https://www.sqlite.org/docs.html)
- [PostgreSQL](https://www.postgresql.org/docs/)


## Automated tests
- I used [Travis](https://travis-ci.org/) to test my test.py files.
[![Build Status](https://travis-ci.org/debapriya9b/onlineShop.svg?branch=master)](https://travis-ci.org/debapriya9b/onlineShop)

### Validation services
- I used [This HTML validator](https://validator.w3.org/) to ensure my code was legal.
    - The only warnings were when the validator failed to recognise the Django template tags.
- I used [This CSS validator](https://jigsaw.w3.org/css-validator/) to ensure my CSS was legal.
            <p>
                <a href="http://jigsaw.w3.org/css-validator/check/referer">
                    <img style="border:0;width:88px;height:31px"
                        src="http://jigsaw.w3.org/css-validator/images/vcss"
                        alt="Valid CSS!" />
                </a>
            </p>
- I used [This Python validator](http://pep8online.com/) to ensure my Python was legal.
    

### Stripe payment testing
Please use the below information to test payments.
- Card number - 4242424242424242
- CVC - Any 3 digit number.
- Expiry date - Any date in the future.

## Manual tests

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [AWS C9](https://aws.amazon.com/cloud9/)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

### Instructions
1. Save a copy of the github repository located at https://github.com/debapriya9b/onlineShop by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/debapriya9b/onlineShop
```
2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. Install all required modules with the command 
```
pip -r requirements.txt.
```
4. Attempt to run project where you will get an error message displaying your host name.
```
python3 manage.py runserver $IP:$PORT
```
5. In your settings.py file add your hostname under 'ALLOWED_HOSTS'.

6. Create a [stripe](https://stripe.com/gb) account and get your API keys.

7. In your local IDE create a file called `env.py`.

8. Inside the env.py file create the below variables.
    - SECRET_KEY
    - STRIPE_PUBLISHABLE
    - STRIPE_SECRET
    - DEFAULT_FROM_EMAIL
    - SERVER_EMAIL
    - EMAIL_HOST
    - EMAIL_HOST_USER
    - EMAIL_HOST_PASSWORD

9. You can now re-run the runserver command to view local project.
```
python3 manage.py runserver $IP:$PORT
```
10. Note - If you are having issues viewing static files you may need to collect static with the below command.
```
python3 manage.py collectstatic
```

## Heroku Deployment

To deploy Creative Jewelry to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
SECRET_KEY | `<your_secret_key>`
STRIPE_PUBLISHABLE | `<your_stripe_publishable>`
STRIPE_SECRET | `<your_stripe_secret>`
DEFAULT_FROM_EMAIL | `<your_from_email>`
SERVER_EMAIL | `<your_server_email>`
EMAIL_HOST | `<your_email_host>`
EMAIL_HOST_USER | `<your_host_user>`
EMAIL_HOST_PASSWORD | `<your_host_password>`

8. In the Heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.


## Content

- www.beadinggem.com for post contents

## Acknowledgements

- The tutors, mentors and support staff at [Code Institute][5]
- [Corey Schafer][10] for his excellent teaching on Youtube about Django, Python, Server setup and more
- The [Django docs][11], which are a paragon of documentation
- The [Python docs][13]
- My mentor Seun Owonikoko

## Disclaimer

The content of this Website is for educational purposes only.

