from base_handler import BaseHandler
from database.blogs import Post
from database.users import User

class NewPostHandler(BaseHandler):
    def get(self):
        if self.user:
            self.render("newpost.html", blogname=self.user.blog_name)
        else:
            self.redirect('/login')

    def post(self):
        if self.user:
            subject = self.request.get('subject')
            content = self.request.get('content')
            uid = self.read_secure_cookie('user_id')
            if subject and content:
                p = Post.create_post(subject, content, uid, self.user.name)
                p.put()
                self.redirect('/permalink/%s' % str(p.key().id()))
            else:
                error = "subject and content, please!"
                self.render("newpost.html", subject=subject, content=content, blogname=self.user.blog_name, error=error)
        else:
            self.redirect('login')
