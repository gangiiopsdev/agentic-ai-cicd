from fastapi import FastAPI
import subprocess
def ping_safe(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', '--', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        output = ping_safe(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}