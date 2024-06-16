from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import Relationship


from db_app.database import Base, SessionLocal
from table_post import Post
from table_user import User

class Feed(Base):
    __tablename__ = "feed_action"
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = Relationship(User)
    post_id = Column(Integer, ForeignKey("post.id"), primary_key=True)
    post = Relationship(Post)
    action = Column(String)
    time = Column(TIMESTAMP)


if __name__ == "__main__":
    lst = SessionLocal().query(Feed.user_id).limit(10).all()
    print([f.user_id for f in lst])
