import os

def collect_images(image_directory):
    """
    Collects all image file paths from a given directory.

    Args:
        image_directory (str): Path to the image directory.

    Returns:
        list: List of image file paths.
    """
    image_paths = []
    for root, dirs, files in os.walk(image_directory):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                image_paths.append(os.path.join(root, file))
    return image_paths

def create_directory(directory):
    """
    Creates a directory if it doesn't exist.

    Args:
        directory (str): Path of the directory to create.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
