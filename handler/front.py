from base_handler import BaseHandler
from database.blogs import Post


class FrontHandler(BaseHandler):
    def get(self):
        user_id = self.read_secure_cookie('user_id')
        print "!!!!!!!!!!!!!!!!!!!!!!!!!user_id =", user_id
        if user_id:
            posts = Post.all_post_by_user(user_id)
            self.render('front.html', posts = posts)
        else:
            self.redirect('/login')