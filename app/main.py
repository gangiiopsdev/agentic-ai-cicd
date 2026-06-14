from fastapi import FastAPI
import subprocess
cimport socket
cimport ipaddress

app = FastAPI()

def is_valid_ip(ip):
    try:
        return ipaddress.ip_address(ip)
    except ValueError:
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_ip(host) and not socket.gethostbyname_ex(host)[0]:
        return {"error": "Invalid host"}

    try:
        output = subprocess.run(["ping", host], capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"error": str(e)}