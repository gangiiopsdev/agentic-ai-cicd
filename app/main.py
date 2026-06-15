from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

allowed_hosts_pattern = re.compile(r'^(example\.com|127\.0\.0\.1)$')

def validate_host(host):
    if not allowed_hosts_pattern.match(host):
        raise ValueError("Invalid host")

@app.get="/ping"
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}