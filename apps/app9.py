from flask_jwt_extended import JWTManager
# 백엔드 시스템이 JWT 기능을 수행할 수 있도록 flask_jwt_extended를 사용
# JWTManager로 플라스크 어플리케이션 객체 넘겨주고 토큰 암호화할 때 사용할 SECRET_KEY 넘겨주면 됨.

from flask import Flask, render_template, jsonify

application = Flask(__name__, instance_relative_config=True)
application.config.update(
    DEBUG = True,
    JWT_SECRET_KEY = 'secret string',
)
# JWT 토큰을 생성하는데 필요한 고유의 시크릿 키 값 설정
jwt = JWTManager(application)
