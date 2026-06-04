from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Simple validation example, can be more complex
    return '.' in host and '@' not in host

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid host"}
    command = ["ping", shlex.quote(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}