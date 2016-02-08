from flask import render_template, request
from flask.views import MethodView
from decimal import Decimal
import json


class AdminView(MethodView):
    coin_machine = None
    light_manager = None

    def get(self):
        return render_template('admin.html', coin_machine=self.coin_machine, light_manager = self.light_manager)

    def post(self):
        status = 200

        light_override = request.form.get('light_override')
        if light_override is not None:
            override = False
            if light_override == "1":
                override = True

            self.light_manager.set_override(override)

        price_per_hour = request.form.get('price_per_hour')
        if price_per_hour is not None:
            try:
                price = Decimal(price_per_hour)
                self.coin_machine.set_price_per_hour(price)
            except ValueError:
                status = 500

        return json.dumps({'success':True}), status, {'ContentType':'application/json'}