from fastapi import FastAPI
import subprocess
git = subprocess.Popen(['ping', host], stdout=subprocess.PIPE)
output, _ = git.communicate()
return {'status': 'completed', 'output': output.decode('utf-8')}