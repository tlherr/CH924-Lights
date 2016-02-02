from flask import render_template
from flask.views import View


class AdminView(View):

    coin_machine = None

    def dispatch_request(self):
        return render_template('admin.html', coin_machine=self.coin_machine)