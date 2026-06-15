from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without shell=True
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}