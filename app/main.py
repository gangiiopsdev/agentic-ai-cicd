from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(user_input):
    return ''.join(c if c.isalnum() or c in ['-', '.', '_'] else '_' for c in user_input)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_command(host)
    subprocess.call(f"ping {safe_host}", shell=False)
    return {"status": "completed"}