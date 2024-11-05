import os
import re

# Define the directory containing the markdown files
input_directory = '_posts'


def count_iframes_in_markdown_files(directory):
    total_iframe_count = 0  # Initialize total count of iframes

    # Process each markdown file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.md'):  # Check for markdown files
            file_path = os.path.join(directory, filename)

            # Read the content of the markdown file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Use regex to find all <iframe> tags
            iframe_matches = re.findall(
                r'<iframe.*?>.*?</iframe>', content, re.DOTALL)
            # Count the number of iframes in the current file
            iframe_count = len(iframe_matches)
            total_iframe_count += iframe_count  # Add to total count

            print(f"Found {iframe_count} <iframe> tags in {filename}")

    print(f"\nTotal number of <iframe> tags across all files: {
          total_iframe_count}")


# Run the function
count_iframes_in_markdown_files(input_directory)
