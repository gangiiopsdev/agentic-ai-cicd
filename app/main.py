from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    if not input_string.strip().isalnum() or len(input_string) > 255:
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not sanitize_input(host):
        return {
            "status": "failed",
            "error": "Invalid host name"
        }
    try:
        result = subprocess.run(shlex.split(f"ping {host}"), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": e.stderr
        }