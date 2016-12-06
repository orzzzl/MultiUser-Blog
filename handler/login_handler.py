from base_handler import BaseHandler
from database.users import User


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/front')
        else:
            msg = 'Invalid login'
            self.render('login.html', error = msg)