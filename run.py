import responder

api = responder.API()

@api.route("/")
def home_html(req, resp):
    resp.text = "hello world"

if __name__ == '__main__':
    api.run()