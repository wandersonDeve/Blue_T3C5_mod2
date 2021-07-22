# Instalar o Flask: pip install Flask

# Importa o flask, render template, o request e o redirect pro nosso projeto
from flask import Flask, render_template, request, redirect

# render_template: "abre" um arquivo html
# request: recebe e envia requisições do python para o html
# redirect: redireciona a página para uma rota especifica

app = Flask(__name__) # Cria uma instância da class Flask
itens = list() # Cria uma lista para os itens

@app.route('/') # Rota original
def index(): # Função da rota (toda rota precisa de uma função)
   return render_template('index.html', titulo='TO DO LIST', itens=itens) # Retorno da função que renderiza a página index.html e manda as variáveis titulo e itens para a página

# Rota para criar um novo item, a rota recebe os métodos POST e GET
@app.route('/new', methods=['POST', 'GET'])
def new(): # Função da rota new
   if request.method == 'POST': # Se o método da requisição for POST faça:
      # Pega o input que possui o name='item' e coloca na var item
      item = request.form['item'] 
      # Adiciona o item pego do form e adiciona na lista itens.
      itens.append(item)
      # Retorna para a rota principal que irá renderizar a página index.html
      return redirect('/') 

# Rota para limpar toda a lista
@app.route('/clear')
def clear(): # Função da rota clear
   itens.clear() # Limpa toda a lista itens
    # Retorna para a rota principal que irá renderizar a página index.html
   return redirect('/')

# Se o código estiver no arquivo principal.
if __name__ == '__main__':
   app.run(debug=True) # Roda nosso app Flask em modo debug
