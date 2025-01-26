# User Registration with Email Verification

This Django project allows users to register with a custom password of their choice. The registration process includes a verification step where a random 4-digit pin is sent to the user's email address. The user must verify the pin to activate their account.

![Login](https://github.com/steve-ongera/Two_AUTH_APPLICATION/blob/main/screenshoots/Authapp_Login.PNG "Login page")

![Register](https://github.com/steve-ongera/Two_AUTH_APPLICATION/blob/main/screenshoots/Authapp_Register.PNG "Register page")


## Features
- User registration with username, email, and password.
- Password confirmation to ensure passwords match.
- A 4-digit verification code sent to the user's email for account activation.
- No password complexity enforcement (passwords of any format are accepted).

## Requirements
- Python 3.x
- Django 3.x or later
- An email provider (e.g., Gmail, SendGrid) to send the verification code

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/steve-ongera/Two_AUTH_APPLICATION.git
    cd project-name
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up your database:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

Now, navigate to `http://127.0.0.1:8000/` in your browser to access the application.

## Email Configuration
To send the 4-digit verification code, you need to configure email settings in your Django project. Add the following to your `settings.py` file:

```python
# Email settings for sending verification code
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Example: for Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'your-email-password'  # Your email password
