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
    # Use os.path.abspath to ensure the command is fully qualified and avoid shell=True
    sanitized_host = host.replace(';', '').replace('&', '')
    result = subprocess.run([os.path.abspath('/bin/ping'), sanitized_host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}