from flask import Flask, jsonify, render_template, redirect, request
from utils import get_pdf_text, get_docx_text, query_response
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return redirect("/process_resume")

@app.route("/process_resume", methods=["GET", "POST"])
def process_resume():
    if request.method == "POST":
        file = request.files['doc']
        option = request.form['document_type']

        if option == "pdf":
            text = get_pdf_text(file)
        elif option == "docx":
            text = get_docx_text(file)
        else:
            text = file.read().decode("utf-8")

        query_res = query_response(text)
        data = json.loads(query_res)  

        return render_template("result.html", data=data)
    else:
        return render_template("resume_upload.html")

if __name__ == "__main__":
    app.run(debug=True)
