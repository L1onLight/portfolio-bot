from db import session, Repository


def fetch_repositories():
    return session.query(Repository).all()


def get_repo_by_name(name: str):
    return session.query(Repository).filter_by(name=name).first()
