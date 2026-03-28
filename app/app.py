from flask import Flask, jsonify
import os
import socket
import datetime

app = Flask(__name__)

# Environment variables
APP_VERSION = os.environ.get('APP_VERSION', '1.0.0')
APP_ENV = os.environ.get('APP_ENV', 'development')

@app.route('/')
def home():
    return jsonify({
        'app': 'Sarmad DevOps App',
        'version': APP_VERSION,
        'environment': APP_ENV,
        'message': 'Welcome! App is running successfully 🚀'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'hostname': socket.gethostname()
    })

@app.route('/info')
def info():
    return jsonify({
        'app': 'Sarmad DevOps App',
        'version': APP_VERSION,
        'environment': APP_ENV,
        'hostname': socket.gethostname(),
        'platform': os.uname().sysname if hasattr(os, 'uname') else 'Windows'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)