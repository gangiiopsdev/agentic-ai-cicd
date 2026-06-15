from fastapi import FastAPI
import subprocess
import shlex

class PingException(Exception):
    pass

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Use shlex.quote to safely escape the user input
        safe_host = shlex.quote(host)
        subprocess.call(['ping', safe_host])
        return {'status': 'completed'}
    except Exception as e:
        raise PingException(str(e))