from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if host.isnumeric() and len(host) <= 15:
        try:
            result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}

    return {'error': 'Invalid or too long host'}