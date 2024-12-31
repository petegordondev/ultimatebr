import os
import glob

# Recursively delete migration files except __init__.py
for file in glob.glob('*/migrations/*.py', recursive=True):
    if not file.endswith('__init__.py'):
        os.remove(file)
        
for file in glob.glob('*/migrations/*.pyc', recursive=True):
    os.remove(file)
