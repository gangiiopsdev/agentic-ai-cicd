from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.Popen instead of subprocess.call with shell=True
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

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