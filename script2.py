import os
import re

# Define the path to the _posts directory
posts_directory = '_posts'


def process_markdown_files(directory):
    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            print(f'Processing file: {file_path}')
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()

            # Prepare to update the permalink
            updated_content = []
            for line in content:
                # Check if the line contains the permalink
                if line.startswith('permalink:'):
                    # Update the permalink line
                    updated_line = 'permalink: /:year-:month-:day-:title\n'
                    updated_content.append(updated_line)
                    print(f'Updated permalink in {filename}')
                else:
                    updated_content.append(line)

            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(updated_content)


if __name__ == '__main__':
    process_markdown_files(posts_directory)
