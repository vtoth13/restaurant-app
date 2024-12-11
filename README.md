# Restaurant App - README

## Introduction

Welcome to the DineScheduler - Restaurant App! This application is designed to streamline restaurant reservations and menu management. It provides a user-friendly interface for customers to book tables and browse the menu, while also offering administrative functionalities for restaurant staff to manage bookings and tables efficiently.

## User Stories
**First-Time Visitor Goals**
| Issue ID | User Story |
|----------|------------|
|[#1](https://github.com/vtoth13/restaurant-app/issues/1) | As a first-time user, I want to see a clear and inviting homepage with all the necessary information about the restaurant, so that I can decide whether I want to dine there. |
|[#2](https://github.com/vtoth13/restaurant-app/issues/2) | As a first-time user, I want to view a menu that shows the tables and how many people each table can seat, so that I can understand the restaurant's seating arrangements. |
|[#3](https://github.com/vtoth13/restaurant-app/issues/3) | As a first-time user, I want to browse through the restaurant's food and drink menu, so I can see what items are available before making a booking. |
|[#4](https://github.com/vtoth13/restaurant-app/issues/4) | As a first-time user, I want to create an account, so I can make a booking and manage my reservations. |
|[#5](https://github.com/vtoth13/restaurant-app/issues/5) | As a first-time user, I want to make a new booking, so I can reserve a table for my preferred date and time. |

**Frequent User Goals**

| Issue ID | User Story |
|----------|------------|
|[#6](https://github.com/vtoth13/restaurant-app/issues/6)|As a frequent user, I want to log in to my account quickly, so I can access my booking information and make new reservations.|
|[#7](https://github.com/vtoth13/restaurant-app/issues/7)|As a frequent user, I want to view my existing bookings, so I can check the details of my reservations and make any necessary changes.|
|[#8](https://github.com/vtoth13/restaurant-app/issues/8)|As a frequent user, I want to create a new booking easily, so I can reserve a table for another visit without much hassle.|
|[#9](https://github.com/vtoth13/restaurant-app/issues/9)|As a frequent user, I want to browse the menu regularly to check for new items, so I can try different dishes each time I visit.|

**Restaurant Owner Goals**

| Issue ID | User Story |
|----------|------------|
|[#10](https://github.com/vtoth13/restaurant-app/issues/10)|As the restaurant owner, I want my staff to have their own login, so they can manage tables and bookings without interfering with customer accounts.|
|[#11](https://github.com/vtoth13/restaurant-app/issues/11)|As the restaurant owner, I want my staff to view all existing tables and their seating capacities, so they can manage reservations efficiently.|
|[#12](https://github.com/vtoth13/restaurant-app/issues/12)|As the restaurant owner, I want my staff to be able to create new tables and edit existing ones, so they can optimize the restaurant's seating arrangements.|
|[#13](https://github.com/vtoth13/restaurant-app/issues/13)|As the restaurant owner, I want my staff to view all bookings, so they can manage reservations and ensure a smooth operation.|
|[#14](https://github.com/vtoth13/restaurant-app/issues/14)|As the restaurant owner, I want my staff to edit the food and drink menu, so we can update the items offered based on availability and new offerings.|
|[#15](https://github.com/vtoth13/restaurant-app/issues/15)|As the restaurant owner, I want my staff to add new items to the menu, so we can keep the menu fresh and exciting for customers.|
|[#16](https://github.com/vtoth13/restaurant-app/issues/16)|As a restaurant owner, I want my staff to be able to make bookings in the past, so that we can accurately record and manage big events and reservations that occurred before the implementation of this system.|
|[#17](https://github.com/vtoth13/restaurant-app/issues/17)|As a restaurant owner, I want my staff to be able to make bookings for special events outside of regular working hours, so that we can accommodate customer requests for special events at any time of day or night.|

## Features

- **Table Management**: View available tables and their seating capacities.
- **Menu Management**: Browse the restaurant's menu with detailed descriptions and images.
- **Booking System**: Create, view, and cancel table bookings.
- **User Authentication**: Sign up, log in, and manage bookings as an authenticated user.
- **Admin Panel**: Access administrative features for managing tables and bookings.

## Usage

### Customer

1. **Browse Menu**: Navigate to the menu section to view available dishes.
2. **Book a Table**: Select an available table and specify booking details such as time and number of guests.
3. **View Bookings**: Check your current bookings and cancel if necessary.

### Admin

1. **Manage Tables**: Add, update, or remove tables from the system.
2. **View All Bookings**: Access a comprehensive list of all customer bookings.
3. **Update Menu**: Add or update menu items, including descriptions and images.

## Technology Stack

#### 1. **Framework: Django**
   - **Version:** 4.2.13
   - **Usage:** Django is the primary web framework in use. It handles the MVC (Model-View-Controller) paradigm, routing, ORM (Object Relational Mapping), and templating.
   - **Configuration Files:** 
     - `settings.py`: Stores configuration like database settings, installed apps, middleware, static and media files settings【4:0†source】【4:5†source】.
     - `urls.py`: Defines URL routing for the app.
     - `wsgi.py` and `asgi.py`: Configurations for WSGI and ASGI, enabling the Django app to handle web server requests【4:4†source】.

#### 2. **Database: SQLite**
   - **Usage:** Used as the default database for the app.
   - **Configuration File:** `settings.py` specifies SQLite as the database backend with default settings【4:5†source】.

#### 3. **Frontend Technologies: HTML, CSS, JavaScript**
   - **Templating Engine:** Django Templates
     - **Files:** Templates are stored in the `templates` directory. Example templates include `menu.html`, `signup.html`, and more.

#### 4. **Forms and Input Handling**
   - **Django Forms:** Used to manage user inputs efficiently.
     - **Files:** `forms.py` bridges communication between HTML forms and Django's ORM【4:4†source】.

#### 5. **Admin Interface**
   - **Django Admin:** Provides a robust administrative interface.
     - **Configurations:** Defined in `admin.py`. Customizations for displaying models in the admin interface are present for models such as `Table`, `MenuItem`, and `Booking`.
  
#### 6. **User Authentication**
   - **Django Auth:** Default user authentication system.
     - **Implementations:** User management is defined in `accounts` app files (e.g., `urls.py`, `views.py`).

#### 7. **Static Files and Media**
   - **Library:** Pillow
   - **Usage:** Handling image uploads for menu items.
   - **Configuration:** Paths and file handling are defined in `settings.py`【4:5†source】 and model definitions include image fields.
  
#### 8. **Middlewares**
   - **Security and Sessions:** Includes middleware for security and session handling.
   - **Files:** Defined in `settings.py` under the `MIDDLEWARE` section【4:5†source】.

#### 9. **JavaScript Libraries: jQuery**
   - **Usage:** Utilized for dynamic form handling and interactions in the Django admin interface.
   - **Files:** Custom scripts for formset and other dynamic functionalities.

#### 10. **Additional Python Packages**
   - **Packages:** The project depends on several additional Python libraries:
     - `django-crispy-forms` for enhanced form rendering.
     - `django-filter` for data filtering in views.
     - `django-widget-tweaks` for form widget customization.
     - **Dependency File:** Referenced in `requirements.txt`.

### Requirements

Here is a list of key packages and their versions used in the project:

| Package                 | Version   |
|-------------------------|-----------|
| Django                  | 4.2.13    |
| django-crispy-forms     | 1.11.2    |
| django-filter           | 2.4.0     |
| django-widget-tweaks    | 1.4.8     |
| mysqlclient             | 2.0.3     |
| Pillow                  | 8.3.1     |
| python-decouple         | 3.4       |
| pytz                    | 2021.3    |
| sqlparse                | 0.4.2     |

#### Notes:
- **MySQLclient** is listed in `requirements.txt`, indicating potential setup for MySQL if needed in production environments.
- **Python Decouple**: Used for managing configuration through environment variables, enhancing security and flexibility.

## Table of Contents for Design
1. [Introduction](#introduction)
2. [Font](#font)
3. [Color Scheme](#color-scheme)
4. [General Styles](#general-styles)
5. [Responsive Design](#responsive-design)
6. [Component Styles](#component-styles)
7. [Custom CSS](#custom-css)
8. [Theme Management](#theme-management)
9. [References](#references)

### Introduction
This document outlines the design components for the restaurant management system, including **font**, **color scheme**, and **general styles**. The goal is to ensure a visually appealing and consistent user interface for the restaurant management system.

### Font

##### Primary Font
The primary font used across the application is **Arial, sans-serif**. This choice provides clarity, readability, and a modern look that is fitting for a web-based application.

#### Font Styles
The font styles are defined as follows:
- **Body Text:** `font-family: Arial, sans-serif`
- **Font Size:**
  - Base size: `16px`
  - Headings: Scaled according to HTML heading tags (`<h1>` to `<h6>`)
- **Font Weights:**
  - Regular: `400`
  - Bold: `700`

#### Usage
The font styles are utilized throughout the application to ensure consistency:
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
}
```
Source: `3-restaurant-app-d9a4dff/templates/base.html` 

### Color Scheme

#### Primary Colors
The color scheme includes a set of primary colors to maintain a distinct visual identity:
- **Primary Color:** `#337ab7` (Bootstrap primary blue)
- **Secondary Color:** `#23527c`
- **Background Color:** `#f5f5f5`
- **Text Color:**
  - Default: `#333`
  - Inverse: `#ffffff`

#### Usage
The color scheme is applied to various UI elements, ensuring that the application is visually striking and cohesive:
```html
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f5f5f5;
    }
    .nav-bar {
        background-color: #333333;
        color: #ffffff;
        padding: 10px;
        text-align: center;
    }
    .nav-bar a {
        color: #ffffff;
    }
    .nav-bar a:hover {
        color: #cccccc;
    }
</style>
```
Source: `3-restaurant-app-d9a4dff/templates/base.html` 

### General Styles

#### Body
The body tag is styled to provide a consistent user experience:
```css
body {
    background-color: #f5f5f5;
    font-family: Arial, sans-serif;
}
```

#### Navigation Bar
The navigation bar is styled to be simple yet effective:
```css
.nav-bar {
    background-color: #333;
    color: #fff;
    padding: 10px;
    text-align: center;
}
.nav-bar a {
    color: #fff;
    text-decoration: none;
}
.nav-bar a:hover {
    color: #ccc;
}
```

### Responsive Design
The application employs responsive design principles to ensure usability across different devices.

#### Media Queries
Media queries are used to adapt the interface for various screen sizes:
```css
@media (max-width: 768px) {
    .nav-bar ul {
        flex-direction: column;
    }
    .card {
        margin-bottom: 20px;
    }
}
```

### Component Styles

#### Buttons
Buttons follow a consistent style to provide uniform action elements across the platform:
```css
button {
    font-size: 18px;
    background-color: #337ab7;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
button:hover {
    background-color: #23527c;
}
```
Source: `3-restaurant-app-d9a4dff/templates/signup.html` , `3-restaurant-app-d9a4dff/templates/menu.html` 

#### Forms
Form elements are designed to be user-friendly and visually consistent:
```css
.form-group {
    background-color: #f9f9f9;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
.form-group input[type="submit"] {
    background-color: #337ab7;
    color: #fff;
    border: none;
    border-radius: 10px;
    padding: 10px;
    cursor: pointer;
}
.form-group input[type="submit"]:hover {
    background-color: #23527c;
}
```
Source: `3-restaurant-app-d9a4dff/templates/signup.html` 

### Custom CSS
Custom styles are used to override or complement the default Bootstrap styles as needed to fit the specific design requirements of the application:
```html
<style>
    .main-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
    }
    .card {
        margin-bottom: 20px;
    }
    .card-img-top {
        height: 150px;
        object-fit: cover;
    }
</style>
```
Source: `3-restaurant-app-d9a4dff/templates/base.html` 

### Theme Management

#### Color Scheme Toggle
The application includes functionality for toggling between light and dark themes:
```javascript
'use strict';
window.addEventListener('load', function(e) {
    function setTheme(mode) {
        if (mode !== "light" && mode !== "dark" && mode !== "auto") {
            console.error(`Got invalid theme mode: ${mode}. Resetting to auto.`);
            mode = "auto";
        }
        document.documentElement.dataset.theme = mode;
        localStorage.setItem("theme", mode);
    }
    function cycleTheme() {
        // (Implementation of toggling logic)
    }
    function initTheme() {
        const currentTheme = localStorage.getItem("theme");
        currentTheme ? setTheme(currentTheme) : setTheme("auto");
    }
    function setupTheme() {
        const buttons = document.getElementsByClassName("theme-toggle");
        Array.from(buttons).forEach(btn => btn.addEventListener("click", cycleTheme));
        initTheme();
    }
    setupTheme();
});
```
Source: `3-restaurant-app-d9a4dff/staticfiles/admin/js/theme.js` 

### References
- Font Awesome Icons: http://fontawesome.io/ 
- Bootstrap 4 CDN: https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css 

## Information Architecture

### 1. Project Structure
The project is divided into several major sections to enhance maintainability and scalability:
- **Accounts:** Handles user authentication and authorization.
- **Main:** Contains the core functionality for managing tables, menu items, and bookings.
- **Staticfiles:** Stores static resources like CSS, JavaScript, and images.

### 2. Models

The primary models included in the `main` app are:
- **Table**
- **MenuItem**
- **Booking**

#### Table
Manages the restaurant's tables including their number, seating capacity, and availability status.

```python
from django.db import models

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table#{self.table_number} ({self.seats} seats)"
```

#### MenuItem
Represents the items available on the restaurant's menu, including name, description, price, and an image.

```python
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="menu")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
```

#### Booking
Manages customer bookings, linking users to tables and capturing booking details.

```python
from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    number_of_people = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.number_of_people} people at {self.booking_time}"
```

### 3. Forms

Django forms simplify the process of handling and validating user inputs. 

#### BookingForm
Used to create bookings with fields for the table, booking time, number of people, and special requests.

```python
import datetime
from django import forms
from .models import Booking, Table

class BookingForm(forms.ModelForm):
    table = forms.ModelChoiceField(queryset=Table.objects.filter(available=True))

    class Meta:
        model = Booking
        fields = ('table', 'booking_time', 'number_of_people', 'special_requests')

    booking_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'min': datetime.date.today().strftime('%Y-%m-%dT%H:%M'),
            'max': (datetime.date.today() + datetime.timedelta(days=90)).strftime('%Y-%m-%dT%H:%M')
        }),
    )

    number_of_people = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 1}),
    )

    special_requests = forms.CharField(label='Special Request', required=False, widget=forms.TextInput(attrs={'size': '60'}))
```

### 4. Views

The views in Django handle the logic for processing requests and returning responses.

#### Example: Booking Create View
Handles creating a booking, ensuring that only authenticated users can book a table.

```python
from .forms import BookingForm
from django.shortcuts import render, redirect
from .models import Table, Booking
from django.contrib.auth.decorators import login_required

@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            Table.objects.filter(id=booking.table.id).update(available=False)
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})
```

### 5. Admin Configuration

Django's admin interface is configured to manage the restaurant's tables, menu items, and bookings.

```python
from django.contrib import admin
from .models import Table, MenuItem, Booking

class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'seats', 'available')
    search_fields = ('table_number',)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'booking_time', 'number_of_people')
    search_fields = ('user__username', 'table__table_number')
    list_filter = ('booking_time',)

admin.site.register(Table, TableAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Booking, BookingAdmin)
```

### 6. URL Routing

Defines URL patterns and their corresponding views, allowing users to navigate between different pages.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tables/', views.table_list, name='table_list'),
    path('menu/', views.menu_list, name='menu_list'),
    path('booking/create/', views.booking_create, name='booking_create'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('check-table-availability/<int:table_id>/<int:number_of_people>/', views.check_table_availability, name='check_table_availability'),
]
```

### 7. Templates

Django templates are HTML files that can dynamically generate content using data passed from views.

#### Example: Booking Form Template

```html
{% extends 'base.html' %}
{% block content %}
  <div class="masthead">
    <h1>Create Booking</h1>
  </div>
  <div class="features">
    <div class="row justify-content-center">
      <div class="col-md-12">
        <div class="card mb-4">
          <div class="card-body">
            <form method="post">
              {% csrf_token %}
              {{ form.as_p }}
              <button type="submit" class="btn btn-primary btn-block">Create Booking</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
  <script>
    const dateTimeInput = document.getElementById('id_booking_time');
    dateTimeInput.addEventListener('input', (e) => {
      const dateTime = e.target.value;
      const dateParts = dateTime.split('T')[0].split('-');
      const timeParts = dateTime.split('T')[1].split(':');
      const hours = parseInt(timeParts[0]);
      const minutes = parseInt(timeParts[1]);
      const minTime = 10 * 60;
      const maxTime = 22 * 60;
      const currentTime = hours * 60 + minutes;
      if (currentTime < minTime || currentTime > maxTime) {
        alert('Please select a time between 10:00 AM and 10:00 PM');
        e.target.value = '';
      }
    });

    const tableSelect = document.getElementById('id_table');
    const numberOfPeopleInput = document.getElementById('id_number_of_people');
    tableSelect.addEventListener('change', checkTableAvailability);
    numberOfPeopleInput.addEventListener('input', checkTableAvailability);

    function checkTableAvailability() {
      const tableId = tableSelect.value;
      const numberOfPeople = numberOfPeopleInput.value;
      if (tableId && numberOfPeople) {
        fetch(`/check-table-availability/${tableId}/${numberOfPeople}`)
          .then(response => response.json())
          .then(data => {
            if (data.is_available) {
              numberOfPeopleInput.setCustomValidity('');
            } else {
              numberOfPeopleInput.setCustomValidity('The selected table does not have enough seats for the number of people.');
            }
          })
          .catch(error => console.error(error));
      }
    }
  </script>
{% endblock %}
```

### 8. Static Files

Static resources like CSS, JavaScript, and images are stored in the `staticfiles` directory to be served by Django's static file management.

## Testing

Please refer to the [TESTING.md](TESTING.md) file for all test-related documentation.

### Fix: Securing the `SECRET_KEY` with `python-decouple`

Initially, the `SECRET_KEY` was stored in the `settings.py` file, which posed a security risk as this file could be checked into version control systems like Git. To mitigate this risk and manage the `SECRET_KEY` securely, I removed it from `settings.py` and used the `python-decouple` package along with environment variables.

#### Solution

I followed the secure approach recommended, which involves specifying the key-value pair in the **Environment Variables** section (e.g., in the Render.com Environment Variables panel).

##### Steps Taken

1. The `SECRET_KEY` was removed from the `settings.py` file.
2. In **Render.com**, the `SECRET_KEY` was added as an environment variable.
3. The `python-decouple` package was used to read the `SECRET_KEY` from the environment variable, making it easier to manage and secure sensitive data.

##### Code Example

In the `settings.py`, I added the following to use `python-decouple`:
```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

## Deployment


- The app was deployed to [Render](https://render.com/).

- The app can be reached by the [link](https://restaurant-app-eh0v.onrender.com).

Please refer to the [DEPLOYMENT.md](DEPLOYMENT.md) file for all deployment-related documentation.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/vtoth13/restaurant-app.git
    cd restaurant-app
    ```

2. **Create a Virtual Environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up the Database**:
    - Ensure MySQL is installed and running.
    - Create a database for the project.
    - Configure the database settings in `booking/settings.py`.

5. **Apply Migrations**:
    ```sh
    python manage.py migrate
    ```

6. **Create a Superuser**:
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the Server**:
    ```sh
    python manage.py runserver
    ```

## Configuration

### Database Configuration

Update the `DATABASES` section in `booking/settings.py` to reflect your database settings:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
    }
}
```

### Static and Media Files

Configure the static and media file settings in `booking/settings.py`:
```python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## Contributing

We welcome contributions to the Restaurant App! To contribute, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button on the repository's GitHub page.

2. **Clone Your Fork**:
    ```sh
    git clone https://github.com/your-username/restaurant-app.git
    cd restaurant-app
    ```

3. **Create a Branch**:
    ```sh
    git checkout -b feature/your-feature
    ```

4. **Make Your Changes**: Implement your feature or bug fix.

5. **Commit Your Changes**:
    ```sh
    git add .
    git commit -m "Add feature: your feature description"
    ```

6. **Push to Your Fork**:
    ```sh
    git push origin feature/your-feature
    ```

7. **Open a Pull Request**: Go to the original repository and open a pull request with a description of your changes.

## Credits

We gratefully acknowledge the following resources and services that have contributed to the development and deployment of our restaurant management system:

- **[GitHub](https://github.com/)** for their excellent repository hosting service which facilitated the version control and collaborative development of our project.
- **[Django](https://www.djangoproject.com/)** for providing a high-level Python web framework that allowed rapid and pragmatic design of our application.
- **[Render](https://render.com/)** for offering a robust and free hosting service, making the deployment of our website seamless and efficient【4:9†source】.
- **[ElephantSQL](https://www.elephantsql.com/)** for their reliable free PostgreSQL database hosting, ensuring our database management is both powerful and easy to use【4:9†source】.
- **[BGJar](https://www.bgjar.com/)** for providing free access to beautiful and customizable SVG background images, enhancing the visual appeal of our website【4:8†source】.
- **[Font Awesome](https://fontawesome.com/)** for their comprehensive set of vector icons and social logos which have been instrumental in creating an engaging user interface【4:8†source】.

## Additional Acknowledgments

### Framework and Libraries

- **Django Crispy Forms**: The Django Crispy Forms library made handling and customizing forms in Django more intuitive and flexible.
- **Django Filter**: Simplified the implementation of sophisticated filtration functionalities in our views.
- **Django Widget Tweaks**: Facilitated the customization and optimization of Django form fields.
- **Pillow**: Essential for handling image processing capabilities within our application.
- **Python Decouple**: Enhanced the management of environment configurations, crucial for separating settings from our source code.
- **PyTZ**: Provided a robust time zone management solution.

### Development Tools

- **Visual Studio Code**: An indispensable tool for coding, offering powerful extensions and integrations that streamlined our development workflow.
- **Postman**: Played a critical role in API development by allowing us to test our endpoints effectively.
- **Git**: This version control system was pivotal in facilitating collaborative development across our team.
- **Docker**: Simplified the creation of containerized environments, ensuring consistency across development, testing, and production stages.

### Hosting and Deployment

- **Heroku**: Provided an alternate platform for quick and easy deployments during development.
- **Gitpod**: Greatly improved our development efficiency by offering a ready-to-code dev environment directly in the browser.

### Design and UI/UX

- **Bootstrap**: The extensive library of front-end components greatly accelerated the styling and responsive design of our application.
- **Canva**: Assisted in creating engaging graphical content for both the application and promotional materials.

### Testing and Quality Assurance

- **Selenium**: Enabled automated browser testing, ensuring our web application performed correctly across different browsers.
- **PyTest**: This testing framework facilitated the creation of simple yet scalable test cases for our application.

## Conclusion

Each of these tools and services played a vital role in bringing our restaurant management system to life. Our heartfelt thanks to all the developers and communities behind these incredible resources❤️. Without their contributions, the development of this project would not have been as efficient and enjoyable.

---

This documentation was generated based on the source code and supporting tools listed. The project is built using the **Django** framework and other tools/libraries that complement it, ensuring a robust and scalable application environment【4:9†source】【4:10†source】.

# Acknowledgments

I would like to express my gratitude to the following individuals for their support and contributions to this project:

- **My Fiancée**: I am deeply thankful to my fiancée for her invaluable insights and patience in helping me better understand certain concepts related to this project. Her support and encouragement have been instrumental in overcoming challenges and making progress.

- **Team Lead**: I appreciate my team lead for granting me the opportunity to take a day off from work to dedicate time to this project. Their understanding and flexibility have enabled me to focus on delivering the best possible outcome.

These acknowledgments would not be complete without mentioning the support of my friends and colleagues who have provided encouragement and feedback throughout this journey.
