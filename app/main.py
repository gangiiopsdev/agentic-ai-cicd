from fastapi import FastAPI
import subprocess
import shlex

class InputSanitizer:
    @staticmethod
def sanitize_input(input_string):
        return shlex.quote(input_string)

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run instead of subprocess.call for better security
    sanitized_host = InputSanitizer.sanitize_input(host)
    command = ['ping', sanitized_host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}