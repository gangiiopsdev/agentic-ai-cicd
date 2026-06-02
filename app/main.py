from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Basic sanitization: check for prohibited characters
    if any(char in input_str for char in [';', '&', '|', '*', '(', ')', '<', '>']):
        raise ValueError('Invalid input')
    return input_str

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}