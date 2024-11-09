import os
import re

# Define the directory and the domain to search for
posts_dir = "_posts"
domain_pattern = r"(https?://(?:www\.)?jamilpremji\.com[^\s]*)"

# Open or create the todo.txt file
with open("todo.txt", "w") as todo_file:
    # Walk through all files in the _posts directory
    for root, _, files in os.walk(posts_dir):
        for file in files:
            # Process only markdown files
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                flagged = False  # Track if the file contains a flagged link
                in_frontmatter = False  # Track if we're within the frontmatter section

                # Read the file line by line
                with open(file_path, "r") as f:
                    lines = f.readlines()

                    for i, line in enumerate(lines, start=1):
                        # Check for start and end of frontmatter
                        if line.strip() == "---":
                            in_frontmatter = not in_frontmatter
                            continue

                        # Only process lines outside of the frontmatter
                        if not in_frontmatter:
                            # Search for any link containing the domain in each line
                            matches = re.findall(domain_pattern, line)
                            if matches:
                                # Flag file as containing a link
                                if not flagged:
                                    todo_file.write(f"{file}:\n")
                                    flagged = True
                                # Write each match with line number to the todo.txt
                                for match in matches:
                                    todo_file.write(f"  Line {i}: {match}\n")

print("Script completed. Check todo.txt for flagged files and links.")
