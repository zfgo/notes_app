# simple boiler plate app.py 

from flask import Flask, request, jsonify 

app = Flask(__name__)

# for now just 
notes = []
# notes = ["first note", "second note"]
next_id = 0 #

@app.get("/notes")
def get_notes():
    return jsonify(notes)

@app.post("/notes")
def create_note():
    global next_id # declare that you are about to modify the global variable
    data = request.get_json()
    text = data.get("text", "")
    note = {"id": next_id, "text": text}
    notes.append(note)
    next_id += 1

    return jsonify(note), 201

if __name__ == "__main__":
    app.run(debug=True)
