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

if __name__ == '__main__':
    cli()
