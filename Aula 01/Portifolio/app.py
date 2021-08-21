from flask import Flask, render_template, request, redirect, flash, session
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'wanderson'


mail_setting = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT":465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "testeflask2021@gmail.com",
    "MAIL_PASSWORD": "lavoisier50331"
}

app.config.update(mail_setting)

mail = Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ctaxltmp:NcUYAQX-fgee6gkXEv8CsjthPW37m5zG@kesavan.db.elephantsql.com/ctaxltmp'
db = SQLAlchemy(app)

class Contato():
    def __init__(self,nome,email,mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem


class Projeto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    imagem = db.Column(db.String(300), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(200), nullable=False)
    

    def __init__(self,nome,imagem,descricao,link):
        self.nome = nome
        self.imagem = imagem
        self.descricao = descricao
        self.link = link

@app.route('/')
def index():
    session['user_logado'] = None
    return render_template('index.html')

@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        contato = Contato(
            request.form['nome'],
            request.form['email'],
            request.form['mensagem']
        )
        
        msg = Message(
            subject='Contato do portifolio',         
            sender=app.config.get('MAIL_USERNAME'),
            recipients=[app.config.get('MAIL_USERNAME')],
            body= f'''
                O {contato.nome} com o email {contato.email} enviou a seguinte mensagem

                {contato.mensagem}
            '''
        )
        mail.send(msg)
    return render_template('send.html', contato=contato)

@app.route('/adm')
def adm():
    if 'user_logado' not in session or session['user_logado'] == None:
        flash('Faça o login para acessar a sessao')
        return redirect('/login')

    projetos = Projeto.query.all()
    return render_template('adm.html', projetos=projetos, projeto='')

@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        projeto = Projeto(
            request.form['nome'],
            request.form['imagem'],
            request.form['descricao'],
            request.form['link']
        )
        db.session.add(projeto)
        db.session.commit()
        flash('Projeto adicionado com sucesso')
        return redirect('/adm')

@app.route('/delete/<id>')
def delete(id):
    if 'user_logado' not in session or session['user_logado'] == None:
        flash('Faça o login para acessar a sessao')
    projetos = Projeto.query.get(id)
    db.session.delete(projetos)
    db.session.commit()
    flash('Projeto apagado com sucesso')
    return redirect('/adm')

@app.route('/edit/<id>',methods=['POST', 'GET'])
def edit(id):
    if 'user_logado' not in session or session['user_logado'] == None:
        flash('Faça o login para acessar a sessao')
    projeto = Projeto.query.get(id)
    projetoDel = Projeto.query.all()
    if request.method == 'POST':
        projetoDel.nome = request.form['nome']
        projetoDel.descricao = request.form['descricao']
        projetoDel.imagem = request.form['imagem']
        projetoDel.link = request.form['link']
        db.session.commit()
        return redirect('/adm')
    return render_template('adm.html', projetoDel=projetoDel, projeto='')
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST', 'GET'])
def auth():
    if request.form['senha'] == 'admin':
        session['user_logado'] = 'logado'
        flash('Login successful')
        return redirect('/adm')
    else:
        flash('login failed')
        return redirect('/login')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
