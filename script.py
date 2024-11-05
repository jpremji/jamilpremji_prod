import os
import re
import requests


def download_image(image_url, save_folder):
    """
    Downloads an image from the specified URL and saves it to the given folder,
    using a modified filename based on the URL.

    :param image_url: The URL of the image to download.
    :param save_folder: The folder (including nested folders) where the image will be saved.
    """
    # Ensure the save folder and any necessary parent directories exist
    os.makedirs(save_folder, exist_ok=True)

    # Extract the part of the URL after 'uploads/'
    try:
        # Split the URL by 'uploads/' and take the second part
        file_path = image_url.split('uploads/', 1)[1]

        # Replace slashes with hyphens to create the new filename
        new_file_name = file_path.replace('/', '-')

        # Create the full save path
        save_path = os.path.join(save_folder, new_file_name)

        # Send a GET request to the image URL
        response = requests.get(image_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Save the image content to a file
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded successfully: {save_path}")
            return new_file_name  # Return the new filename for use in markdown
        else:
            print(f"Failed to retrieve image. Status code: {
                  response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def process_markdown_files(input_directory):
    """
    Processes all markdown files in the specified directory, downloading images and
    updating the markdown links accordingly.

    :param input_directory: The directory containing the markdown files to process.
    """
    save_folder = 'assets/images'  # Folder where images will be saved
    allowed_domain = 'jamilpremji.com'  # Domain to restrict downloads to

    # Process each markdown file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.md'):  # Check for markdown files
            file_path = os.path.join(input_directory, filename)

            # Read the content of the markdown file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Find all markdown image links
            markdown_image_pattern = r'!\[.*?\]\((https?://[^\s)]+)\)'
            matches = re.findall(markdown_image_pattern, content)

            for image_url in matches:
                # Check if the image URL is from the allowed domain
                if allowed_domain in image_url:
                    # Download the image and get the new filename
                    new_file_name = download_image(image_url, save_folder)

                    if new_file_name:
                        # Update the markdown link in the content
                        updated_link = f'![](assets/images/{new_file_name})'
                        content = content.replace(
                            f'![]({image_url})', updated_link)

            # Save the updated content back to the original markdown file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)

            print(f"Processed file: {filename}")


# Example usage
input_directory = '_posts'  # Directory containing markdown files
process_markdown_files(input_directory)
