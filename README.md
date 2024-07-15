# Restaurant App - README

## Introduction

Welcome to the Restaurant App! This application is designed to streamline restaurant reservations and menu management. It provides a user-friendly interface for customers to book tables and browse the menu, while also offering administrative functionalities for restaurant staff to manage bookings and tables efficiently.

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

