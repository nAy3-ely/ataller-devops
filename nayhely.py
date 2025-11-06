# nayhely.py (VERSION FINAL CON FLASK)

from flask import Flask
from datetime import datetime

app = Flask(__name__)
PORT = 10000 # Puerto que Render necesita

@app.route("/")
def home():
    html_content = f"""
    <html>
    <head><title>Taller Nayhely Valle - Flask</title></head>
    <body>
        <h1>👋 ¡Hola! Este es mi Taller de Contenedores con Flask</h1>
        <p>La fecha y hora actual del contenedor es: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>✅ Servicio desplegado en Render.</p>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)