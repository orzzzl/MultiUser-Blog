from google.appengine.ext import db

def users_key(group = 'default'):
    return db.Key.from_path('users', group)

class User(db.Model):
    name = db.StringProperty(required = True)
    pw = db.StringProperty(required = True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid, parent = users_key())

    @classmethod
    def by_name(cls, name):
        u = User.all().filter('name =', name).get()
        return u

    @classmethod
    def register(cls, name, pw, email = None):
        return User(parent = users_key(),
                    name = name,
                    pw = pw,
                    email = email)

    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and pw == u.pw:
            return u

