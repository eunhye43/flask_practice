# from flask import Flask
# from api.index import bp as index_bp
# from api.board import bp as board_bp
# from model import initialize_db

from flask import Blueprint, render_template, request, redirect
from model import Database