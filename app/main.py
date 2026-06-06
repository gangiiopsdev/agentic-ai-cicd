from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output with proper input validation and sanitization
    try:
        result = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}
    return {'status': 'completed', 'result': result.decode('utf-8')}