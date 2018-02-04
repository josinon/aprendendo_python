from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory

from flask_mysqldb import MySQL

aplicacao_web = Flask(__name__)
aplicacao_web.config.from_pyfile('config.py')

db = MySQL(aplicacao_web)


from views import *
if (__name__) == '__main__':
	aplicacao_web.run(debug=True)
