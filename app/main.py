from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str: str) -> str:
    if not input_str or len(input_str) > 255:
        return None
    return input_str.strip().replace('\', '').replace(';', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host is None:
        return {'error': 'Invalid host'}, 400
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}