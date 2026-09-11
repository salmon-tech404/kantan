"""
Kantanda Compiler Wrapper (Compatibility shim)
Delegates compilation to compile_kantanda.py
"""
import os
import subprocess
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(current_dir, "compile_kantanda.py")
res = subprocess.run([sys.executable, script_path] + sys.argv[1:])
sys.exit(res.returncode)
