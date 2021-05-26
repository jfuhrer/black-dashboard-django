# High-Fidelity Prototype for financial advisory session documentation - Master Thesis of Jara Fuhrer

This is the high-fidelity prototype developed for the Master's Thesis at University of Zurich. The code is based on an opensource template of creative tim, called "black-dashboard django", version 1.0.1.

<br />



## Table of Contents

* [Demo](#demo)
* [Quick Start](#quick-start)
* [Template Documentation](#template-documentation)
* [Browser Support](#browser-support)
* [Responsiveness](#responsiveness)
* [Resources](#resources)
* [Reporting Issues](#reporting-issues)
* [Technical Support or Questions](#technical-support-or-questions)
* [Licensing of Template](#licensing-of-template)

<br />

## Demo

> To authenticate use the default credentials ***jara / Masterarbeit*** or create a new user. Be aware however, that a new user possibly doesnt have any advisory sessions.

- [Login Page](https://fincon-agent.herokuapp.com/)
- The page is hosted on Heroku, using Amazon Webservices.

<br />

## Quick start

> UNZIP the sources or clone the private repository. After getting the code, open a terminal and navigate to the working directory, with product source code.

```bash
$ # Get the code
$ git clone https://github.com/jfuhrer/black-dashboard-django.git
$ cd black-dashboard-django
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

<br />

## Template Documentation
The documentation for the template used **Black Dashboard Django** is hosted at their [website](https://demos.creative-tim.com/black-dashboard-django/docs/1.0/getting-started/getting-started-django.html).

<br />


## Browser Support

At present, Firefox and Google Chrome are supported.

<img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/chrome.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/firefox.png" width="64" height="64">

<br />

## Responsiveness

Generally, all functionalities are implemented and designed for desktops. Hence, the mobile version is not fully supported.

Nevertheless, the navigation with the side- and topbar as well as the main pages are indeed responsive on smartphones.
(References: iPhone 6/7/8 iOs 11 (375 x 667), Notebook (1280 x 578) and Monitor (1920 x 937))
<br />

## Resources
**ToDo: put in urls**
- Demo:  https://fincon-agent.herokuapp.com/ 
- Download Page: https://github.com/jfuhrer/black-dashboard-django/

<br />

## Reporting Issues

Contact jara.fuhrer@uzh.ch (until September 2021)

<br />

## Technical Support or Questions

Contact jara.fuhrer@uzh.ch (until September 2021)

<br />

## Licensing of Template

- Copyright 2019 - present [Creative Tim](https://www.creative-tim.com/)
- Licensed under [Creative Tim EULA](https://www.creative-tim.com/license)

<br />


