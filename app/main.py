from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # More comprehensive validation to prevent common malicious patterns
    forbidden_chars = [';', '&', '|', '<', '>', '`', '$', '\', '/', '*', '?', '~', '{', '}', '[', ']', '^']
    return all(char not in host for char in forbidden_chars)

@app.get("/ping")
def ping(host: str):
    try:
        # Validate host to ensure it does not contain malicious input
        if not is_valid_host(host):
            raise ValueError("Invalid host")
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}