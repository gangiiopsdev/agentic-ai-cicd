from fastapi import FastAPI
import subprocess
def run_safe_command(command, args):
    # Use subprocess.run instead of subprocess.call and avoid using shell=True
    return subprocess.run([command] + args, check=True)

cmd = 'ping'  # Replace with the correct command
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Run the ping command safely without shell=True
    try:
        subprocess.run([cmd, host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}