from flask import Flask

import ciphers.tools as tools, ciphers.extendedVigenere as extendedVigenere

app = Flask(__name__)

# Routes

if __name__=="__main__":
    app.run(debug = True)