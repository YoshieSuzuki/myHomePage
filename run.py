import responder

api = responder.API()

@api.route("/")
def home_html(req, resp):
    resp.content = api.template('Home.html')

if __name__ == '__main__':
    api.run()