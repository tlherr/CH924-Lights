from flask import render_template, request, jsonify
from flask.views import MethodView
import time
import json


class RESTView(MethodView):
    coin_machine = None
    light_manager = None

    def get(self):
        time_activated = time.ctime(int(self.light_manager.activation_time))
        time_expires = time.ctime(int(self.light_manager.expiration_time))
        return jsonify(money=self.coin_machine.money,
                       price_per_hour=self.coin_machine.price_per_hour,
                       locked=self.coin_machine.is_locked,
                       override=self.light_manager.override,
                       time_remaining=self.light_manager.time_remaining/60,
                       time_activated=str(time_activated),
                       time_expires=str(time_expires))

    def post(self):
        light_override = request.form.get('light_override')
        if light_override is not None:
            override = False
            if light_override == "1":
                override = True

            self.light_manager.set_override(override)

        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
