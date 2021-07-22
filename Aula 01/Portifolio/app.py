from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
mail_setting = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT":465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "",
    "MAIL_PASSWORD": "",
}

app.config.update(mail_setting)

mail = Mail(app)

class Contato():
    def __init__(self,nome,email,mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

@app.route('/')
def index():
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

if __name__ == '__main__':
    app.run(debug=True)