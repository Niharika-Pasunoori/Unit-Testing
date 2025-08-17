from testing_project.settings import *

MAINTENANCE_MODE=False


# To run all the test files, when site is under maintenance   python manage.py test --settings=testing_project.test_settings   

PASSWORD_HASHERS=[
    "django.contrib.auth.hashers.MD5PasswordHasher"
]

# To run tests with tag python manage.py test --settings=testing_project.test_settings --tag=auth