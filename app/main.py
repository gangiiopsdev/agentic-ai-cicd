from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = f"ping -c 1 {sanitized_host}"
    args = shlex.split(command)
    subprocess.run(args, check=True)
    return {"status": "completed"}