from base_handler import BaseHandler

class MainPage(BaseHandler):
    def get(self):
        if self.user:
            self.redirect('/front')
        else:
            self.redirect('/login')