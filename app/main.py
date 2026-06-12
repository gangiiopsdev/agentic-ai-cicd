from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command: list) -> str:
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to ensure it does not contain malicious characters
        if not all(c.isalnum() or c in '-.:@,_' for c in host):
            raise ValueError("Invalid host format")
        safe_host = shlex.quote(host)
        output = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}