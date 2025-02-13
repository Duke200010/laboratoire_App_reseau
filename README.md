# Application Flask - Horoscope

Cette application Flask permet à un utilisateur de soumettre un formulaire avec son nom, prénom et date de naissance pour obtenir son signe du zodiaque et une prédiction astrologique. Les données sont traitées de manière asynchrone via AJAX, et l'horoscope est affiché dynamiquement sans recharger la page. L'application tourne sur `http://127.0.0.1:5000`.

## Fonctionnalités

- Formulaire pour saisir un nom, un prénom et une date de naissance.
- Validation des données côté serveur (vérification des champs obligatoires et de la validité de la date).
- Calcul du signe du zodiaque en fonction de la date de naissance.
- Affichage dynamique de l'horoscope (signe du zodiaque, prédiction et image associée) sans recharger la page.
- Gestion d'une erreur 404 personnalisée pour les pages non trouvées.
- Utilisation de jQuery pour les requêtes AJAX et la manipulation du DOM.

## Images disponibles

Actuellement, seules les images pour les signes **Poisson** et **Cancer** sont disponibles dans le dossier `static/images/`. Si l'utilisateur a un autre signe du zodiaque, l'image ne sera pas affichée.

## Prérequis

Avant d'exécuter l'application, assurez-vous que les prérequis suivants sont installés :

- **Python 3**
- **Flask**


