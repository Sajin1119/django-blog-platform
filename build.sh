#!/usr/bin/env bash
pip install -r requirements.txt
pip install gunicorn
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "
from users.models import User
u, created = User.objects.get_or_create(username='sajin', defaults={'email':'sajin@test.com'})
u.is_staff = True
u.is_superuser = True
u.set_password('Sajin@1234')
u.save()
print('Superuser ready!')
"