from fakesite import database, app
from fakesite.models import Usuario, Foto

with app.app_context():

    database.create_all()