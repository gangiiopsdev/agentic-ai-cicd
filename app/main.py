from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}