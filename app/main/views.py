from flask import render_template,request,redirect,url_for,abort
from ..models import User,Blog,Comment
from . import main
from .forms import blogForm,CommentForm
from .. import db,photos
from flask_login import login_required,current_user
import markdown2 

@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    blogs = Blog.query.all()
    title = 'Welcome to blog app'
    
    return render_template('index.html', title = title,blogs=blogs)




   
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
        new_comment = Comment(comment = comment,blog_id=blog.id,user_id=user.id)
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

@main.route('/index/<int:id>/delete_comment', methods = ['GET','POST'])
@login_required
def delete_comment(id):

    current_post = Comment.query.filter_by(id = id).first()

    if current_post.user != user_user:
        abort(404)

    db.session.delete(current_post)
    db.session.commit()
    return redirect(url_for('.index'))
    return render_template('comment.html',current_post = current_post)
@main.route('/blog/<int:id>', methods = ['GET','POST'])    
def view_comment(id):
    
    # blog = Blog.query.filter_by(id=id).first()
    comments =Comment.get_comments(id=id)
    return render_template('view.html',comments=comments)
