from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    if not isinstance(input_string, str) or not all(c.isalnum() for c in input_string):  # Simplified check for alphanumeric characters only
        raise ValueError("Invalid input")

@app.get="/ping")
def ping(host: str):
    try:
        sanitize_input(host)
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as e:
        return {"status": "invalid", "error": str(e)}