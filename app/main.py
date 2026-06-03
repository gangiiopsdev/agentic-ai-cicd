from fastapi import FastAPI
import subprocess
from shlex import quote
global_process = None
async def create_ping_process(host):
    global global_process
    if global_process and global_process.poll() is not None:
        global_process.terminate()
        await global_process.wait()
    # Use a full path for the executable to mitigate risks
    global_process = subprocess.Popen(['/bin/ping', quote(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    create_ping_process(host)
    return {'status': 'completed'}