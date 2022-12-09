# flask-json-editor
(not functional at the moment)
A chatGPT experiment, this is a generic simple json editor served by flask.
Could be used e.g. as a config editor for some dev tool or otherwise.

# missing
* complete write support for more complex json structures (reading works; although rendering could be improved)
* type checking
* list support

# implementation
The json file data.json is displayed in a web form served by flask.
The file can be updated. 

# running
1. python -m venv .venv
2. .venv\Scripts\activate.bat (windows)
3. pip install -r requirements.txt
4. python main.py


# credit
Built iteratively with chatGPT.
