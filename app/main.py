from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_subprocess(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = ['ping', host]
    output = safe_subprocess(command)
    if 'error' in output.lower():
        return {"status": "error", "message": output}
    return {"status": "completed", "output": output}