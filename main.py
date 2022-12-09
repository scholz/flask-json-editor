from flask import Flask, request, jsonify, render_template, redirect
import json

app = Flask(__name__, template_folder="templates")

with open('data.json') as json_file:
        data = json.load(json_file)

@app.route('/')
def index():
    # Load the JSON file every time the index is called
    with open('data.json') as json_file:
        data = json.load(json_file)
    # Render the HTML form using Jinja2 template
    return render_template('form.html', data=data)

@app.route('/update', methods=['POST'])
def add_entry():

    # Get the data from the form submission
    new_data = request.form

    # Iterate over the elements of the data
    for key, value in new_data.items():
        # Get the original value from the JSON structure
        original_value = data[key]

        # Check the type of the original value
        if type(original_value) == dict:
            # If the original value is a dictionary, iterate over its elements
            for subkey, subvalue in original_value.items():
                # Check the type of the input value
                if type(value) != type(subvalue):
                    # If the types do not match, return an error message
                    return "Error: the type of the input value for '{}' does not match the original type.".format(key)
        else:
            # If the original value is not a dictionary, check the type of the input value
            if type(value) != type(original_value):
                # If the types do not match, return an error message
                return "Error: the type of the input value for '{}' does not match the original type.".format(key)

    # If no errors were encountered, update the JSON structure with the new data
    data.update(new_data)

    # Save the updated data to the JSON file
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)
        
    # Redirect to the index page to show the updated data
    return redirect('/')

    

if __name__ == '__main__':
    app.run()
