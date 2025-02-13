from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
import html
from datetime import datetime

app = Flask(__name__, static_folder = "static",template_folder= "templates")


def signe_zodiac(date):
    month = date.month
    day = date.day
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Verseau"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Poissons"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Bélier"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taureau"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gémeaux"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Lion"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Vierge"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Balance"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpion"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittaire"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorne"
    else:
        return "Inconnu"


@app.route('/')
def accueil():
    return render_template('accueil.html', titre="Horoscope du Jour")


@app.route('/horoscope', methods=['POST'])
def horoscope():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    date_str = request.form.get('date')

    if not nom or not prenom or not date_str:
        return jsonify({"erreur": "parametre manquant"}), 400

    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return jsonify({"erreur": "date invalide"}), 400

    signe =signe_zodiac(date)
    prediction = "Aujourd'hui vous allez devenir riche!"
    image = f"{signe.lower()}.jpg"

    return jsonify({
        "nom": nom,
        "prenom": prenom,
        "signe": signe,
        "prediction": prediction,
        "image": image
    })


@app.errorhandler(404)
def page_not_found(e):
    return render_template('erreur.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
