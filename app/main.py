from fastapi import FastAPI
import subprocess
get_ip = lambda x: subprocess.run(['ping', '-c', '1', x], stdout=subprocess.PIPE).stdout.decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or len(host) > 50:
        raise ValueError("Invalid input")
    result = get_ip(host)
    return {'status': 'completed', 'result': result}