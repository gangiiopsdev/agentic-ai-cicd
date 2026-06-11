from fastapi import FastAPI
import subprocess
host = 'example.com'  # Assume this is safely provided elsewhere
ping_command = ['ping', host]
subprocess.run(ping_command, check=True)
return {'status': 'completed'}