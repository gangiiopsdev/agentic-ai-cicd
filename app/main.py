from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', '-c', '1'] + shlex.split(sanitized_host)
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'output': result.stdout}