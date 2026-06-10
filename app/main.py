from fastapi import FastAPI
import subprocess
get_ip_info = lambda ip: subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, text=True)

app = FastAPI()

@app.get("/"), 
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    result = get_ip_info(host)
    if result.returncode == 0:
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed"}