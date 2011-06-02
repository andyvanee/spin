This is my first Tornado app.

I've pulled the guts out of my webpy_couch app and re-implemented
it with Tornado. I'll probably just tinker away at this...

ATM it's set up pretty static. 

### Requirements:
- Python libraries: couchdb and Tornado
- CouchDB
- Copy couch.py.dist to couch.py and add a db and username/password to work with.
- In the couch db there should be at least {"users": {"username": "password"}} and {"default": {"text":""}}

### Bind mounting the static folder

I'm linking my static content folder into Nginx, while still keeping it under
version control with a bind mount like this:

file: /etc/fstab
    ...
    /srv/http/nginx/static/spin /srv/http/sites/spin/spin none bind
    ...

If you want Tornado to serve the styles/js, you'll have to fix the pathnames in the template.

Run it with:
    python spin.py 3000    #to run on port 3000
    python spin.py 3000 > log.txt 2>&1 &
