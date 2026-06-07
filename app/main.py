from fastapi import FastAPI
import subprocess
cimport subprocess
cdef is_valid_host(host):
    return all(c.isalnum() or c in ('.', '-', '_') for c in host)

cdef ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host name")
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}