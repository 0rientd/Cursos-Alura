from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'alura'

class Cria_Jogo:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria

jogo1 = Cria_Jogo("Pomemon Gold", "RPG")
jogo2 = Cria_Jogo("Pomemon Silver", "RPG")
jogos = [jogo1, jogo2]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Inventário Holding', jogos=jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    
    return render_template('novo.html', titulo="Novo jogo")

@app.route('/criar', methods=['POST'],)
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    jogo = Cria_Jogo(nome, categoria)

    jogos.append(jogo)

    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'alura' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash('Usuário => ' + request.form['usuario'] + ' logou com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Não logado, tente novamente!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')
    

app.run(debug=True)