from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}

# Add input validation and sanitization for 'host'
def validate_host(host: str):
    # Implement validation logic here
    pass

@app.post("/ping")
def ping_endpoint(host: str = Query(..., description="Target host to ping")):
    validated_host = validate_host(host)
    if not validated_host:
        return {"status": "error", "message": "Invalid input"}
    return ping(validated_host)