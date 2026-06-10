from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    run_ping(host)
    return {"status": "completed"}

# Define a function to validate the host input
def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific domains or IP addresses
    return True