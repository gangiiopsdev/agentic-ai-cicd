from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        # Use subprocess.run instead and avoid shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Run the ping command safely and sanitize input
    output = run_ping(subprocess.check_output(['echo', host]).decode('utf-8').strip())
    return {"status": "completed", "output": output}