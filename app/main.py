from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.', '_'))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}
# Additional security measures
import shlex
def safe_subprocess(command_parts):
    command = ' '.join(shlex.quote(arg) for arg in command_parts)
    subprocess.run(command, shell=True, check=True)