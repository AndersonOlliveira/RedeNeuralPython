from flask import Flask, render_template,request

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
       boas = "<h1>Olá, Programadores! </h1>"
       instr = '<p>Entre com dois número </p>'
       return  boas + instr

@app.route('/somar/')
@app.route('/somar/<num01>/<num02>')

def somar(num01=0,num02=0):
    resultado = float(num01)+float(num02)
    return str(resultado)
# @app.route('/logar', methods=['GET', 'POST'])
# def logar():
#    if request.method == 'POST':
#      return 'Recebeu um post, fazer login' 
#    else:
#      return "Recebu um Get !, exibir form de login"  
if __name__ == '__main__':
    app.run()