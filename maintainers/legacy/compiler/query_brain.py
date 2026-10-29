"""
Kantanda Cognitive Query Wrapper (Compatibility shim)
Delegates querying to query_kantanda.py
"""
import os
import subprocess
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(current_dir, "query_kantanda.py")
res = subprocess.run([sys.executable, script_path] + sys.argv[1:])
sys.exit(res.returncode)
