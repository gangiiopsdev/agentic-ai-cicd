from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        args = ['ping', shlex.quote(sanitized_host)]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=10)
        return {"status": "completed", "output": output.decode()}  # Return ping output if needed
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}