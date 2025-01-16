from flask import Flask, render_template, request, redirect, url_for
import html

app = Flask(__name__, static_folder = "static",template_folder= "templates")

@app.route("/", methods=["GET", "POST"])
def accueil():
    if request.method == "POST":
        # Validation des entrées pour éviter les injections
        nom = html.escape(request.form.get("nom"))
        ville = html.escape(request.form.get("ville"))
        return render_template("accueil.html", nom=nom, ville=ville, formulaire=False)
    
    return render_template("accueil.html", formulaire=True)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("erreur.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
