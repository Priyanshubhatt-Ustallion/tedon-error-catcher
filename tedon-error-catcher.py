import sys
import subprocess

# 1. Grab the target file from the terminal
target_file = sys.argv[1]
print(f"🕵️ IBM Bob Daemon watching: {target_file}...\n")

# 2. Run the target file and catch everything
result = subprocess.run(
    ["python", target_file], 
    capture_output=True, 
    text=True
)

# 3. CONDITIONAL LOGIC: Did it crash? 
if result.returncode != 0:
    print("🚨 CRASH DETECTED! Gathering context for IBM Bob...\n")
    
    # We grab the red error text from our invisible terminal
    capture_error = result.stderr
    
    # We open the file WITHOUT quotes so it uses our variable
    with open(target_file, "r") as file:
        broken_code = file.read()
        
    # We use curly brackets {} to inject our 3 pieces of data into the final prompt
    final_payload = f"Bob, please fix {target_file}.\n\n=== BROKEN CODE ===\n{broken_code}\n=== CRASH LOG ===\n{capture_error}"
    
    # Print the payload! (For the hackathon, we will send this to the API)
    print("=== FINAL PAYLOAD FOR AI ===")
    print(final_payload)
    print("============================")

else:
    print("✅ Script ran perfectly! No AI needed.")