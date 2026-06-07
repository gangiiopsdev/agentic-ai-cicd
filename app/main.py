from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}