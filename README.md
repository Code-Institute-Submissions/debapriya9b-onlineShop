Travis Testing
  
  [![Build Status](https://travis-ci.org/debapriya9b/onlineShop.svg?branch=master)](https://travis-ci.org/debapriya9b/onlineShop)
  
Deployed project below:

[Creative Jewelry](https://)

## UX



## User stories



## Wireframes

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
    - I also used [autopep](https://pypi.org/project/autopep8/) to format my python code systematically.

### Stripe payment testing
Please use the below information to test payments.
- Card number - 4242424242424242
- CVC - Any 3 digit number.
- Expiry date - Any date in the future.
- 

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
1. Save a copy of the github repository located at https://github.com/JordenCI/UnicornAttractor---Milestone-4 by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/JordenCI/UnicornAttractor---Milestone-4
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

To deploy Family Hub to heroku, take the following steps:

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

## Acknowledgements