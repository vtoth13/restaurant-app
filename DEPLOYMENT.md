# Deployment Guide

This guide provides detailed instructions for deploying the **Restaurant App** using three different methods: **Local Deployment**, **Heroku**, and **Render**.

## Table of Contents
- [Local Deployment](#local-deployment)
- [Heroku Deployment](#heroku-deployment)
- [Render Deployment](#render-deployment)

## Local Deployment

Here's a step-by-step guide to deploying and running the Restaurant App locally on your machine.

### Prerequisites
- Python 3.8+
- Virtual Environment (venv)
- Node.js (for additional front-end requirements)
- Git
- MySQL database server

### Steps

1. **Clone the Repository**
   ```sh
   git clone https://github.com/vtoth13/restaurant-app.git
   cd restaurant-app
   ```

2. **Create and activate a Virtual Environment**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**
   ```sh
   pip install -r requirements.txt
   npm install  # If there’s a package.json for front-end dependencies
   ```

4. **Set up the MySQL database**
   ```sql
   CREATE DATABASE restaurant_app;
   CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON restaurant_app.* TO 'appuser'@'localhost';
   ```

5. **Configure the `.env` file with database settings**
   ```env
   DJANGO_SETTINGS_MODULE=booking.settings
   ...
   DATABASE_URL=mysql://appuser:password@localhost/restaurant_app
   ```

6. **Apply the database migrations**
   ```sh
   python manage.py migrate
   ```

7. **Create a superuser to access the Django admin**
   ```sh
   python manage.py createsuperuser
   ```

8. **Run the Django development server**
   ```sh
   python manage.py runserver
   ```

### Access the Application
- Visit `http://127.0.0.1:8000` in your web browser to see the application.
- Access the admin interface at `http://127.0.0.1:8000/admin` and log in with the superuser credentials.

## Heroku Deployment

Heroku makes it easy to deploy and manage scalable applications. Follow these steps to deploy the Restaurant App on Heroku.

### Prerequisites
- Heroku CLI installed
- GitHub Account (optional)

### Steps

1. **Log in to Heroku**
   ```sh
   heroku login
   ```

2. **Create a new Heroku app**
   ```sh
   heroku create restaurant-app
   ```

3. **Push the code to the Heroku remote repository**
   ```sh
   git push heroku main
   ```

4. **Add environment variables on Heroku**
   ```sh
   heroku config:set DJANGO_SETTINGS_MODULE=booking.settings
   heroku config:set DATABASE_URL=mysql://appuser:password@localhost/restaurant_app
   ```

5. **Scale the dynos on Heroku**
   ```sh
   heroku ps:scale web=1
   ```

6. **Run migrations on Heroku**
   ```sh
   heroku run python manage.py migrate
   ```

7. **Create a superuser on Heroku**
   ```sh
   heroku run python manage.py createsuperuser
   ```

### Access the Application
- Visit the URL provided by Heroku after deployment.

## Render Deployment

Render offers a straightforward way to deploy web applications with automatic HTTPS.

### Prerequisites
- Render account
- GitHub repository connected

### Steps

1. **Create a new Web Service on Render**
   - Go to your Render dashboard.
   - Click on "New" then "Web Service".
   - Connect your GitHub repository and select the restaurant-app.

2. **Configure the Environment**
   - Add environment variables in "Environment" settings:
     ```env
     DJANGO_SETTINGS_MODULE=booking.settings
     DATABASE_URL=mysql://appuser:password@localhost/restaurant_app
     ```

3. **Set build and start commands**
   - **Build Command**: `pip install -r requirements.txt && npm install && npm run build`
   - **Start Command**: `python manage.py runserver 0.0.0.0:8000`

4. **Deploy the App**
   - Click "Create Web Service" and Render will automatically build and deploy your app.

5. **Run migrations on Render**
   - In the Render service dashboard, go to the Shell and run:
     ```sh
     python manage.py migrate
     ```

6. **Create a superuser on Render**
   - In the Render service dashboard, use the Shell to create a superuser:
     ```sh
     python manage.py createsuperuser
     ```

### Access the Application
- Visit the URL provided by Render after deployment.

