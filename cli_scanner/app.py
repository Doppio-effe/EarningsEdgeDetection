from flask import Flask, jsonify
import subprocess, json, sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def scan():
    try:
        result = subprocess.run(['python3', 'scanner.py', '--list'], 
                               capture_output=True, text=True, timeout=900)
        return jsonify(json.loads(result.stdout))
    except:
        return jsonify({"error": "scan failed", "logs": result.stderr})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
