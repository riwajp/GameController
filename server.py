# examples/joystick.py

# Let's get this party started!
from wsgiref.simple_server import make_server

import falcon
from keystrokes1 import press, pressKey, releaseKey


# Falcon follows the REST architectural style, meaning (among
# other joystick) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class Joystick:
    def on_get(self, req, resp):
        for i, j in req.params.items():
            press(j)
            break

        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('index.html', 'r') as f:
            resp.body = f.read()


class Buttons:
    def on_get(self, req, resp):
        for i, j in req.params.items():
            cmds = [k for k in j]
            if (cmds[0] == "p"):
                pressKey(cmds[1])
            else:
                releaseKey(cmds[1])

            break

        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('index.html', 'r') as f:
            resp.body = f.read()


# falcon.App instances are callable WSGI apps
# in larger applications the app is created in a separate file
app = falcon.App()

# Resources are represented by long-lived class instances
joystick = Joystick()
buttons = Buttons()


# joystick will handle all requests to the '/joystick' URL path
app.add_route('/joystick', joystick)
app.add_route("/buttons", buttons)


with make_server('', 8000, app) as httpd:
    print('Serving on port 8000...')

    # Serve until process is killed
    httpd.serve_forever()
