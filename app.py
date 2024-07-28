from flask import Flask, render_template
from pets_dict import pets

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/animals/<pet_type>')
def animals(pet_type):
    return render_template('animals.html', pet_type=pet_type,
                           pets=enumerate(pets[pet_type]))


@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    return render_template('pet.html', pet_type=pet_type, pet=pet)


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5001, debug=True)
