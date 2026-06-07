from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Secure implementation using subprocess.Popen with validation
    if host.strip() == '' or any(char in host for char in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`\'"):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = run_ping(host)
    return {"status": "completed", "output": output}