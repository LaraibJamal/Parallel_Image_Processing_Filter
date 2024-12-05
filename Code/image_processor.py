import os
from PIL import Image, ImageFilter  # Importing necessary modules for image processing.

class ImageProcessor:
    """
    A class for processing images by applying filters such as Gaussian Blur and Edge Detection.
    """

    def __init__(self, output_directory):
        """
        Initializes the ImageProcessor with an output directory.
        
        Args:
            output_directory (str): Directory to save processed images.
        """
        self.output_directory = output_directory

    def apply_filters(self, img_path):
        """
        Applies Gaussian Blur and Edge Detection filters to the given image and saves the results.

        Args:
            img_path (str): Path to the image file.

        Returns:
            str: Path of the processed image.
        """
        # Open the image file using the PIL Image module
        with Image.open(img_path) as img:
            # Apply a Gaussian Blur filter to the image
            blurred_img = img.filter(ImageFilter.GaussianBlur(15))

            # Apply an Edge Detection filter to the image
            edges_img = img.filter(ImageFilter.FIND_EDGES)

            # Extract the image file name from its path
            base_name = os.path.basename(img_path)

            # Define paths to save the processed images
            save_path_blur = os.path.join(self.output_directory, f"blurred_{base_name}")
            save_path_edges = os.path.join(self.output_directory, f"edges_{base_name}")

            # Save the blurred image
            blurred_img.save(save_path_blur)

            # Save the edge-detected image
            edges_img.save(save_path_edges)

        # Return the path of the processed image for reference
        return img_path
