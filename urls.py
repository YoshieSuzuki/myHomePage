from controllers import api
from controllers import IndexController, CreateController

api.add_route('/', IndexController)

api.add_route('/create/{hogehoge}', CreateController)