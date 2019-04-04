# EPSI I4 - NoSQL - TP 3

#### Collaborateurs : 
- Marine LHUILLIER
- Meihdi FORTIN

## Sujet :
A l'aide du langage de programmation de votre choix et d'un driver Redis, développer une application capable de sauvegarder et de consulter des notes.

L'application devra permettre de :
- Consulter l'ensemble des notes sauvegardées sur le serveur
- Ajouter une note (en renseigner uniquement le contenu de celle-ci)
- Consulter une note à partir de son ID
- Supprimer une note à partir de son ID

## Solution choisie :
Le langage choisi pour ce projet est `python` associé au microframework Flask.
L'application développée permet ainsi de lancer un serveur HTTP faisant passerelle vers un server redis local.

### Prérequis :
La documentation et les commandes suivantes sont faites pour une distribution `Linux`.

Il est nécessaire afin de pouvoir lancer l'application que votre poste dispose de :
- **Python3**
    - Commande d'installation : `sudo apt-get install python3`
- **RedisServer**
    - Commande d'installation : `sudo apt-get install redis-server`
- **Flask**
    - Commande d'installation : `sudo apt install python3-flask`
- **Git**
    - Commande d'installation : `sudo apt install git`


### Installation du projet :

Pour télécharger le projet lancer la commande :
```
$ git clone https://github.com/MarineLH/I4_no_sql_TP_3.git
```

Une fois fait, lancer les commandes suivantes afin d'instancier redis dans le projet :
```
$ cd I4_no_sql_TP_3/redis-py
$ sudo python3 setup.py install
```

### Lancer le serveur HTTP et le serveur Redis :

La partie suivante va permettre de démarrer un serveur Redis Local ainsi que notre application (serveur HTTP).

- **Lancer le server redis :**
```
$ sudo service redis-server start
```
- **Lancer le server HTTP :**
```
$ cd chemin/vers/I4_no_sql_TP_3
$ python3 FlaskServer.py
```

Notre serveur HTTP est maitenant fonctionnel :
```
* Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 125-398-279
```

### Utilisation de l'application : 

Plusieurs méthodes sont disponibles afin d'utiliser le serveur HTTP pour sauvegarder et consulter des données sur le serveur Redis,
notamment avec l'utilisation de commandes `curl`ou via l'application bureau `Postman`.

- **Créer une note :**
    - CURL : `curl -H "Content-Type:text/plain" --data 'le_contenu_de_la_note" http://localhost:8080/notes`
    - POSTMAN :
   

