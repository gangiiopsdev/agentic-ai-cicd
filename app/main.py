from fastapi import FastAPI
import subprocess
def safe_subprocess(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

cmd = ['ping', host]
if isinstance(host, str) and len(host.split()) == 1:
    output = safe_subprocess(cmd)
    return {"status": "completed", "output": output}
else:
    raise ValueError('Invalid input')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_subprocess(cmd)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {'error': str(e)}