from flask import Flask, render_template, request, send_from_directory

import ciphers.myOwnStreamCipher as mosc
import ciphers.tools as tools
import ciphers.extendedVigenere as ev
import ciphers.playfair as pf

import base64
import os

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
DOWNLOAD_FOLDER = './downloads'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# Routes
@app.route("/", methods = ['POST', 'GET'])
def home():
    if request.method == "POST":
        file = request.files['file']
        text = request.form['plaintext']
        key = request.form['encryptionkey']
        mode = request.form['options']
        extension = request.form['extension']

        if text == "":
            # if neither exists
            if file.filename == '':
                return render_template('layout.html', error="No File not Text to Encrypt")
            inputfile = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(inputfile)
            text = tools.read_encrypt(inputfile)            
        if key == "":
            return render_template('layout.html', error='No Key Available')
        
        if mode == "1":
            cipher = mosc.mosc_encrypt(text, key)
            name = "encrypted"
            path = os.path.join(app.config['DOWNLOAD_FOLDER'], name)
            tools.export_encrypted(cipher, path)
            return((render_template('layout.html', error="", result = cipher, filename = name, textinput = text, key = key, extension = extension)))

        elif mode == "2":
            if extension == "":
                extension = "txt"
            try:
                plain = mosc.mosc_decrypt(text, key)
            except UnicodeDecodeError:
                return(render_template('layout.html', error = "Invalid input! Only base64 is accepted."))
            name = f"decrypted.{extension}"
            print(name)
            path = os.path.join(app.config['DOWNLOAD_FOLDER'], name)
            tools.export_decrypted(plain, path)
            return (render_template('layout.html', error="", result = plain, filename = name, textinput = text, key = key, extension = extension))
        
    return render_template('layout.html', error="")

@app.route("/downloads/<name>", methods=['GET'])
def downloads(name):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], name, as_attachment=True)

if __name__=="__main__":
    app.run(debug = True)