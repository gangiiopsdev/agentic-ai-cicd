from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return subprocess.list2cmdline([input_str])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        output = subprocess.run(sanitized_host, capture_output=True, text=True, check=True, shell=False)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}