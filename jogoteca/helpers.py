import os
from app import aplicacao_web

def recupera_imagem(id):
	for nome_arquivo in os.listdir(aplicacao_web.config['UPLOAD_PATH']):
		if f'capa{id}' in nome_arquivo:
			return nome_arquivo
	return 'capa_padrao.jpg'

def deleta_arquivo(id):
	for nome_arquivo in os.listdir(aplicacao_web.config['UPLOAD_PATH']):
		if f'capa{id}' in nome_arquivo:
			os.remove(aplicacao_web.config['UPLOAD_PATH']+'/'+nome_arquivo)

