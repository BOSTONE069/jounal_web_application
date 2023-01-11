<p style="align:center">
    <img src="rjikm/static/rjikm/logo.png">
</p>

# Regional Journal of Information and Knowledge Management
A web application developed using the Django framework that allows users to submit their articles to the administrator for review and posting. The application allows users to sign up or log in, and then use the submission form to send their articles. The administrator is able to review, approve, and post the articles. The application uses the crispy-forms library to enhance the user interface.


# Table of Contents
- [Installation](#Installation)
- [Usage](#Usage)
- [Troubleshooting](#Troubleshooting)
- [Contribution](#Contribution)
- [Credits](#Credits)
- [License](#License)

# Installation
This project run on the Django framework and 
therefore in the installation you have to create
 the django virtual enviroment and install the package for 
crispy form using 
1. `pip install virtualenv`
2. `myenv\Scripts\activate.bat` or `source myenv/bin/activate`
3. `pip install django`
4. `pip install django-crispy-forms`
5. On local machine you can run the project using `python manage.py runserver`

# Usage
Go to the login page http://127.0.0.1:8000/accounts/login/
Signup if not registered or login with your credentials
After successful login, you will be redirected to submission page
Fill up the submission form and submit the article
The admin can review, approve and post the article from the admin panel

# Troubleshooting
- If you have any issue regarding installation or usage, please raise an issue [here](#https://github.com/BOSTONE069/jounal_web_application)
- If you are getting any error related to crispy forms, please make sure that you have added 'crispy_forms' in your installed apps in settings.py


# Credits
- [Django](#https://www.djangoproject.com/)
- [Crispy-forms](#https://pypi.org/project/django-crispy-forms/)

# License
This project is licensed under the [MIT License](#https://www.mit.edu/~amini/LICENSE.md).


<p style="align:center">
    <img src="RJIKM 1.png">
</p>

<p style="align:center">
    <img src="rjikm 3.png">
</p>

