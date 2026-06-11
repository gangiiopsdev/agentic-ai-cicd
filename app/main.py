from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation to ensure only alphanumeric characters are used
    return ''.join(c for c in host if c.isalnum() or c in ['.', '-'])

@app.get("/ping")
def ping(host: str):
    validated_host = validate_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1', validated_host], capture_output=True, text=True, check=True)
        return {'host': host, 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=str(e))