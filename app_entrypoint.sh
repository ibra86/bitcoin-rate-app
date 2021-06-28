#!/usr/bin/env bash

exec gunicorn -b 0.0.0.0:80 --log-level debug wsgi:app
