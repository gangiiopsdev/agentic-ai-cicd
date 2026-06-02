from fastapi import FastAPI
import subprocess
def shell_escape(s):
    return ''.join(['\' + c if c in '"$' else c for c in s])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(f"ping {shell_escape(host)}")
    return {"status": "completed"}