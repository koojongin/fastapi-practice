# from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String

from db.base_class import Base


# if TYPE_CHECKING:

class Post(Base):
    id = Column(Integer, index=True)
    title = Column(String)
    content = Column(String)
