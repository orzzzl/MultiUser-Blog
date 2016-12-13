from base_handler import BaseHandler
from database.users import User


class Explore(BaseHandler):
    def get(self):
        all_users = User.get_all()
        self.render("explore.html", all_users=all_users)
