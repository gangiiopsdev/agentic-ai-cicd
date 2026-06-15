from fastapi import FastAPI
import subprocess
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except cimport as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive Controls:
# 1. Validate input to ensure it does not contain malicious commands.
# 2. Use absolute paths for system commands.
# 3. Consider using a safer alternative if possible, such as ping libraries.