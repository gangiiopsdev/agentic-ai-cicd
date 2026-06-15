from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', '-c 1', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}