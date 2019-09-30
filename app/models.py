from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    pass_secure = db.Column(db.String(255))
    email= db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String())
    blogs = db.relationship('Blog',backref = 'users',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'users',lazy="dynamic")

    @property
    def password(self):
         raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    @login_manager.user_loader
    def load_user(user_id):
       return User.query.get(int(user_id))

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    written_on = db.Column(db.DateTime,default=datetime.utcnow)
    title =db.Column(db.String(255))
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment_id =db.relationship("Comment",backref='blogs',lazy="dynamic")
    
    @classmethod
    def get_blogs(cls,id):
        blog = blog.query.all()
        # blog =Blog.query.filter_by(blog_id=blog_id).all()
        return Blog
    
    def delete(self, id):
        comments = Comment.query.filter_by(id = id).all()
        for comment in comments:
            db.session.delete(comment)
            db.session.commit()
        db.session.delete(self)
        db.session.commit()
    def __repr__(self):
        return f'Blog{self.description}'
    


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    # posted_on = db.Column(db.DateTime,default=datetime.utcnow)
    comment= db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    def save_comments(self):
        db.session.add(self)
        db.session.commit()
    def clear_comment(self):
        comment.comments.clear()
    @classmethod
    def get_comments(cls,id):
        comments =Comment.query.filter_by(blog_id=id).all()
        return comments

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit() 
       
    def __repr__(self):
        return f'Comment{self.comment}'
        
