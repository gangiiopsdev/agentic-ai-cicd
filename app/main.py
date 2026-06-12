from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}