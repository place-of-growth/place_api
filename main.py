import json
import os

from flask import Flask, request, send_file
from flask_cors import CORS
from models import db_session
import random
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from sqlalchemy.orm import class_mapper

from models.user import User
from models.events import Events

from urllib.parse import urlparse, parse_qs

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'
app.config['JSON_AS_ASCII'] = False

db_session.global_init()


def to_dict(model):
    columns = class_mapper(model.__class__).columns
    return dict((c.name, getattr(model, c.name)) for c in columns)


# @app.route('/auth', methods=['POST'])  # Авторизация
# def auth():
#     try:
#         if request.method == 'POST':
#             db_sess = db_session.create_session()
#             user = db_sess.query(User).filter(User.mail == request.form.get('login'),
#                                               User.password == request.form.get('password')).all()
#             if len(user) != 0:
#                 db_sess.close()
#                 return json.dumps({'status': 'ok', 'user': {'id': str(user[0].id),
#                                                             'name': str(user[0].name),
#                                                             'mail': str(user[0].mail),
#                                                             'phone': str(user[0].phone),
#                                                             'login': str(user[0].login),
#                                                             'password': str(user[0].password)}})
#             else:
#                 db_sess.close()
#                 return json.dumps({'status': 'error'})
#     except Exception as error:
#         return json.dumps({'status': 'error'})
#
#
# @app.route('/registration', methods=['POST'])  # Регистрация
# def reg():
#     try:
#         if request.method == 'POST':
#             db_sess = db_session.create_session()
#             new_user = User(name=request.form.get('name'), mail=request.form.get('mail'),
#                             phone=request.form.get('phone'), login=request.form.get('login'),
#                             password=request.form.get('password'))
#             db_sess.add(new_user)
#             db_sess.commit()
#             db_sess.refresh(new_user)
#             db_sess.close()
#             print(new_user.id)
#             return json.dumps({'status': 'ok', 'user': {'id': str(new_user.id),
#                                                         'name': str(new_user.name),
#                                                         'mail': str(new_user.mail),
#                                                         'phone': str(new_user.phone),
#                                                         'login': str(new_user.login),
#                                                         'password': str(new_user.password)}})
#     except Exception as error:
#         return json.dumps({'status': 'error'})


@app.route('/get_photo_events', methods=['GET'])  # Метод получения фото мероприятий
def get_photo_events():
    data = parse_qs(urlparse(request.url).query)
    return send_file('assets/events/' + data.get('image')[0])


@app.route('/get_events', methods=['POST'])  # Метод для получения информации о мероприятиях
def get_events():
    try:
        if request.method == 'POST':
            db_sess = db_session.create_session()
            events = db_sess.query(Events).all()
            db_sess.close()
            return json.dumps({'status': 'ok', 'events': [to_dict(result) for result in events]})
    except Exception as error:
        return json.dumps({'status': 'error'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)
