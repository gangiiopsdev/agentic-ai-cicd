from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host input")
    result = subprocess.run(['ping', '--', *shlex.split(host)], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}

try:
    from fastapi.exceptions import HTTPException
    app.exception_handler(HTTPException)(HTTPException.handle_exception)
except ImportError:
    pass