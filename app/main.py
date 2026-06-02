from fastapi import FastAPI
import subprocess
import shlex
class Sanitizer:
    @staticmethod
def sanitize_input(input_str):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        return ''.join(filter(lambda x: x in allowed_chars, input_str))
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = Sanitizer.sanitize_input(host)
    command = ['ping', shlex.quote(sanitized_host)]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed", "output": result.stderr}