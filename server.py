from flask import Flask, request, jsonify
import os
import hashlib

app = Flask(__name__)
FILE_STORE = "filestore"

# Ensure the file store directory exists
os.makedirs(FILE_STORE, exist_ok=True)

def calculate_hash(file_path):
    """Calculate the hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

@app.route('/add', methods=['POST'])
def add_files():
    files = request.files
    response = {}
    for filename, file in files.items():
        file_path = os.path.join(FILE_STORE, filename)
        if os.path.exists(file_path):
            response[filename] = "File already exists"
        else:
            file.save(file_path)
            response[filename] = "File added successfully"
    return jsonify(response)

@app.route('/ls', methods=['GET'])
def list_files():
    files = os.listdir(FILE_STORE)
    return jsonify(files)

@app.route('/rm', methods=['DELETE'])
def remove_file():
    filename = request.args.get('filename')
    file_path = os.path.join(FILE_STORE, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": f"{filename} removed successfully"})
    return jsonify({"error": "File not found"}), 404

@app.route('/update', methods=['POST'])
def update_file():
    files = request.files
    response = {}
    for filename, file in files.items():
        file_path = os.path.join(FILE_STORE, filename)
        temp_path = f"{file_path}.temp"
        file.save(temp_path)

        if os.path.exists(file_path):
            if calculate_hash(file_path) == calculate_hash(temp_path):
                os.remove(temp_path)
                response[filename] = "File already up to date"
            else:
                os.replace(temp_path, file_path)
                response[filename] = "File updated"
        else:
            os.rename(temp_path, file_path)
            response[filename] = "File added"
    return jsonify(response)

@app.route('/wc', methods=['GET'])
def word_count():
    total_words = 0
    for filename in os.listdir(FILE_STORE):
        file_path = os.path.join(FILE_STORE, filename)
        with open(file_path, 'r') as f:
            total_words += len(f.read().split())
    return jsonify({"word_count": total_words})

@app.route('/freq-words', methods=['GET'])
def freq_words():
    limit = int(request.args.get('limit', 10))
    order = request.args.get('order', 'dsc')
    word_freq = {}

    for filename in os.listdir(FILE_STORE):
        file_path = os.path.join(FILE_STORE, filename)
        with open(file_path, 'r') as f:
            for word in f.read().split():
                word_freq[word] = word_freq.get(word, 0) + 1

    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=(order == 'dsc'))
    return jsonify(sorted_words[:limit])

if __name__ == '__main__':
    app.run(port=5000)
