from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    if not host.isalnum():
        return False
    # Additional validation can be added here to further restrict valid inputs
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host input")
    result = subprocess.run(['ping', '--', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}

try:
    from fastapi.exceptions import HTTPException
    app.exception_handler(HTTPException)(HTTPException.handle_exception)
except ImportError:
    pass