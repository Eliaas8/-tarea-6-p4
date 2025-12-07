from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_db
from uuid import uuid4
import json, os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET")

db = get_db()

@app.route("/")
def index():
    libros = []
    for key in db.scan_iter("libro:*"):
        libros.append(json.loads(db.get(key)))
    return render_template("index.html", libros=libros)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = {
            "id": str(uuid4()),
            "titulo": request.form["titulo"].strip(),
            "autor": request.form["autor"].strip(),
            "genero": request.form["genero"].strip(),
            "estado": request.form["estado"].strip()
        }

        if not all(data.values()):
            flash("Todos los campos son obligatorios", "danger")
            return redirect(url_for("add"))

        db.set(f"libro:{data['id']}", json.dumps(data))
        flash("Libro agregado correctamente", "success")
        return redirect(url_for("index"))

    return render_template("add.html")

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    key = f"libro:{id}"

    if not db.exists(key):
        flash("Libro no encontrado", "danger")
        return redirect(url_for("index"))

    libro = json.loads(db.get(key))

    if request.method == "POST":
        for campo in ["titulo", "autor", "genero", "estado"]:
            libro[campo] = request.form[campo].strip()

        db.set(key, json.dumps(libro))
        flash("Libro actualizado", "success")
        return redirect(url_for("index"))

    return render_template("edit.html", libro=libro)

@app.route("/delete/<id>")
def delete(id):
    eliminado = db.delete(f"libro:{id}")
    if eliminado:
        flash("Libro eliminado", "success")
    else:
        flash("Libro no encontrado", "danger")
    return redirect(url_for("index"))

@app.route("/search")
def search():
    criterio = request.args.get("criterio")
    valor = request.args.get("valor", "").lower()

    resultados = []
    for key in db.scan_iter("libro:*"):
        libro = json.loads(db.get(key))
        if valor in libro.get(criterio, "").lower():
            resultados.append(libro)

    return render_template("index.html", libros=resultados)

if __name__ == "__main__":
    app.run(debug=True)
