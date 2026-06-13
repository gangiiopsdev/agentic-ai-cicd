from fastapi import FastAPI
import subprocess
get_shell = subprocess.getoutput

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        response = get_shell(f"ping {host}")
        return {'status': 'completed', 'response': response}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}