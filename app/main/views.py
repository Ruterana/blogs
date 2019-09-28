from flask import render_template,request,redirect,url_for,abort
from ..models import User,Blog,Comment
from . import main
from .forms import blogForm
from .. import db,photos
from flask_login import login_required,current_user
import markdown2 

@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    blog = Blog.query.all()
    title = 'Welcome to blog app'
    
    return render_template('index.html', title = title,blogs=blog)




   
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
@main.route('/comment/<int:id>/new',methods=['GET','POST'])
@login_required
def new_comment(id):
    form=commentForm()
    blog =Blog.query.filter_by(id=id).first()
    comments = comment.query.filter_by(id = id).all()
    if form.validate_on_submit():
        description = form.description.data
        id = id
        user_id = current_user ._get_current_object().id
        new_comment =Comment(user_id =current_user._get_current_object().id, title = title,description=description,blog=blog,comment=comment)
        new_comment.save_comments()
        db.session.add(new_comment)
        db.session.commit()
        return redirect (url_for('main.index'))
    return render_template('comment.html',form=form,blogs=blogs)
