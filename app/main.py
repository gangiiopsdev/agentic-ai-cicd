from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_command(input_str):
    return ''.join(shlex.quote(c) for c in input_str)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_command(host)
    # Secure implementation
    subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    return {"status": "completed"}