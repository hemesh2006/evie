import subprocessf

# List of Python scripts to run
scripts = [r"components\text_overlay.py", r"components\gif_overlay.py",r"components\image_overlay.py"]

# Start each script in a new process
processes = []
for script in scripts:
    process = subprocess.Popen(["python", script])
    processes.append(process)

# Wait for all processes to complete
for process in processes:
    process.wait()

print("All scripts have finished execution.")
