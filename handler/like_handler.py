from base_handler import BaseHandler
from database.likes import Like


class LikeHandler(BaseHandler):
    def post(self, pid):
        existed = Like.check_liked(self.user.name, pid)
        if not existed:
            l = Like.create_like(self.user.name, int(pid))
            l.put()
        self.redirect(self.request.referer)
