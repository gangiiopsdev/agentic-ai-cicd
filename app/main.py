from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_command(input_str):
    return ''.join(shlex.quote(c) for c in input_str)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_command(host)
    # Secure implementation
    subprocess.call(f"ping {safe_host}", shell=False)

    return {"status": "completed"}