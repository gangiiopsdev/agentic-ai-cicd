from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Basic sanitization: replace common shell metacharacters with an empty string
    return ''.join(char for char in input_str if char not in "'""	\n;`&|*?~<>^()[]{}$#%")

@app.get("/ping")
def ping(host: str):

    # Sanitize the host input to mitigate command injection
    sanitized_host = sanitize_input(host)

    # Use subprocess.run with shell=False and args parameter for safe execution
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=False)

    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }