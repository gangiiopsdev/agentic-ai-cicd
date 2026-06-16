from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):    
    # Safe implementation
    output = _ping(host)
    return {'output': output}