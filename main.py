from flask import Flask
import random

app = Flask(__name__)

lista_consejo=["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
               "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones",
               "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
               "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo"]
moneda=["cara",
         "cruz"]


@app.route("/")
def index():
    return f'<h1>hola esta es mi pagina web y te dare consejos sobre la dependencia tecnologica, tambien puedes lanzar una moneda</h1><a href="/nuevo consejo">¡Ver un dato aleatorio!</a><a href="/lanzmon">¡Lanzar una moneda!</a>'

@app.route("/lanzmon")
def Lanzar_moneda():
    return f'<p>{random.choice(moneda)}</p>'


@app.route("/nuevo consejo")
def consejos():
    return f'<p>{random.choice(lista_consejo)}</p>'
    

app.run(debug=True)

