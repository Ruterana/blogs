from flask import render_template,request,redirect,url_for,abort
from ..models import User,Blog,Comment,Quote,Subscription
from . import main
from ..request import get_quote
from .forms import blogForm,CommentForm,UpdateBlogForm,SubscriptionForm
from .. import db,photos
from flask_login import login_required,current_user
from  ..email import mail_message


@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    form=SubscriptionForm()
    if form.validate_on_submit():
       name = form.name.data
       email= form.email.data
       new_subscriber=Subscription(name=name,email=email)
    #    mail_message("Thank you for subscribing","email/welcome_user",new_subscriber.email,new_subscriber=new_subscriber)
       db.session.add(new_subscriber)
       db.session.commit()
       
       return redirect(url_for('main.index'))
    quote=get_quote()
    blogs = Blog.query.all()
    title = 'Welcome to blog app'
    
    return render_template('index.html', title = title,blogs=blogs,quote=quote, subscription_form=form)

@main.route('/blog/new',methods=['GET','POST'])
@login_required
def new_blog():
    form= blogForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        
        new_blog =Blog(user_id =current_user._get_current_object().id, title = title,description=description)
        db.session.add(new_blog)
        db.session.commit()
        return redirect (url_for('main.index'))
    return render_template('blog.html',blog_form=form)
#   return render_template('comment.html',form=form,blogs=blogs)

@main.route('/comment/<int:id>', methods=['GET','POST'])
def comment(id):

    form = CommentForm()
    blog = Blog.query.filter_by(id=id).first()
    user=User.query.filter_by(id=id).first()

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment = comment,blog_id=blog.id)
        new_comment.save_comments()
    
        # return redirect(url_for('.comment'))
    return render_template('comment.html',comment_form = form)

@main.route('/index/<int:id>/delete', methods = ['GET','POST'])
@login_required
def delete(id):
    current_post = Blog.query.filter_by(id = id).first()

    if current_post.user != current_user:
        abort(404)
    db.session.delete(current_post)
    db.session.commit()
    return redirect(url_for('.index'))

@main.route('/delete/blog/<int:id>', methods = ['GET','POST'])
@login_required
def delete_blog(id):

    blog = Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()
        # blog.delete_comment()
    
    return redirect(url_for('.index'))
    
@main.route('/blog/<int:id>', methods = ['GET','POST'])    
def view_comment(id):
    
    # blog = Blog.query.filter_by(id=id).first()
    comments =Comment.get_comments(id=id)
    return render_template('view.html',comments=comments)
@main.route('/update/blog/<int:id>',methods= ['GET','POST'])
@login_required
def update_blog(id):
 blog=Blog.query.filter_by(id=id).first()
 if blog is None:
      abort(404)
 form=UpdateBlogForm()
 if form.validate_on_submit():
       blog.title=form.title.data
       blog.description=form.description.data
       db.session.add(blog)
       db.session.commit()
       return redirect(url_for('main.index'))
 return render_template('update_blog.html',form=form)


