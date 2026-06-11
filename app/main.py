from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = f"ping {shlex.quote(sanitized_host)}"
    args = shlex.split(command)
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}