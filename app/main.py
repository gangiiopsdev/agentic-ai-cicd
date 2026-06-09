from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host: str) -> str:
    return shlex.quote(host)

@app.get("/ping")
def ping(host: str):
    # Use a secure way to escape and construct the command
    escaped_host = escape_host(host)
    result = subprocess.run(["ping", "-c", str(4), escaped_host], check=True, capture_output=True, text=True)
    return {
        "status": "completed",
        "response": result.stdout
    }