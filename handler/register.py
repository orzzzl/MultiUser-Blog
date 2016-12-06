from base_handler import BaseHandler
from tools.validators import *
from database.users import User

class RegisterHandler(BaseHandler):
    def get(self):
        self.render("register.html")

    def post(self):
        have_error = False

        self.username = self.request.get("username")
        self.password = self.request.get("password")
        self.email = self.request.get("email")
        self.verify = self.request.get("verify")

        params = dict(username = self.username,
                      email = self.email)

        if not valid_username(self.username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(self.password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif self.password != self.verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if self.email and (not valid_email(self.email)):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.render('register.html', **params)
        else:
            self.done()

    def done(self, *a, **kw):
        u = User.by_name(self.username)
        if u:
            msg = 'That user already exists.'
            self.render('register.html', error_username = msg)
        else:
            print self.password
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect('/front')