from flask import Flask, render_template, request, jsonify, redirect, url_for
import uuid

app = Flask(__name__)

@app.route("/")
def index():
    session_id = str(uuid.uuid4())[:8]  # z. B. "a9f3bd7e"
    return redirect(url_for("chat", session_id=session_id))

@app.route("/chat/<session_id>")
def chat(session_id):
    return render_template("chat.html", session_id=session_id)

