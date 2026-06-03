from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': output.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)