#!/bin/bash

python gen_catalog.py

git add .

git commit -m "new post on `date`"

git push
