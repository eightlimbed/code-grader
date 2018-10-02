# Configures the flask CLI tool

from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User
import unittest

app = create_app()
cli = FlaskGroup(create_app=create_app)

# Create a cli command for recreating the db
@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

# Create a cli command for running unit tests
@cli.command()
def test():
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    if results.wasSuccessful():
        return 0
    return 1

# Create a seed to populate the database with some intial data
@cli.command()
def seed_db():
    '''Seeds the database.'''
    db.session.add(User(username='theo', email='theo@huxtable.com'))
    db.session.add(User(username='rudolph', email='red@hat.com'))
    db.session.commit()

if __name__ == '__main__':
    cli()
