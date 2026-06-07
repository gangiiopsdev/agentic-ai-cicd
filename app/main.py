from fastapi import FastAPI
import subprocess
global_subprocess = subprocess.Popen(['ping'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global_subprocess.stdin.write(f' {host}
'.encode())
    global_subprocess.stdin.flush()
    output, _ = global_subprocess.communicate()
    return {'status': 'completed', 'output': output.decode() if output else None}