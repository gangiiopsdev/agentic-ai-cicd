from fastapi import FastAPI
import subprocess
host = 'example.com'  # Replace with actual host
ping_command = ['ping', host]
git = subprocess.Popen(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = git.communicate()
return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}