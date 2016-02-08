from flask import render_template, request, jsonify
from flask.views import MethodView
import json


class RESTView(MethodView):
    coin_machine = None
    light_manager = None

    def get(self):
       return jsonify(money=self.coin_machine.money,
                      price_per_hour=self.coin_machine.price_per_hour,
                      time_remaining=self.light_manager.time_remaining)

    def post(self):
        light_override = request.form.get('light_override')
        if light_override is not None:
            override = False
            if light_override == "1":
                override = True

            self.light_manager.set_override(override)

        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}