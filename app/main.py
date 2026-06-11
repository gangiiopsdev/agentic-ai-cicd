from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = execute_ping(host.replace(';', '').replace('&', ''))  # Sanitize input to prevent command injection
    return {'status': 'completed', 'output': output}