from flask.views import View
from flask import render_template, redirect


class AdminView(View):

    def dispatch_request(self):
        # templates located in templates directory by default
        return render_template('admin.html')