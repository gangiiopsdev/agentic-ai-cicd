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
        # Use subprocess.run to safely execute the command with user-supplied input
        result = subprocess.run(['ping', shlex_quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'error': str(e)}