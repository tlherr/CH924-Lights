from flask import render_template
from flask.ext.classy import FlaskView


class ShowUsers(FlaskView):
    route_base = '/'

    def index(self):
        users = "Test"
        return render_template('admin.html', objects=users)