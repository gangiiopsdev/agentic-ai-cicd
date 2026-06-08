from fastapi import FastAPI
import subprocess
import shlex
class SanitizedInput:
    @staticmethod
def sanitize_input(value):
        return ''.join(e for e in value if e.isalnum() or e in ['-', '.', '_', '/', ':'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = SanitizedInput.sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', shlex.quote(sanitized_host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode('utf-8')}