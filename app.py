#REVISÃO DE FLASK
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def primeira_pagina():
    return '<h1> minha primeira pagina </h1>'
   
@app.route('/formulario')
def formulario():
    form ='''<h1> minha primeira pagina </h1>
    <from>
        <lapel>primeiro nome:</lapel>
        <input type= "text" placeholder="digite seu primeiro nome"> <br><br>
        <lapel>segundo nome</lapel>
        <input type="text" placeholder="digite seu segundo nome"><br><br>
        <input type="submit" value="enviar">
    </from>'''
    return form

@app.route('/formulario do imc')
def formularioimc():
    html ='''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de IMC</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-bottom: 8px;
        }
        input[type="number"], input[type="submit"] {
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
            transition: border-color 0.3s ease-in-out;
        }
        input[type="number"]:focus {
            outline: none;
            border-color: #4CAF50;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease-in-out;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .resultado {
            background-color: #f9f9f9;
            border: 1px solid #ccc;
            padding: 15px;
            border-radius: 4px;
            margin-top: 20px;
        }
        .resultado h3 {
            margin-top: 0;
            font-size: 24px;
            text-align: center;
            margin-bottom: 10px;
        }
        .resultado p {
            text-align: center;
            font-size: 18px;
            margin: 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Calculadora de IMC</h2>
        <form id="formIMC">
            <label for="peso">Peso (kg):</label>
            <input type="number" id="peso" name="peso" required>

            <label for="altura">Altura (m):</label>
            <input type="number" id="altura" name="altura" step="0.01" required>

            <input type="submit" value="Calcular">
        </form>

        <div class="resultado" id="resultadoIMC">
            <!-- Aqui será exibido o resultado do IMC -->
        </div>
    </div>

    <script>
        document.getElementById('formIMC').addEventListener('submit', function(event) {
            event.preventDefault();

            // Obtendo os valores de peso e altura
            var peso = parseFloat(document.getElementById('peso').value);
            var altura = parseFloat(document.getElementById('altura').value);

            // Calculando o IMC
            var imc = peso / (altura * altura);

            // Determinando a condição de saúde baseada no IMC
            var resultado = '';
            if (imc < 18.5) {
                resultado = 'Você está abaixo do peso.';
            } else if (imc >= 18.5 && imc < 25) {
                resultado = 'Seu peso está normal (dentro da faixa saudável).';
            } else if (imc >= 25 && imc < 30) {
                resultado = 'Você está com sobrepeso.';
            } else {
                resultado = 'Você está obeso.';
            }

            // Exibindo o resultado do IMC e a condição de saúde
            var resultadoElement = document.getElementById('resultadoIMC');
            resultadoElement.innerHTML = `
                <h3>Seu IMC é: ${imc.toFixed(2)}</h3>
                <p>${resultado}</p>
            `;
        });
    </script>
</body>
</html>



'''

    return html




if __name__ == '__main__':
    app.run(debug=True)






