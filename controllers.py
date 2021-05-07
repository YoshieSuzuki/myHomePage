import responder

api = responder.API()

class IndexController:
    async def on_get(self, req, resp):
        resp.html = api.template('Home.html')

class SpecialThanksController:
    async def on_get(self, req, resp):
        resp.html = api.template('specialthanks.html')