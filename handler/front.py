from base_handler import BaseHandler
from database.blogs import Post


class FrontHandler(BaseHandler):
    def get(self):
        posts = Post.all().order('-created')
        self.render('front.html', posts = posts)