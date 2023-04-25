#!/usr/bin/env sh

export FLASK_APP=app/routes.py
export FLASK_ENV=development

flask run

#Terminal command: sh run_local.sh