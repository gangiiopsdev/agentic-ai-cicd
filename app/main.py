from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in '-.')

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Safe implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}