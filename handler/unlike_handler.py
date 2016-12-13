from base_handler import BaseHandler
from database.likes import Like


class UnLikeHandler(BaseHandler):
    def post(self, pid):
        existed = Like.check_liked(self.user.name, pid)
        if existed:
            l = Like.get_by_user_and_pid(self.user.name, pid)
            for ele in l:
                ele.delete()
        self.write("34")
        self.redirect(self.request.referer)
