from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return shlex.quote(input_str)

@app.get("/ping")
def ping_endpoint(host: str):
    host = sanitize_input(host)
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}