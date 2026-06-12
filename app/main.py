from fastapi import FastAPI
import subprocess
git clone https://github.com/your-username/your-repo.git
# Add your secure implementation here
app = FastAPI()

def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)