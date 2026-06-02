from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e if e.isalnum() or e in ('-', '.', '_') else '_' for e in input_str)

def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, check=True, shell=False)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}