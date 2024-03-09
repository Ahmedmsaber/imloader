# main.py

from src.image_grabber import grab_images_from_webpage

if __name__ == "__main__":
    # Take the webpage URL as user input
    webpage_url = input("Enter the URL of the webpage containing images: ")

    # Ask the user for the folder name to save images
    folder_name = input("Enter the name of the folder to save images in (e.g., your-name-folder): ")

    # Specify the output folder
    output_folder = f"images/{folder_name}"

    
    grab_images_from_webpage(webpage_url, output_folder)

    print("Image scraping completed.")
