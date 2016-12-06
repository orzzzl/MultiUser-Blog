from base_handler import BaseHandler
from database.blogs import Post

class NewPostHandler(BaseHandler):
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect('/login')

    def post(self):
        if self.user:
            subject = self.request.get('subject')
            content = self.request.get('content')
            if subject and content:
                p = Post.create_post(subject, content)
                p.put()
                self.redirect('/permalink/%s' % str(p.key().id()))
            else:
                error = "subject and content, please!"
                self.render("newpost.html", subject=subject, content=content, error=error)
        else:
            self.redirect('login')
