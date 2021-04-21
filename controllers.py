import responder

api = responder.API()

class IndexController:
    async def on_get(self, req, resp):
        resp.html = api.template('Home.html')

class CreateController:
    async def on_get(self, req, resp, hogehoge):
        #something
        pass