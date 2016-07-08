# Django Blog

This is a blog website I created using Django and SQLite. The blog is hosted on [PythonAnywhere](http://ssujan1.pythonanywhere.com) and is accessible to anyone. Feel free to register for a new account, create a post or just check it out!

The reason I created this blog was to learn Django, get familiar with best practices in full stack web dev and having fun with creating a website from scratch. I used [Django Girls tutorial](http://tutorial.djangogirls.org/en/) as a starting point and highly recommend it to anyone who wants to learn Django, even if you're new to programming!

### Blog Features

Below is a list of features that the blog currently has or that will be implemented.
- [ ] Social Login
- [x] Sign up/Login for Account
- [x] Account Profile
- [x] Create Posts
- [ ] Create Topic Pages (similar to Reddit)
- [x] [Posts support Markdown](https://github.com/adi-/django-markdownx)
- [ ] [Async Search for Posts](https://django-ajax-search.readthedocs.io/en/latest/start.html)
- [ ] [Endless Pagination](http://django-endless-pagination.readthedocs.io/en/latest/index.html)
- [X] [Material Design](https://github.com/viewflow/django-material)
- [ ] uWSGI and Nginx as web server
- [x] Account Access Level
- [x] Secure Website ([Beyond Security](http://www.beyondsecurity.com/vulnerability-scanner-verification/ssujan1.pythonanywhere.com))

### Getting Started

1. Project requirements:
  * Python3 - install it from [here](https://www.python.org/downloads/)

2. Clone this repo: 
  * `git clone https://github.com/sujan-sube/django-blog.git`
  
3. Install Virutal Environment: 
  * `cd django-blog`
  * `python -m venv myvenv` 
  * (if you have trouble with this check out this [link](http://tutorial.djangogirls.org/en/django_installation/#virtual-environment))
  
4. Activate Virtual Environment:
  * For **Windows**: `myvenv\scripts\activate`
  * For **Linux/Mac**: `source myvenv/bin/activate`
  
5. Install Packages:
  * `pip install -r requirements.txt`
  
6. Run DB Migrations:
  * `python manage.py migrate`
  
7. Run Django Dev Server:
  * `python manage.py runserver`

  
If you have any questions or would like to get in contact with me, send me an email at ssujan1@hotmail.com.
