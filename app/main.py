from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c.isspace())

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        args = shlex.split('ping ' + sanitized_host)
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}