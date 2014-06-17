Example Django and Docker setup
===============================

I'm just playing around now.  Currently, this is a minimal Django installation
with Postgres.

How to run (with fig)
---------------------

This project uses fig to coordinate things, so the easy way to get up an
running is this::

    $ pip install fig
    $ fig up

This will turn on your db service and your django service.  Leave this running.
You also need to migrate your database, so you can do it like this::

    $ fig run web syncdb

How to run (without fig)
------------------------

If you don't want to use fig (for example, if you want to know what's going
on), here's the commands that I ran to get everything working.  This is a lot
more involved than the fig example, but I learned a ton doing it.

First run::

    $ docker build -t djangodocker_web .

This will build the web image.  Internally, the web image relies on the
``google/python`` image, but it also installs ``libpq-dev`` package so that we
can install psycopg2.  I originally wanted to use ``google/python-runtime``,
but I don't think it would be possible [#f1]_.

Next we want to get our database container up and running, we can run this::

    $ docker run --name postgres \
             -e USER=docker \
             -e PASS=docker \
             -e DB=docker \
             paintedfox/postgresql

.. note::

  I chose to use ``paintedfox/postgresql`` instead of the "official" ``postgres``
  from stackbrew image because the official one isn't marked as Trusted and also
  I would rather have Postgres installed from a package manager than compiled
  like the way that stackbrew creates their images.


After that we should probably migrate our database::

    $ docker run --rm -ti \
             --link postgres:db_1 \
             djangodocker_web \
             /env/bin/python syncdb

I called that using the ``--rm`` option because I don't want to keep littering
everything with all of these one-off containers.  I think that's correct.  The
``-ti`` options would be optional in a normal migration, but since the first
migration asks you if you want to create a superuser, you need to have those.
Now we can run our web container::

    $ docker run --rm \
             --link postgres:db_1 \
             -p 8000:8080 \
             djangodocker_web
    
This was cool and all, but then I tried to edit my settings file when I
realized that code inside the container wasn't being updated with my code.  So
I turned off the web service and rebuilt the image and restarted the web
service and then my new settings were in the code.  So I have to rebuild and
restart the server every time I change my code?  Turns out no.  Duh, obviously
not.  Using this whole thing would be a waste if I had to do that.  I just have
to mount my source code into the image, which Docker makes quite easy.::

    $ docker run --rm -t \
             --link postgres:db_1 \
             -p 8000:8080 \
             -v /abs/path/to/dir/:/app \
             djangodocker_web \
             /env/bin/uwsgi --python-autoreload --ini uwsgi.ini

Now whenever I change the code, the changes appear in the browser.


.. [#f1] Let's see what happens with this issue: <https://github.com/GoogleCloudPlatform/python-docker/issues/7>.
