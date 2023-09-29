import json
import connexion
from connexion.resolver import RelativeResolver

def listPets(limit: int):
    p1 = json.loads('{"id":1,"name":"Pet 1","tag":"#pet1"}')
    return [p1]


app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('petstore.yaml', arguments={"title": "Connexion example"}, resolver=RelativeResolver("app"))
app.run(port=8080)