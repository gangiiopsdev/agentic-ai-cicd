from fastapi import FastAPI
import subprocess
get_ip = lambda h: [i[4][0] for i in socket.getaddrinfo(h, None)][0]

app = FastAPI()

def is_safe_host(host):
    # Simple check for localhost and IP address
    return host in ['127.0.0.1', '::1', 'localhost'] or get_ip(host) in ['127.0.0.1', '::1']

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    subprocess.run(['ping', '-c', '1', get_ip(host)], check=True)
    return {"status": "completed"}