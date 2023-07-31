#!/bin/bash

gunicorn main:app --reload --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
uvicorn main:app --reload --host 0.0.0.0 --port 8000