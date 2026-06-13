from fastapi import FastAPI
import subprocess
git = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = git.communicate()
return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}