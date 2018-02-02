from flask import Flask, render_template, request, redirect

aplicacao_web = Flask(__name__)

class Jogo:
	def __init__(self, nome, categoria, console):
		self.nome = nome
		self.categoria = categoria
		self.console = console

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNES')
lista = [jogo1, jogo2, jogo3]


@aplicacao_web.route('/')
def ola():
	return render_template('lista.html', jogos=lista, titulo="Jogos")

@aplicacao_web.route('/novo')
def form():
	return render_template('novo.html', titulo='Novo Jogo')

@aplicacao_web.route('/salvar', methods=['POST'])
def salvar():
	nome = request.form['nome']
	categoria = request.form['categoria']
	console = request.form['console']
	jogo = Jogo(nome, categoria, console)
	lista.append(jogo)
	return redirect('/')

@aplicacao_web.route('/login')
def login():
	return render_template('login.html')

@aplicacao_web.route('/autenticar')
def autanticar():
	if 'mestra' == request.form['senha']
		return redirect('')

aplicacao_web.run(debug=True)
