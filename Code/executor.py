from concurrent.futures import ProcessPoolExecutor  # For parallel execution
import time  # For tracking elapsed time

class ImageProcessingExecutor:
    """
    Manages sequential and parallel execution of image processing tasks.
    """

    def __init__(self, processor):
        """
        Initializes the executor with an ImageProcessor instance.
        
        Args:
            processor (ImageProcessor): Instance of ImageProcessor.
        """
        self.processor = processor

    def sequential_processing(self, image_paths):
        """
        Processes images sequentially and measures execution time.

        Args:
            image_paths (list): List of image file paths.

        Returns:
            float: Time taken for sequential processing in minutes.
        """
        start_time = time.time()  # Record the start time
        for image_path in image_paths:  # Loop through each image path
            self.processor.apply_filters(image_path)  # Apply filters to the image
        end_time = time.time()  # Record the end time
        return (end_time - start_time) / 60  # Convert elapsed time to minutes

    def parallel_processing(self, image_paths, num_processes=4):
        """
        Processes images in parallel using multiple processes and measures execution time.

        Args:
            image_paths (list): List of image file paths.
            num_processes (int): Number of processes to use.

        Returns:
            float: Time taken for parallel processing in minutes.
        """
        start_time = time.time()  # Record the start time
        with ProcessPoolExecutor(max_workers=num_processes) as executor:  # Create a process pool
            executor.map(self.processor.apply_filters, image_paths)  # Distribute tasks among processes
        end_time = time.time()  # Record the end time
        return (end_time - start_time) / 60  # Convert elapsed time to minutes
