from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_ping(host):
    try:
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Run the safe ping function
    output = run_safe_ping(host)
    return {"status": "completed", "output": output}