from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in '-._~:/?#@[\]^!$&'"'(),;=')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}