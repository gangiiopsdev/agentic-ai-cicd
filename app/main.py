from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = ''.join(filter(str.isalnum, host))
    args = ['ping', safe_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout