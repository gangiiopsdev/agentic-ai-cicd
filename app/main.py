from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.Popen
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        ping_result = ping(host)
        return {'status': 'completed', 'output': ping_result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}