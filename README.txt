This is my first Tornado app.
I've pulled the guts out of my webpy_couch app and re-implemented
it with Tornado. I'll probably just tinker away at this...

ATM it's set up pretty static. Copy couch.py.dist to couch.py and add
a db and username/password to work with.

In the couch db there should be at least {"users": {"username": "password"}}
and {"default": {"text":""}}

Run with ` python spin.py 3000 ` (on port 3000)
or, run as a daemon ` python spin.py 3000 > log.txt 2>&1 & `

