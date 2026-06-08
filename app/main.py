from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use shlex.quote to safely escape the host argument
        output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output.decode('utf-8')}'''

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)'''