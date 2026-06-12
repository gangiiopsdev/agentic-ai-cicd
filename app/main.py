from fastapi import FastAPI
def ping(host: str):
    # Sanitize input using a whitelist approach
    allowed_hosts = ['google.com', 'example.com']
    if host in allowed_hosts:
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        return {'status': 'error', 'message': 'Invalid host'}