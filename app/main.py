from fastapi import FastAPI
import subprocess
def _ping(host):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
def ping(host: str):
    # Secure implementation
    if not valid_host(host):
        raise ValueError("Invalid host")
    output = _ping(host)
    return {"status": "completed", "output": output}
def valid_host(host):\n    allowed_hosts = ['example.com', 'test.example.com']  # Replace with actual validation logic\n    return host in allowed_hosts