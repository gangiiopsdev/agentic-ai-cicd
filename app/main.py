from fastapi import FastAPI
import subprocess
gt
app = FastAPI()
gt
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
gt
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)
gt