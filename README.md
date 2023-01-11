$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install Flask
(venv) $ python -m flask --version
$ export FLASK_APP=main.py
(venv) $ flask run

pm2 start main.py --name chain-data --interpreter=python3
pm2 start main.py --interpreter python3
