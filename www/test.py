import orm
from models import User, Blog, Comment
def test(loop):
    yield from orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root',database='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()
for x in test():
    pass