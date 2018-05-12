Celery Periodic Tasks Demo
===

Usage
====
1. run demo1.py<br/>
`celery -A demo1 worker --beat --loglevel=debug --config=demo1`

2. run demo2.py<br/>
`celery -A demo2 worker --beat --loglevel=debug`

Installation
============
1. `git clone https://github.com/Wayde2014/celery-periodic-tasks-demo`<br/>
2. `pip install -r requirements.txt`<br/>