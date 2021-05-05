from gpiozero import LED 
from flask import Flask, render_template
app = Flask(__name__)

luzSala = False
luzQuarto = False
portao = False

ledSala = LED(23)
ledQuarto = LED(24)
ledPortao = LED(25)

# Flask apresenta a página html 
@app.route('/')
def index():
    return render_template('index.html')

# Recursos do servidor 
@app.route('/evento/luz/<tipo>', methods=['POST'])
def luz(tipo):
    global luzSala
    global luzQuarto

    operacao = "ligada"
    if(tipo == "sala"):
        if(luzSala):
            ledSala.off()
            operacao = "desligada"
        else:
            ledSala.on()
        luzSala = (not luzSala)
    if(tipo == "quarto"):
        if(luzQuarto):
            ledQuarto.off()
            operacao = "desligada"
        else:
            ledQuarto.on()
        luzQuarto = (not luzQuarto)
    return f"Luz {tipo} {operacao}"

@app.route('/evento/portao', methods=['POST'])
def acionarPortao():
    global portao

    operacao = "Abrindo"
    if(portao):
        ledPortao.off()
        operacao = "Fechando"
    else:
        ledPortao.on()
    portao = (not portao)
    return f"{operacao} Portão"


