from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input before passing to subprocess
    host = subprocess.quote(host)
    subprocess.run(['ping', host], check=True)