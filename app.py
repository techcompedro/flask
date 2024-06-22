from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '''<h1>minha primeira pagina</h1>
    <form>
           <label>primeiro nome:</label>
           <input type="text"><br><br>
           <lapel>segundo Nome</label>
           <input type="text"><br><br>
           <input type="submit" value="enviar">
    </form>'''
app.run()
