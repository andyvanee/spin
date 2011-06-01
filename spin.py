import couchdb, json, sys
import tornado.ioloop
import tornado.web

from lib.couch import db

class BaseHandler(tornado.web.RequestHandler):
  def get_current_user(self):
    return self.get_secure_cookie("user")

class Login(BaseHandler):
  def get(self):
    self.write('<html><body><form action="/spin/login" method="post">'
         'Name: <input type="text" name="name">'
         '<input type="submit" value="Sign in">'
         '</form></body></html>')

  def post(self):
    username = self.get_argument("name")
    users = db.get("users")
    if users.has_key(username):
      self.set_secure_cookie("user", username)
      self.redirect("/spin/")
    else:
      self.write("Authentication failed")
      return

class Spin(BaseHandler):
  def get(self):
    username = self.get_current_user()
    if not self.current_user:
      self.redirect("/spin/login")
      return
    doc = db.get("default")
    doc_text = doc.pop("text")
    self.render("templates/form.html", 
      title="Spin",
      content=doc_text,
      id=doc.id,
      rev=doc.rev,
      username = username
    )

  def post(self):
    if not self.get_current_user:
      self.redirect("/spin/login")
      return
    id = self.get_argument("id")
    rev = self.get_argument("rev")
    content = self.get_argument("content")
    
    db.save({'_id': id, '_rev': rev, 'text': content})
    self.redirect('/spin/')
    #self.files
    #self.path
    #self.headers

class Default(tornado.web.RequestHandler):
  def get(self):
    self.write("hello...")

application = tornado.web.Application([
  (r"/", Default),
  (r"/spin/", Spin),
  (r"/spin/login", Login),
], cookie_secret="61oETzYXQAGbYdkL5gEmGeJPFuYh7EAnp2XdTP1o/Vo=")

if __name__ == "__main__":
  port=3000
  arg = int(sys.argv[1])
  if arg:
    if 1023 < arg < 49152:
      port = arg
  application.listen(port)
  tornado.ioloop.IOLoop.instance().start()