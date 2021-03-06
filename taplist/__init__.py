from flask import Flask
from flask.ext.stormpath import StormpathManager
from flask.ext.cors import CORS

import os

app = Flask(__name__)
app.config.from_object('config.{0}'.format(os.getenv('APP_SETTINGS', 'Config')))
StormpathManager(app)
CORS(app)
if app.config['DEVEL']:
    app.debug=True

from taplist import views

app.add_url_rule('/<location>/entry', view_func=views.Entry.as_view('entry'), methods=['GET', 'POST', 'PUT'])
app.add_url_rule('/<location>/scroll', view_func=views.Scroll.as_view('scroll'), methods=['GET'])
app.add_url_rule('/<location>/json', view_func=views.Json.as_view('get_json'), methods=['GET'])
app.add_url_rule('/<location>/<beerid>', view_func=views.GetBeer.as_view('get_beer'), methods=['GET'])
app.add_url_rule('/<location>/edit', view_func=views.Edit.as_view('editlist'), methods=['GET', 'POST'])
app.add_url_rule('/<location>/', view_func=views.BarLists.as_view('bars'))
app.add_url_rule('/locations', view_func=views.Locations.as_view('locations'), methods=['GET'])
app.add_url_rule('/', view_func=views.Index.as_view('index'))
