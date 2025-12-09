# simple boiler plate app.py 

from flask import Flask, jsonify 

app = Flask(__name__)

# for now just 
notes = []
# notes = ["first note", "second note"]
next_id = 1 #

@app.get("/notes")
def get_notes():
    return jsonify(notes)

if __name__ == "__main__":
    app.run(debug=True)
