from base_handler import BaseHandler
from database.users import User
from database.blogs import Post


class Debug(BaseHandler):
    def get(self):
        posts = Post.exe_gql("select * from Post")
        self.write(posts)
