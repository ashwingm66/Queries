import random

from django.contrib.auth.hashers import make_password
from django.utils.timezone import now
from faker import Factory
from blog.models import User, Article, Tag, Comments


fake = Factory.create()

#clean up database
Article.objects.all().delete()
Tag.objects.all().delete()
User.objects.all().delete()
Comments.objects.all().delete()

user_names = []
for i in range(1000):
    generated_name = fake.name()
    if generated_name not in user_names:
        user_names.append(generated_name)
    else:
        continue


for i in range(len(user_names)):
    name = user_names[i]
    email = ".".join(name.lower().split()) + "@xyz"
    is_Admin = True
    password = make_password("12345")
    user = User.objects.create(username=name, email=email, password=password, is_Admin=is_Admin)
    user.save()

my_tag = ['python','django','blog','documentation','models','faker','tags']

for tag in my_tag:
   # print(tag)
    tag_name = Tag.objects.create(tag_name=tag)
    tag_name.save()


users = User.objects.all()
tags = Tag.objects.all()

for user in users:
    tag = random.choice(tags)
    description = fake.sentence()
    time = now()
    [Article.objects.create(user=user,tag_name=tag,description=description,time=time).save() for i in range(250)]
articles = Article.objects.all()

for art in articles:
    user = random.choice(users)
    description = fake.sentence()
    time = now()
    [Comments.objects.create(user=user, article = art , description = description, time = time ).save() for i in range (4)]
