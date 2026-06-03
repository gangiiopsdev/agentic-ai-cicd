from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    if 'ping' not in input_str.split():
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if sanitize_input(host):
        subprocess.call(['ping', host])
    else:
        raise ValueError("Invalid input detected")
    return {"status": "completed"}