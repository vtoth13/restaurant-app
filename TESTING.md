# Testing

---

## Overview

This document provides detailed insights into the **Testing** aspect of the Restaurant Application built using the **Django Framework**. It includes information on setting up and running various tests, best practices, and the different types of tests implemented for ensuring the application works as expected.

---

## Table of Contents

1. [Environment Setup](#environment-setup)
2. [Running Tests](#running-tests)
3. [Writing Tests](#writing-tests)
    - [Unit Tests](#unit-tests)
    - [Integration Tests](#integration-tests)
    - [Functional Tests](#functional-tests)
4. [Test Coverage](#test-coverage)
5. [Best Practices](#best-practices)

---

## Environment Setup

Before running the tests, ensure your environment is properly set up. The following packages are required:

### Dependencies for Testing:

```plaintext
Django==4.2.13
django-crispy-forms==1.11.2
django-filter==2.4.0
django-widget-tweaks==1.4.8
mysqlclient==2.0.3
Pillow==8.3.1
python-decouple==3.4
pytz==2021.3
sqlparse==0.4.2
```

Install these dependencies using `pip`:

```sh
pip install -r requirements.txt
```

## Running Tests

To run the tests, use Django’s built-in test management command. Simply navigate to your project’s main directory and execute:

```sh
python manage.py test
```

Tests will be executed, and the results will be displayed in the terminal.

## Writing Tests

### Unit Tests

*Unit Tests* are the simplest and fastest types of tests. They focus on the smallest pieces of code, like individual functions or methods, ensuring they work correctly in isolation.

**Location:**
- Unit tests for models and views can be found in `main/tests.py`.

**Example:**

```python
from django.test import TestCase
from django.contrib.auth.models import User
from main.models import Table, Booking

class TableModelTestCase(TestCase):
    def setUp(self):
        self.table = Table.objects.create(table_number=1, seats=4, available=True)

    def test_table_creation(self):
        self.assertEqual(self.table.table_number, 1)
        self.assertEqual(self.table.seats, 4)
        self.assertTrue(self.table.available)
```

### Integration Tests

*Integration Tests* check the interaction between multiple components such as views, forms, and models together to ensure they work cohesively.

**Example:**

```python
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Table, Booking

class BookingIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.table = Table.objects.create(table_number=1, seats=4)

    def test_booking_create_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('booking_create'), {
            'table': self.table.id,
            'booking_time': '2024-06-27T12:00',
            'number_of_people': 4
        })
        self.assertEqual(response.status_code, 302)  # Redirects after booking creation
        self.assertTrue(Booking.objects.filter(user=self.user).exists())
```

### Functional Tests

*Functional Tests* ensure the complete functionality of the application, typically involving more complex interactions that simulate the real-world use case.

**Example**:

```python
from django.test import TestCase, Client

class UserSignupTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_signup(self):
        response = self.client.post('/accounts/signup/', {
            'username': 'newuser',
            'password1': 'complexpassword',
            'password2': 'complexpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
```

## Test Coverage

To ensure that the tests cover all parts of your code base, it’s crucial to use tools like `coverage.py`.

### Steps to Run Coverage:

1. **Install Coverage**:
    ```sh
    pip install coverage
    ```

2. **Run Tests with Coverage**:
    ```sh
    coverage run --source='.' manage.py test
    ```

3. **Generate Coverage Report**:
    ```sh
    coverage report -m
    ```

This will display a coverage report and highlight the parts of the code that are not covered by tests.

## Best Practices

1. **Isolate Tests**: Each test should be independent and should not rely on the state of another test.
2. **Use Fixtures**: Use Django’s fixtures or `setUp` method to create test data instead of modifying the database directly in tests.
3. **Clean Up**: Ensure each test cleans up after itself by removing any test data created.
4. **Descriptive Names**: Name your test methods and classes descriptively to reflect what they're testing.
5. **Continuous Integration**: Integrate testing into the CI/CD pipeline to ensure that all tests are run on every commit.