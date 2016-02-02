from flask import render_template
from flask.views import View


class AdminView(View):

    coin_machine = None

    def dispatch_request(self):
        users = "Test"
        return render_template('admin.html', money=self.coin_machine.money)