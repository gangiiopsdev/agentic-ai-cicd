from fastapi import FastAPI
import subprocess
from shlex import quote
generate_ping_command = lambda host: ['ping', quote(host)]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.run(generate_ping_command(host), check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': str(e)}

    return {'status': 'completed'}