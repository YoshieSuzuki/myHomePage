from controllers import api
import controllers

api.add_route('/', controllers.IndexController)
api.add_route('/Home.html', controllers.IndexController)

api.add_route('/specialthanks.html', controllers.SpecialThanksController)