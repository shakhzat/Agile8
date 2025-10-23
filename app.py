from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Бет үлгісі (форма)
HTML_PAGE = """
<!doctype html>
<title>Қарапайым форма</title>
<h1>Сәлем! Бұл қарапайым Flask қосымшасы</h1>
<form method="post" action="/submit">
  <label>Атыңыз: <input name="name"></label><br><br>
  <label>Хабарлама: <input name="msg"></label><br><br>
  <button type="submit">Жіберу</button>
</form>

{% if result %}
<h2>Нәтиже:</h2>
<p><b>Аты:</b> {{ result.name }}</p>
<p><b>Хабарлама:</b> {{ result.msg }}</p>
{% endif %}
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "Аты жоқ")
    msg = request.form.get("msg", "")
    return render_template_string(HTML_PAGE, result={"name": name, "msg": msg})

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
