from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not validate_input(host):
        raise ValueError("Invalid input")
    args = ['ping', host]
    return subprocess.run(args, check=True)
def validate_input(input_str: str) -> bool:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    if not all(char in allowed_chars for char in input_str):
        return False
    return True
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "output": result.stdout}
    except ValueError as e:
        return {"error": str(e)}, 400