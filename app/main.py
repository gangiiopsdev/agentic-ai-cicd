from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Using subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Call the safe_ping function instead of using subprocess directly
    return {'status': 'completed', 'output': safe_ping(host)}