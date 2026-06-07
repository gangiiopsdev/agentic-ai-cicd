from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if not host.isalnum():
        raise ValueError("Invalid host name")
    try:
        command = ['ping', host]
        command = shlex.split(' '.join(command))  # Use shlex to safely handle the command
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    try:
        return {'status': safe_ping(host)}
    except ValueError as e:
        return {'error': str(e)}, 400