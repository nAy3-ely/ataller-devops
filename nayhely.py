# nayhely.py (VERSION FINAL con FLASK para Render)

from flask import Flask
from datetime import datetime

# La aplicación Flask se inicializa
app = Flask(__name__)

# Puerto que Render DEBE USAR (10000)
PORT = 10000

@app.route("/")
def home():
    """Ruta principal que muestra el mensaje del taller."""
    
    html_content = f"""
    <html>
    <head><title>Taller Nayhely Valle - Flask</title></head>
    <body>
        <h1>👋 ¡Hola! Este es mi Taller de Contenedores con Flask</h1>
        <p>El framework web usado es: <b>Flask</b> (v2.2.5)</p>
        <p>La fecha y hora actual del contenedor es: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>✅ El servicio Docker está funcionando correctamente en Render.</p>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    # Flask sirve la aplicacion en el puerto 10000
    app.run(host='0.0.0.0', port=PORT)