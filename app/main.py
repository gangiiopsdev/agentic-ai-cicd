from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_safe_command(command, *args):
    return subprocess.run([command] + [shlex.quote(arg) for arg in args], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with check=True and shell=False
    result = execute_safe_command('ping', host)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}