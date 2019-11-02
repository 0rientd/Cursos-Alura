from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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
    return render_template('novo.html', titulo="Novo jogo")

@app.route('/criar', methods=['POST'],)
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    jogo = Cria_Jogo(nome, categoria)

    jogos.append(jogo)

    return redirect('/')

app.run(debug=True)