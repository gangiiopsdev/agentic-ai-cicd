from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return input_str.replace(';', '').replace('&', '').replace('||', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    args = shlex.split(f'ping {sanitized_host}')
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}