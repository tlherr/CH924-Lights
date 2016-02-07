from flask import render_template
from flask.views import MethodView


class AdminView(MethodView):
    coin_machine = None

    def get(self):
        return render_template('admin.html', coin_machine=self.coin_machine)

    def post(self):
        override = (bool)(request.form['light_override'])
        print override