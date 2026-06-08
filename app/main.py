from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell(s):
    return \''.join(c if c.isalnum() or c in '_.-' else '_' for c in s)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell(host)
    subprocess.call(f"ping {safe_host}", shell=False)
    return {"status": "completed"}