from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(user_input):
    return shlex.quote(user_input)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}