from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell(input_str):
    return ''.join([c if c.isalnum() or c in '._-\@:' else '_' for c in input_str])

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell(host)
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}