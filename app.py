from flask import Flask, request, jsonify
import os
import uuid

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_csv():
    file = request.files['file']
    request_id = str(uuid.uuid4())
    file.save(f"{request_id}.csv")
    return jsonify({"request_id": request_id, "message": "CSV received and processing started."})

@app.route('/status/<request_id>', methods=['GET'])
def check_status(request_id):
    output_csv = f"output_{request_id}.csv"
    if os.path.exists(output_csv):
        return jsonify({"request_id": request_id, "status": "Completed", "output_csv_path": output_csv})
    return jsonify({"request_id": request_id, "status": "Processing"})

if __name__ == '__main__':
    app.run(debug=True)