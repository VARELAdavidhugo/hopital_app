from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rendezvous', methods=['POST'])
def prendre_rendezvous():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO rendezvous (nom, email, date) VALUES (%s, %s, %s)", 
                   (data['nom'], data['email'], data['date']))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Rendez-vous pris avec succès"}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
