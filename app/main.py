from fastapi import FastAPI
import subprocess
cmd = ['ping', host]
# Secure implementation
result = subprocess.run(cmd, capture_output=True, text=True, check=True)
return result.stdout