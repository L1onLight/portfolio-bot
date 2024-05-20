import csv
import os
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

from config import abs_path


class Base(DeclarativeBase):
    pass


class Repository(Base):
    __tablename__ = "repositories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(255))
    technologies: Mapped[str] = mapped_column(String(255))
    url: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"Repository(id={self.id!r}, name={self.name!r})"

    def dict(self):
        return {"name": self.name,
                "description": self.description,
                "technologies": self.technologies,
                "url": self.url}

    def get_repo_info(self):
        text = f"""
<strong>Name</strong>: {self.name}\n
<strong>Description</strong>: {self.description}\n
<strong>Technologies</strong>: {self.technologies}\n
<strong>Github</strong>: <a href="{self.url}">Link</a>
    """
        return text


engine = create_engine(f"sqlite:///{os.path.join(abs_path, "data", "portfolio.db")}")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def create_fixtures():
    repos_csv = os.path.join(abs_path, "data/repositories.csv")
    with open(repos_csv, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        repos = []
        for row in reader:
            repos.append(Repository(**row))

    session.bulk_save_objects(repos)
    print("All repos created")
    session.commit()


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

if not session.query(Repository).all():
    create_fixtures()
