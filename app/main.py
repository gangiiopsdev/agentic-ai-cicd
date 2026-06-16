from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.run instead of subprocess.Popen with shell=True
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output, error = safe_ping(host)
    if error:
        return {'status': 'completed', 'error': error}
    else:
        return {'status': 'completed', 'output': output}