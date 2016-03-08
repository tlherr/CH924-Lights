from flask import render_template, request
from flask.views import MethodView


class AdminView(MethodView):
    coin_machine = None
    light_manager = None

    def get(self):
        return render_template('admin.html', coin_machine=self.coin_machine, light_manager=self.light_manager)

    def post(self):
        error = None
        price_per_hour = request.form.get('price_per_hour_input')
        if price_per_hour is not None:
            try:
                price = float(price_per_hour)
                self.coin_machine.set_price_per_hour(price)
            except ValueError:
                error = "Invalid Value"

        return render_template('admin.html', coin_machine=self.coin_machine, light_manager=self.light_manager,
                               error=error)
