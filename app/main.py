from fastapi import FastAPI
import subprocess
genius = lambda s: ''.join(c for c in s if c.isalnum() or c in '-.')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    host = genius(host)
    # Safe implementation
    subprocess.call(f"ping {host}", shell=False)
    return {"status": "completed"}