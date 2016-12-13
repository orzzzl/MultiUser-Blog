from base_handler import BaseHandler
from database.blogs import Post

class Edit(BaseHandler):
    def get(self, pst):
        post = Post.get_post(pst)
        if self.user:
            self.render("edit.html", subject=post.subject, content=post.content, pst=pst)
        else:
            self.redirect('/login')

    def post(self, pst):
        if self.user:
            subject = self.request.get('subject')
            content = self.request.get('content')
            pst = self.request.get('post_id')
            if subject and content:
                p = Post.get_post(pst)
                p.subject = subject
                p.content = content
                p.put()
                self.redirect('/permalink/%s' % str(p.key().id()))
            else:
                error = "subject and content, please!"
                self.render("edit.html", subject=subject, content=content, pst=pst, error=error)
        else:
            self.redirect('login')
