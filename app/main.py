from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation: allow only alphanumeric characters and hyphens
    return ''.join(c for c in host if c.isalnum() or c == '-').strip()

@app.get("/ping")
def ping(host: str):
    validated_host = validate_host(host)
    if not validated_host:
        return {"error": "Invalid host name"}
    args = ['ping', validated_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}