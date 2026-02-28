import os
import sys

def create_target_file(version_tag):
    """Generates a new Python file on the EC2 instance."""
    
    # Create a dynamic filename based on the matrix version
    filename = f"generated_script_{version_tag}.py"
    
    # The Python code we want to write inside the new file
    code_content = (
        f"# This file was automatically generated!\n"
        f"def main():\n"
        f"    print('Hello from EC2! Generated using Python {version_tag}')\n\n"
        f"if __name__ == '__main__':\n"
        f"    main()\n"
    )

    # Write the file to the current directory
    with open(filename, 'w') as f:
        f.write(code_content)
        
    print(f"Success: {filename} has been created on the EC2 instance.")

if __name__ == "__main__":
    # Grab the python version from the command line arguments
    version_arg = sys.argv[1] if len(sys.argv) > 1 else "default"
    create_target_file(version_arg)
