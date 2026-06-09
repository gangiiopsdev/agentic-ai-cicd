from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_input(input_string):
    return ''.join(c if c.isalnum() else '_' for c in input_string)

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and args
    try:
        escaped_host = escape_input(host)
        result = subprocess.run(['ping', escaped_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}