from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.strip().isalnum():
        raise ValueError('Invalid input')

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as e:
        return {"status": "invalid", "error": str(e)}