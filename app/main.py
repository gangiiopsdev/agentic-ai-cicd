from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c if c.isalnum() else '_' for c in input_str)

@app.get("/ping")
def ping(host: str):

    # Sanitize the input to prevent command injection
    sanitized_host = sanitize_input(host)

    # Use subprocess.run with shell=False and check=True to mitigate risks
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}