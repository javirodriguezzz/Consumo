import webapp2
from webapp2_extras import jinja2


class DoHandler(webapp2.RequestHandler):
    def post(self):
        km = self.request.get("edKm", "ERROR")  # Identificador dentro del form, si no ERROR por defecto
        tiempo = self.request.get("edTiempo", "ERROR")
        consumo_medio = self.request.get("edConMedio", "ERROR")
        jinja = jinja2.get_jinja2(app=self.app)
        velocidad_media = 0
        consumo_total = 0

        if float(tiempo) is not 0:
            velocidad_media = float(km) / float(tiempo)
            consumo_total = (velocidad_media * float(consumo_medio))/100

        sust = {
            "velocidad_media": velocidad_media,
            "consumo_total": consumo_total
        }
        self.response.write(jinja.render_template("respuesta.html", **sust))


app = webapp2.WSGIApplication([
    ('/do', DoHandler)
], debug=True)