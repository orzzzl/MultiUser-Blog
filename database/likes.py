from google.appengine.ext import db


def like_key(name='default'):
    return db.Key.from_path('likes', name)


class Like(db.Model):
    """
    The database store information about who like which article
    """
    user = db.StringProperty(required=True)
    pid = db.IntegerProperty(required=True)

    @classmethod
    def create_like(cls, user, pid):
        return Like(user=user, pid=pid)

    @classmethod
    def get_by_user_and_pid(cls, username, pid):
        res = db.GqlQuery("select * from Like WHERE user = :u and pid = :p", u=username, p=int(pid))
        return res

    @classmethod
    def get_by_pid(cls, pid):
        res = db.GqlQuery("select * from Like WHERE pid = %d" % int(pid))
        return res


    @classmethod
    def check_liked(cls, username, pid):
        query_res = Like.get_by_user_and_pid(username, pid)
        existed = False
        for _ in query_res:
            existed = True
            break
        return existed