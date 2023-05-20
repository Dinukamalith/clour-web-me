import os
import requests

def colorize_photo(photo_path):
    # Load the photo into memory.
    with open(photo_path, "rb") as f:
        image_data = f.read()

    # Request the colorized photo from the API.
    url = "https://api.hotpot.ai/colorize"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY"
    }
    response = requests.post(url, headers=headers, data=image_data)

    # Save the colorized photo to disk.
    if response.status_code == 200:
        colorized_photo_path = os.path.join("/tmp", "colorized_photo.jpg")
        with open(colorized_photo_path, "wb") as f:
            f.write(response.content)

    return colorized_photo_path

if __name__ == "__main__":
    # Get the photo path from the user.
    photo_path = input("Enter the path to the photo you want to colorize: ")

    # Colorize the photo.
    colorized_photo_path = colorize_photo(photo_path)

    # Display the colorized photo.
    from PIL import Image
    image = Image.open(colorized_photo_path)
    image.show()
