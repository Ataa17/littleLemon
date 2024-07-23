# Django Project

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Admin Panel](#admin-panel)

## Introduction

This is a Django project designed for a restaurant booking system. It includes  menu management endpoints,an admin panel and authentication endpoints for user management.


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ataa17/littlelemon.git
   cd project
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

## Running the Project

To run the project, use the following command:

```bash
python manage.py runserver
```

## API Endpoints
- **Menu**
  - `/restaurant/menu`
  - `/restaurant/menu/<int:pk>`

- **booking**
  - `/restaurant/booking/tables`
  - `/restaurant/booking/tables/<int:pk>`

- **User List:**
  - `/auth/users/`

- **User Activation:**
  - `/auth/users/activation/`

- **Current User:**
  - `/auth/users/me/`

- **Resend Activation:**
  - `/auth/users/resend_activation/`

- **Reset Password:**
  - `/auth/users/reset_password/`
  - `/auth/users/reset_password_confirm/`

- **Reset Username:**
  - `/auth/users/reset_username/`
  - `/auth/users/reset_username_confirm/`

- **Set Password:**
  - `/auth/users/set_password/`

- **Set Username:**
  - `/auth/users/set_username/`

- **User Detail:**
  - `/auth/users/<username>/`

- **API Root:**
  - `/auth/`

- **Token Authentication:**
  - `/auth/token/login/`
  - `/auth/token/logout/`

## Admin Panel

To access the admin panel, navigate to:

```
/admin/
```

Use the superuser credentials created during the installation process to log in.