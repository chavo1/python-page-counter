#!/usr/bin/env python3

import time
import redis
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")
cache = redis.Redis(host='localhost', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/', methods=["GET", "POST"])
def hit():
    count = get_hit_count()
    if request.method == "POST":
        return render_template("index.html", count=' (%i) \n' % int(count))
    if request.method == "GET":
        cache = redis.Redis(host='localhost', port=6379)
        cache.get('hits')
        cache.delete('hits')
        return render_template("index.html", count='(0)')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
