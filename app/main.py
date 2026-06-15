from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    # Use check_output instead of call and capture output
    try:
        result = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {'result': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e.output.decode())}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)