#REVISÃO DE FLASK
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def primeira_pagina():
    return '<h1> minha primeira pagina </h1>'
#form
@app.route('/formulario')
def formulario():
    form ='''<h1> formulario </h1>
    <from>
        <lapel>primeiro nome:</lapel>
        <input type= "text" placeholder="digite seu primeiro nome:"> <br><br>
        <lapel>segundo nome</lapel>
        <input type="text" placeholder="digite seu segundo nome:"><br><br>
        <input type="submit" value="enviar">
    </from>'''
    return form




#dados 
@app.route('/meu_nome_e_idade')
def nomeidade():
    return 'pedro, 17 anos'
#JASON do nome e idade
@app.route('/dados')
def idadenome():
    dados = {
        'nome': 'Pedro',
        'idade': 17
    }
    return jsonify(dados)



@app.route('/v1/user/idade/<nome>')
def rertonar_idade(nome):
    if nome == 'pedro':
        return jsonify(idade=17)
    else:
        return jsonify('não encontrado')






if __name__ == '__main__':
    app.run(debug=True)






