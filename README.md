# connexion-demo

Contains a simplified version of the [petstore.yaml from OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/main/examples/v3.0/petstore.yaml).

The app loads the swagger file into a Connexion app running a Flask server. Only "listPets" works, with a single instance of pets being returned.
App starts on `http://localhost:8080`, the swagger ui is visible under `http://localhost:8080/ui/`.
