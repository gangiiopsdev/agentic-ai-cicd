from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        try:
            result = subprocess.run(command, check=True, capture_output=True, shell=False, *args, **kwargs)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return str(e.stderr.decode())

app = FastAPI()
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    command = ['ping', '-c', '1', safe_host]
    output = SafeSubprocess.run(command, shell=False)
    return {"status": "completed", "output": output}