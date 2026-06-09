from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Enhanced input validation to prevent command injection
    if not host or any(char in host for char in ('&&', ';', '|', '`')):
        return None  
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    if output is None:
        return {"status": "invalid input"}
    return {"status": "completed", "output": output}