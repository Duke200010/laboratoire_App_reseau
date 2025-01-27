# Application Flask 

Cette application Flask permet à un utilisateur de soumettre un formulaire avec son nom et sa ville. Les données sont ensuite sécurisées contre les attaques XSS et affichées sur la même page. Si l'utilisateur tente d'accéder à une page non existante, une erreur 404 est renvoyée. L'application tourne au http://127.0.0.1:5000

## Fonctionnalités

- Formulaire pour saisir un nom et une ville.
- Validation et échappement des données pour éviter les attaques XSS (Cross-Site Scripting).
- Gestion d'une erreur 404 personnalisée pour les pages non trouvées.
- Affichage dynamique des informations soumises après validation.

## Prérequis

Avant d'exécuter l'application, assurez-vous que les prérequis suivants sont installés :

- **Python 3.x**
- **Flask**

### Installation des dépendances

1. Clonez ce repository ou téléchargez les fichiers.
2. Créez un environnement virtuel (optionnel mais recommandé) :

    ```bash
    python -m venv venv
    ```

3. Activez l'environnement virtuel :

    - Sur macOS/Linux :
      ```bash
      source venv/bin/activate
      ```
    - Sur Windows :
      ```bash
      .\venv\Scripts\activate
      ```

4. Installez les dépendances :

    ```bash
    pip install Flask
    ```

## Exécution de l'application

Une fois les dépendances installées, vous pouvez démarrer l'application avec la commande suivante :

```bash
python app.py

