from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
from signal import alarm, signal, SIGALRM
def ping(host: str):
    def handler(signum, frame):
        raise TimeoutExpired("ping command timed out")
    try:
        alarm(5)
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return JSONResponse(content={'status': 'completed', 'output': output.decode()})
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'failed', 'error': e.output.decode()}, status_code=500)
    except TimeoutExpired:
        return JSONResponse(content={'status': 'timeout', 'message': 'ping command timed out'}, status_code=408)
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)