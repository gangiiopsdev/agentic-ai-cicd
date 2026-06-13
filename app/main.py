from fastapi import FastAPI
import subprocess
import shlex
globally_banned_hosts = ['192.168.1.1', '10.0.0.1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in globally_banned_hosts:
        return {'status': 'banned'}
    try:
        # Using subprocess.Popen instead of subprocess.run for better control
        process = subprocess.Popen(['ping', '-c', '1', shlex.quote(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate(timeout=5)
        if process.returncode == 0:
            return {'status': 'completed'}
        else:
            return {'status': str(error)}
    except subprocess.TimeoutExpired as e:
        return {'status': 'timeout'}
    except Exception as e:
        return {'status': str(e)}