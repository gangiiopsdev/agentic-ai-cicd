from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return shlex.quote(input_string)

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    result = subprocess.run(["ping", safe_host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}