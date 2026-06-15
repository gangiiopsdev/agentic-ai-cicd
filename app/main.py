from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    response = safe_ping(host)
    return {"status": "completed", "response": response}