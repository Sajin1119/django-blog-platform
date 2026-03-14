
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


python manage.py shell -c "
from faker import Faker
from users.models import User
from posts.models import Post, Category
import random

fake = Faker()

# Create 2 users
for u in [('alex_writer','alex@test.com'), ('maya_blogs','maya@test.com')]:
    user, _ = User.objects.get_or_create(username=u[0], defaults={'email':u[1]})
    user.set_password('Test@1234')
    user.save()

all_users = list(User.objects.all())

tech_categories = ['Technology','AI','Web Development','Cybersecurity','Cloud Computing']
categories = []
for name in tech_categories:
    cat, _ = Category.objects.get_or_create(name=name, defaults={'slug':name.lower().replace(' ','-')})
    categories.append(cat)

tech_topics = ['The Future of AI','Why Python Dominates','Understanding Cloud','React vs Vue','Cybersecurity Basics','Machine Learning','Docker and Kubernetes','Edge Computing','Web3 Basics','Building REST APIs']

for i in range(50):
    title = f'{random.choice(tech_topics)} Part {i+1}'
    Post.objects.get_or_create(title=title, defaults={'content':chr(10).join(fake.paragraphs(nb=6)),'author':random.choice(all_users),'category':random.choice(categories),'is_published':True})

print('Done!')
"