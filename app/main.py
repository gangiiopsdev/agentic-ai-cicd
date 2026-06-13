from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid command injection
    host = sanitize_input(host)
    try:
        args = shlex.split('ping ' + host)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}