from flask import Flask

app=Flask(__name__)

#Criando a pagina inicial
'''@app.route("/")
def homepage():
	return "Meu primeiro site,coisa lindaaa" '''
	
#Criando a pagina de contatos
@app.route("/")
def contatos():
	return "<p>Telefone:81 992624419</p> <p>Email:Orlandopaullo817@gmail.com</p> "





#Colocando o site no Ar
if __name__== "__main__":
	app.run()
