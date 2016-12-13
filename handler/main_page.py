from base_handler import BaseHandler


class MainPage(BaseHandler):
    def get(self):
        if self.user:
            self.redirect('/front/' + str(self.user.name))
        else:
            self.redirect('/login')
