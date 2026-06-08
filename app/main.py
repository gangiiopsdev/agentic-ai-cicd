from fastapi import FastAPI
import subprocess
def execute_command(command):
    return subprocess.run(command, check=True, text=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input
    safe_host = subprocess.list2cmdline([host])
    command = ['ping', safe_host]
    result = execute_command(command)
    return {'status': 'completed', 'output': result.stdout}