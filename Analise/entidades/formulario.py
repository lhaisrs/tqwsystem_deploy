class Formulario(object):
	nome = None
	descricao = None
	membro = None
	constructos = []

	def __init__(self, nome, descricao, membro, constructos):
		self.nome = nome
		self.descricao = descricao
		self.membro = membro
                #self.membroNome  = membro.nome
                #self.membroCargo = membro.cargo
		self.constructos = constructos
