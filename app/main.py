from fastapi import FastAPI
import subprocess
import shlex

cdef shlex_quote(host):
    return shlex.quote(host)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Use shlex to safely quote the host argument
        command = ['ping', shlex_quote(host)]
        subprocess.call(command)
    except Exception as e:
        return {'error': str(e)}
    return {'status': 'completed'}