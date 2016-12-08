from google.appengine.ext import db
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    uid = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    @classmethod
    def create_post(cls, subject, content, uid):
        return  Post(parent=blog_key(), subject = subject, content = content, uid = uid)

    @classmethod
    def get_post(cls, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        return post

    @classmethod
    def all_post_by_user(cls, userid):
        posts = db.GqlQuery("select * from Post WHERE uid = :u order by created desc" , u=userid)
        return posts

    @classmethod
    def exe_gql(cls, cmd):
        posts = db.GqlQuery(cmd)
        return posts

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)