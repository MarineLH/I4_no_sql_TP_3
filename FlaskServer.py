from flask import Flask, request
import RedisServer
import uuid

app = Flask(__name__)

server_host = "127.0.0.1"
server_port = 8080
server_address = server_host + ":" + str(server_port)


@app.route("/", methods=['GET'])
def index():
    return "Utilisation du serveur : " \
           "\n\n - Récupérer toutes les notes : \n" \
           "      GET http://" + server_address + "/notes" \
           "\n\n - Récupérer une note à partir de son id : \n" \
           "      GET http://" + server_address + "/notes/{id}" \
           "\n\n - Créer une note : \n" \
           "      POST http://" + server_address + "/notes" \
           "\n      avec dans le body le contenu de la note à créer" \
           "\n\n - Supprimer une note : \n" \
           "      DELETE http://" + server_address + "/notes/{id}"


@app.route("/notes", methods=['GET'])
def get_notes():
    notes = RedisServer.get_all_notes()
    return "Récupération de toutes les notes disponibles : \n" + str(notes)


@app.route("/notes/<string:id>", methods=['GET'])
def get_note(id):
    note = RedisServer.get_note(id)
    if note is None:
        return "Il n'existe aucune note avec l'id : " + id
    else:
        return "Récupération de la note " + id + " : \n    " + note


@app.route("/notes", methods=['POST'])
def post_note():
    id = str(uuid.uuid4().hex)
    note = str(request.data)[2:-1]
    RedisServer.post_note(id, note)
    return "Création de la note : " + note + "\nAvec l'id : " + id


@app.route("/notes/<string:id>", methods=['DELETE'])
def delete_note(id):
    if RedisServer.delete_note(id) == 0:
        return "Impossible de supprimer la note avec l'id : " + id + " car elle n'existe pas"
    else:
        return "La note avec l'id : " + id + " a bien été supprimée"


if __name__ == "__main__":
    app.run(host=server_host, port=server_port, debug=True)
