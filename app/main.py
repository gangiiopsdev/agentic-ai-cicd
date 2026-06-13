from fastapi import FastAPI
import subprocess
import shlex
delimiter = ':'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        args = ['ping'] + shlex.split(host)
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        output, error = process.communicate()
        return {'status': 'completed', 'output': output.decode('utf-8'), 'error': error.decode('utf-8')}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'message': 'Operation timed out'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}