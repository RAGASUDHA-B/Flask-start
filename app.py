from flask import Flask,render_template,url_for,redirect
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/admin')
def hello_admin():
   return 'hello admin'

@app.route('/user/<name>')
def user(name):
   if name=="admin":
      return redirect(url_for("admin"))
   else:
      return redirect(url_for("admin"))
   
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run(debug = True)