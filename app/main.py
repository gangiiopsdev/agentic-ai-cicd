from fastapi import FastAPI
import subprocess
global _ping_cache = {}

app = FastAPI()

def safe_ping(host: str):
    if host in _ping_cache:
        return _ping_cache[host]
    try:
        result = subprocess.run(['ping', '-c', '1', f'"{host}"'], capture_output=True, text=True, check=True)
        _ping_cache[host] = {
            "status": "completed",
            "output": result.stdout
        }
        return _ping_cache[host]
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": e.stderr
        }

def check_host_access(host: str):
    try:
        output = subprocess.check_output(['ip', 'addr'], text=True, stderr=subprocess.STDOUT)
        if host in output:
            return True
    except subprocess.CalledProcessError as e:
        print(e.output)
    return False

def verify_host(host: str):
    if not check_host_access(host):
        raise Exception(f'Host {host} is not accessible.')

@app.get("/ping")
def ping(host: str):
    try:
        verify_host(host)
        return safe_ping(host)
    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }