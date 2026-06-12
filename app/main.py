from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Non-vulnerable implementation
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return ping(host)