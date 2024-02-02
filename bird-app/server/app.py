import os
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Bird

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgresql://bird_app_e0ow_user:96hUDUjq7HdbgIYv4JCqN8hWOb99K4jj@dpg-cmue3qev3ddc738had30-a.oregon-postgres.render.com/bird_app_e0ow')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json_compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class  Birds(Resource):

    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)
        #return {'birds': [b.serialize() for b in Bird.query.all()]}

api.add_resource(Birds, '/birds')        

