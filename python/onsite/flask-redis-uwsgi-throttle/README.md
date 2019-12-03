# Flask app served by uWSGI

Tasks:

1. Create a simple flask app, with no validation, that just accepts a
   `POST` on `/user` with the json payload: `{"email":"foo", "password": "bar"}` and stores that in a redis instance running on
   `localhost:6379`.

2. You will be given console access to a machine pointing to
   `https://ingress.dev.newstore.com/`. Configure nginx and uwsgi
   manually. Install any packages that you need, including redis.
