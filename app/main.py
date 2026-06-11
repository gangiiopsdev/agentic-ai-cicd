from fastapi import FastAPI
import socket
def safe_ping(host: str):
    try:
        ip = socket.gethostbyname(host)
        if ip not in ['192.168.1.1', '10.0.0.1']:
            return "Invalid host"
    except socket.gaierror:
        return "Invalid host"
    args = ['ping', '-c', '1', ip]  # Use '-c' option to limit the number of pings
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return result.stdout
def validate_host(host: str):
    if host in ['example.com', 'test.com']:
        return True
    return False@app.get('/')def home():
    return {"message": 'Agentic Self-Healing Pipeline'}@app.get('/ping')def ping(host: str):    if validate_host(host):
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    else:
        return {"status": "invalid host", "message": 'Host is not allowed'}