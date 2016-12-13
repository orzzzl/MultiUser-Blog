from base_handler import BaseHandler
from database.blogs import Post


class Delete(BaseHandler):
    def get(self, pst):
        post = Post.get_post(pst)
        if self.user:
            self.render("delete.html", subject=post.subject, content=post.content, pst=pst,
                        blogname=self.user.blog_name)
        else:
            self.redirect('/login')

    def post(self, pst):
        try:
            pst = self.request.get('post_id')
            p = Post.get_post(pst)
            p.delete()
            self.redirect('/front/' + str(self.user.name))
        except:
            self.redirect('login')
