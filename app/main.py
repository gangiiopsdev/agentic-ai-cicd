from fastapi import FastAPI
import subprocess

def execute_ping(host):
    # Validate the host input to ensure it does not contain malicious characters
    if not host.isalnum():
        raise ValueError("Invalid input")
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'result': execute_ping(host)}