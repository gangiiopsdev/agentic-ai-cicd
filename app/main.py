from fastapi import FastAPI
import subprocess

def sanitize_input(input_string):
    return subprocess.list2cmdline([input_string])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        output = subprocess.run(['ping', '-c 1'] + [sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}