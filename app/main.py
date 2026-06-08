from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Use parameterized commands instead of string formatting
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    response = safe_ping(host)
    return {"status": "completed", "response": response}