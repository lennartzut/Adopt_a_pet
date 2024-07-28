from flask import Flask
from pets_dict import pets

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry 
     friend:</p>
    <ul>
      <li><a href="/animals/dogs">Dogs</a></li>
      <li><a href="/animals/cats">Cats</a></li>
      <li><a href="/animals/rabbits">Rabbits</a></li>
    </ul>
    '''


@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f'<h1>List of {pet_type}</h1>'
    html += '<ul>'
    for idx, pet in enumerate(pets[pet_type]):
        html += (f'<li><a href="/animals/{pet_type}/{idx}">'
                 f'{pet["name"]}</a></li>')
    html += '</ul>'
    return html


@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    return f'''
        <h1>{pet['name']}</h1>
        <img src="{pet['url']}" alt="{pet['name']}" style="width
        :300px;height:auto;"><br> <p>{pet['description']}</p>
        <ul>
          <li><strong>Breed:</strong> {pet['breed']}</li>
          <li><strong>Age:</strong> {pet['age']} years</li>
        </ul>
        <a href="/animals/{pet_type}">Back to
        {pet_type.capitalize()}</a>
        '''


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5001, debug=True)
