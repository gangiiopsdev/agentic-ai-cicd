from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(user_input):
    return shlex.quote(user_input)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', sanitized_host]
    process = subprocess.Popen(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}