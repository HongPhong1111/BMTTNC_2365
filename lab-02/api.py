from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailfenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Caesar cipher algorithm
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Vigenere cipher algorithm
vigenere_cipher = VigenereCipher()

@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Railfence cipher algorithm
railfence_cipher = RailfenceCipher()

@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Playfair cipher algorithm
playfair_cipher = PlayfairCipher()

@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_create_matrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'matrix': playfair_matrix})

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_message': decrypted_text})

# Transposition cipher algorithm
transposition_cipher = TranspositionCipher()

@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = int(data['key'])
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = int(data['key'])
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)