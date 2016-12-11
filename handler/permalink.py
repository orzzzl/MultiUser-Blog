from base_handler import BaseHandler
from database.blogs import Post
from database.users import User

class Permalink(BaseHandler):
    def get(self, pst):
        try:
            post = Post.get_post(pst)
            user = User.by_name(post.author)
            self.render("permalink.html", post = post, username = self.user.name if hasattr(self.user, 'name') else None,
                         blogname = user.blog_name
                        )
        except:
            if not post:
                self.error(404)
                return