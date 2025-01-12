from flask import Blueprint, jsonify

# Buat Blueprint untuk mengorganisasi routes
main = Blueprint('main', __name__)

# Route dasar (contoh)
@main.route('/')
def home():
    return jsonify({
        "message": "Selamat datang di Flask app yang di-deploy di Railway!"
    })

# Route tambahan (contoh)
@main.route('/about')
def about():
    return jsonify({
        "message": "Ini adalah halaman tentang aplikasi Flask."
    })
