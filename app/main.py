from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if any(char in host for char in ' <>|&;*?`$(){}[]\'):  # Check for potentially harmful characters
        raise ValueError("Invalid characters in host")
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)