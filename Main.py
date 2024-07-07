from flask import Flask, request
import os

app = Flask(Aitech-folder)

def save_user_data(name, email, number):
    data_folder = 'user_data'
    os.makedirs(data_folder, exist_ok=True)

    with open(os.path.join(data_folder, f'{name}.txt'), 'w') as file:
        file.write(f'Nom: {name}\nEmail: {email}\nNuméro: {number}')

@app.route('/user', methods=['POST'])
def save_form_data():
    name = request.form.get('name')
    email = request.form.get('email')
    number = request.form.get('number')
    
    save_user_data(name, email, number)
    
    return 'Données enregistrées avec succès!'

if Aitech-folder == 'main.py':
    app.run(host='0.0.0.0', port=8080)