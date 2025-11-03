from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    color = ""
    if request.method == "POST":
        datamon = request.form.get("datamon", "").strip()
        answer = request.form.get("answer", "").strip()

        if not datamon or not answer:
            result = "⚠️ Please enter both fields!"
            color = "missing"
        elif datamon.lower() == answer.lower():
            result = "✅ Correct!"
            color = "correct"
        else:
            result = "❌ Incorrect!"
            color = "incorrect"

    return render_template("index.html", result=result, color=color)

if __name__ == "__main__":
    app.run(debug=True)