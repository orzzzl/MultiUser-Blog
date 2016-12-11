from base_handler import BaseHandler
from database.blogs import Post
from database.users import User


class FrontHandler(BaseHandler):
    def get(self, username):
        try:
            user = User.by_name(username)
            user_id = str(user.key().id())
            posts = Post.all_post_by_user(user_id)
            self.render('front.html', posts = posts, username = self.user.name if hasattr(self.user, 'name') else None,
                        blogname = user.blog_name
                        )
        except:
            self.redirect('/login')