import subprocess

print("=== Running YOLOv5 on image ===")
subprocess.run(["python", "main.py"], check=True)

print("\n=== Extracting structured data with LLM ===")
subprocess.run(["python", "Part2.py"], check=True)

print("\n✅ All outputs saved in 'results' folder.")
