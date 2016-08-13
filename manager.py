import pip
pip.main(['install', '-r', 'requirements.txt'])

import os
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from spending import app, db


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host="0.0.0.0"))


if __name__ == '__main__':
    manager.run()
