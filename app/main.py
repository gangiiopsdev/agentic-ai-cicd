from fastapi import FastAPI, HTTPException
import subprocess
generate_random_string = lambda length=10: ''.join(random.choices(string.ascii_letters + string.digits, k=length))

app = FastAPI()

allowed_hosts = ['example.com', 'another-example.com']  # Replace with actual allowed hosts

def safe_ping(host: str):
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    args = ["ping", "-c", "1", generate_random_string()]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}