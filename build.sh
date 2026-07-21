#!/usr/bin/env bash

# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Create a regular test user if it does not exist
python manage.py shell <<'PYTHON'
import os

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("TEST_USER_USERNAME")
email = os.environ.get("TEST_USER_EMAIL", "")
password = os.environ.get("TEST_USER_PASSWORD")

if not username or not password:
    print("Test user was not created: TEST_USER_USERNAME or TEST_USER_PASSWORD is missing.")
else:
    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            "email": email,
            "is_staff": False,
            "is_superuser": False,
        },
    )

    if created:
        user.set_password(password)
        user.save()

        print(f"Test user '{username}' was created.")
    else:
        print(f"Test user '{username}' already exists.")
PYTHON
