from flask import Flask,render_template,url_for,redirect
app = Flask(__name__)

post=[
   {
      
      'author':'corey schafer',
      'title':'blog post 1',
      'content':'first post content',
      'date_posted':'april 20,2025'
   },
   {
      
      'author':'raga',
      'title':'blog post 2',
      'content':'post content',
      'date_posted':'april 20'
   }
]

@app.route('/')
def home():
   return render_template('home.html',post=post)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/admin')
def hello_admin():
   return 'hello admin'

@app.route('/user/<name>')
def user(name):
   if name=="admin":
      return redirect(url_for("hello_admin"))
   else:
      return redirect(url_for("hello_admin",name=name))
   
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run(debug = True)