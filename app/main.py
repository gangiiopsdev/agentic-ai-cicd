from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Use a safe method to check reachability without shell=True
    response = subprocess.run(['ping', '-c', '1', sanitize_input(host)], capture_output=True, text=True)
    if response.returncode == 0:
        return {"status": "completed", "response": response.stdout}
    else:
        return {"status": "failed", "error": response.stderr}