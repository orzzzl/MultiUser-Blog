from base_handler import BaseHandler
from database.blogs import Post

class Permalink(BaseHandler):
    def get(self, pst):
        post = Post.get_post(pst)

        if not post:
            self.error(404)
            return

        self.render("permalink.html", post=post)