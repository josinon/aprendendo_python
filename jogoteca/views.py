from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from dao import JogoDao, UsuarioDao
from model import Usuario, Jogo
import time
from app import aplicacao_web, db
from helpers import deleta_arquivo, recupera_imagem

jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)


@aplicacao_web.route('/')
def index():
	return render_template('lista.html', jogos=jogo_dao.listar(), titulo="Jogos")

@aplicacao_web.route('/novo')
def novo():
	if 'usuario_logado' not in session:
		return redirect(url_for('login', proxima=url_for('novo')))
	return render_template('novo.html', titulo='Novo Jogo')

@aplicacao_web.route('/salvar', methods=['POST'])
def salvar():
	nome = request.form['nome']
	categoria = request.form['categoria']
	console = request.form['console']
	jogo = Jogo(nome, categoria, console)
	if (request.form.get('id')):
		jogo.id = request.form['id']
	jogo = jogo_dao.salvar(jogo)

	arquivo = request.files['arquivo']
	upload_path = aplicacao_web.config['UPLOAD_PATH']
	timestamp = time.time()
	deleta_arquivo(jogo.id)
	arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')
	flash('O jogo foi salvo com sucesso!! ')
	return redirect(url_for('index'))

@aplicacao_web.route('/editar/<int:id>')
def editar(id):
	if 'usuario_logado' not in session:
		return redirect(url_for('login', proxima=url_for('editar')))
	jogo = jogo_dao.busca_por_id(id)
	capa=recupera_imagem(id)
	return render_template('editar.html', titulo='Editar Jogo' , jogo=jogo, capa_jogo=capa)

@aplicacao_web.route('/atualizar', methods=['POST'])
def atualizar():
	return salvar()

@aplicacao_web.route('/deletar/<int:id>')
def deletar(id):
	if 'usuario_logado' not in session:
		return redirect(url_for('login', proxima=url_for('deletar', id=id)))
	jogo = jogo_dao.deletar(id)
	flash('O jogo foi removido com sucesso!! ')
	return redirect(url_for('index'))

@aplicacao_web.route('/login')
def login():
	proxima = request.args.get('proxima')
	return render_template('login.html', proxima=proxima)

@aplicacao_web.route('/autenticar', methods=["POST"])
def autenticar():
	login = request.form['usuario']
	senha = request.form['senha']

	usuario = usuario_dao.buscar_por_id(login)
	if usuario.senha == senha:
		session['usuario_logado'] = usuario.id
		flash(usuario.nome +' logou com sucesso.')
		proxima_pagina = request.form['proxima']
		return redirect(proxima_pagina)
	else:
		flash('Erro de autenticação. Tente novamente.')
		return redirect(url_for('login'))

@aplicacao_web.route('/logout')
def logout():
	session['usuario_logado'] = None
	flash('Logout realizado com sucesso.')
	return redirect(url_for('login'))


@aplicacao_web.route('/imagem/<capa>')
def imagem(capa=None):
	return send_from_directory('uploads', capa)

