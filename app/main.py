from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(cmd):
    try:
        result = subprocess.run(shlex.split(cmd), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    # Secure implementation with shlex to safely handle arguments
    cmd = f'ping {shlex.quote(host)}'
    output = run_command(cmd)
    return {'status': 'completed', 'output': output}