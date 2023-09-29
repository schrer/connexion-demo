import json
from connexion import FlaskApp
from connexion.resolver import RelativeResolver

def list_pets(limit: int):
    pets = []
    for i in range(limit):
        pets.append(generate_pet(i))
    return pets



def generate_pet(id: int):
    return json.loads(f'{{"id":{id},"name":"Pet {id}","tag":"#pet{id}"}}')


app = FlaskApp(__name__, specification_dir='openapi/')
app.add_api('petstore.yaml', arguments={"title": "Connexion example"}, resolver=RelativeResolver("app"))
app.run(port=8080)