from datetime import datetime, timedelta
from app import app, db
from app.models import User, Post


# create four users
u1 = User(username='john', email='john@example.com')
u1.set_password('123456')
u2 = User(username='susan', email='susan@example.com')
u2.set_password('123456')
u3 = User(username='mary', email='mary@example.com')
u3.set_password('123456')
u4 = User(username='david', email='david@example.com')
u4.set_password('123456')
u5 = User(username='ivanir', email='efi.ivanir@gmail.com')
u5.set_password('123456')
db.session.add_all([u1, u2, u3, u4,u5])

# create four posts
now = datetime.utcnow()
p1 = Post(body="post from john", author=u1,
          timestamp=now + timedelta(seconds=1))
p2 = Post(body="post from susan", author=u2,
          timestamp=now + timedelta(seconds=4))
p3 = Post(body="post from mary", author=u3,
          timestamp=now + timedelta(seconds=3))
p4 = Post(body="post from david", author=u4,
          timestamp=now + timedelta(seconds=2))
db.session.add_all([p1, p2, p3, p4])
db.session.commit()

# setup the followers
u1.follow(u2)  # john follows susan
u1.follow(u4)  # john follows david
u2.follow(u3)  # susan follows mary
u3.follow(u4)  # mary follows david
db.session.commit()

# check the followed posts of each user
f1 = u1.followed_posts().all()
f2 = u2.followed_posts().all()
f3 = u3.followed_posts().all()
f4 = u4.followed_posts().all()
