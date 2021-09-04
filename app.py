from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)

# encrypt your message
def encoder(message):
    encoded_message = f'encoded {message}'
    return encoded_message

# decrypt your message
def decoder(message):
    decoded_message = f'decoded {message}'
    return decoded_message


@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/encode')
def encode():
    return render_template('encode.html') 


@app.route('/encoded_message', methods=['POST'])
def encoded_message():
    text = request.form['encode_message']
    encoded_text = encoder(text)
    return render_template('encoded_message.html', encoded_text=encoded_text) 


@app.route('/decode')
def decode():
    return render_template('decode.html') 


@app.route('/decoded_message', methods=['POST'])
def decoded_message():
    text = request.form['decode_message']
    decoded_text = decoder(text)
    return render_template('decoded_message.html', decoded_text=decoded_text) 

app.run(debug=True)
