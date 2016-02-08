from flask import render_template, request
from flask.views import MethodView
import json


class AdminView(MethodView):
    coin_machine = None
    light_manager = None

    def get(self):
        return render_template('admin.html', coin_machine=self.coin_machine, light_manager = self.light_manager)

    def post(self):
        light_override = request.form.get('light_override')
        if light_override== "0":
            override = False
        elif light_override== "1":
            override = True

        self.light_manager.set_override(override)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}