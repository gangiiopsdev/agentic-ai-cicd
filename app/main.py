from fastapi import FastAPI
import subprocess
global host_var
def ping(host: str):
    global host_var
    host_var = host

@app.get("/ping")
def ping_command():
    try:
        result = subprocess.run(['ping', host_var], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}