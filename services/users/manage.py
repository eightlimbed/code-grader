# Configures the flask CLI tool

from flask.cli import FlaskGroup
from project import app, db

cli = FlaskGroup(app)

# Create a cli command for recreating the db
@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()
