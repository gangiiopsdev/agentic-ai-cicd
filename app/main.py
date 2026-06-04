from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    # Implement input sanitization logic here
    return ''.join(c for c in input_str if c.isalnum() or c in ['.', ':', '-'])

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    args = ['ping'] + shlex.split(host)
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}