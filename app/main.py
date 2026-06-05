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
    subprocess.call(ping_command.format(sanitized_host))
    
    return {"status": "completed"}