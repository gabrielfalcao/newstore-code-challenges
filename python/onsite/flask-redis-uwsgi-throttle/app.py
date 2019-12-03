from flask import Flask
from flask import request, Response
import json
import redis

app = Flask(__name__)
conn = redis.Redis()


@app.route('/user', methods=['POST'])
def hello_world():
   new_user = request.get_json(silent=True)
   entries = conn.rpush('users', json.dumps(new_user))
   return Response(json.dumps({'created_user': new_user['username'], 'entries': entries}), status=200)
   

if __name__ == '__main__':
    app.run(debug=True)
