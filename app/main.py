from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not validate_input(host):
        raise ValueError("Invalid input")
    args = ['ping', host]
    return subprocess.run(args, check=True, shell=False)
def validate_input(input_str: str) -> bool:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    if not all(char in allowed_chars for char in input_str):
        return False
    return True
def escape_shell_arg(arg: str) -> str:
    import shlex
    return shlex.quote(arg)
app = FastAPI()
@app.get("/ping")
def ping(host: str):\n    try:\n        result = safe_ping(escape_shell_arg(host))\n        return {"status": "completed", "output": result.stdout}\n    except ValueError as e:\n        return {"error": str(e)}, 400