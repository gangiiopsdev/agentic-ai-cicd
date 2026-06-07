from fastapi import FastAPI
import subprocess
global ping_command
ping_command = ['ping', '{}']

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(shlex.split(f'{ping_command[0]} {sanitized_host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "stdout": subprocess.getoutput(f'{ping_command[0]} {sanitized_host}')}