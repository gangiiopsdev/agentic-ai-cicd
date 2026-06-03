from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() and e.isprintable())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host or len(sanitized_host) > 100:
        raise ValueError("Invalid input for ping command")
    subprocess.run(shlex.split(f"ping {sanitized_host}"), check=True)
    return {"status": "completed"}