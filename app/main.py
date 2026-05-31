from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        args = shlex.split(f'ping {sanitized_host}')
        subprocess.call(args)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}