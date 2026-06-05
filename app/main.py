from fastapi import FastAPI
import subprocess
import shlex
def escape_input(input_str):
    return shlex.quote(input_str)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with input escaping
    subprocess.run(["ping", escape_input(host)], check=True)
    return {"status": "completed"}