from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input):
    return ' '.join(shlex.split(input))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}