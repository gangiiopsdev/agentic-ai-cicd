from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Simple sanitization example, may need further refinement for production use
    return ''.join(filter(lambda x: x.isalnum() or x in ('-', '.', ':'), input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation
    subprocess.call(f"ping {sanitized_host}", shell=True)

    return {"status": "completed"}