from flask import Flask, request
import RedisServer
import uuid

app = Flask(__name__)

server_host = "127.0.0.1"
server_port = 8080


@app.route("/", methods=['GET'])
def index():
    return "Utilisation du serveur : " \
           "\n\n - Récupérer toutes les notes : \n" \
           "      GET http://" + server_host + ":" + str(server_port) + "/notes" \
           "\n\n - Récupérer une note à partir de son id : \n" \
           "      GET http://" + server_host + ":" + str(server_port) + "/notes/{id}" \
           "\n\n - Créer une note : \n" \
           "      POST http://" + server_host + ":" + str(server_port) + "/notes" \
           "\n      avec dans le body le contenu de la note à créer"


@app.route("/notes", methods=['GET'])
def get_notes():
    notes = RedisServer.get_all_notes()
    return "Récupération de toutes les notes disponibles : \n" + str(notes)


@app.route("/notes/<string:id>", methods=['GET'])
def get_note(id):
    note = RedisServer.get_note(id)
    if note is None:
        reponse = "Il n'existe aucune note avec l'id : " + id
    else:
        reponse = "Récupération de la note " + id + " : \n    " + note

    return reponse


@app.route("/notes", methods=['POST'])
def post_note():
    id = uuid.uuid4().hex
    RedisServer.post_note(str(id), str(request.data)[2:-1])
    return "Création de la note : " + str(request.data)[2:-1] + "\nAvec l'id : " + str(id)


@app.route("/notes/<string:id>", methods=['DELETE'])
def delete_note(id):
    note = RedisServer.delete_note(id)
    if note == 0:
        reponse = "Impossible de supprimer la note avec l'id : " + id + " car elle n'existe pas"
    else:
        reponse = "La note avec l'id : " + id + " a bien été supprimée"
    return reponse


if __name__ == "__main__":
    app.run(host=server_host, port=server_port, debug=True)
