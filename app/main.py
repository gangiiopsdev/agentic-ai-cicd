from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    try:
        # Sanitize input by ensuring it does not contain potentially harmful characters
        if any(char in host for char in [';', '|', '&', '*', '$']):
            raise ValueError('Invalid characters detected in hostname')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)