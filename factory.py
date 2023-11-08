from flask import Flask

import settings
from blueprints.user import user_bp
# from extensions import db


def create_app():
    app = Flask(__name__)
    # TODO ��������
    app.config.from_object(settings.DevelopmentConfig)
    # TODO ע������
    app.register_blueprint(user_bp)
    # TODO ��ʼ������
    # db.init_app(app)

    return app
