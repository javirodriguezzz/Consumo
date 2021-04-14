#!/usr/bin/env python
import webapp2
from webapp2_extras import jinja2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        plantilla = {

        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template(
            "index.html", **plantilla
        ))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
