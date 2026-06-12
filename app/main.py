from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it only contains expected characters (e.g., alphanumeric and possibly hyphens or dots)
    if not host.isalnum() and not all(c in '-.' for c in host):
        return {'status': 'error', 'result': 'Invalid input'}
    result = run_ping(host)
    return {'status': 'completed', 'result': result}