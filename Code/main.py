from utils import collect_images, create_directory  # Import utility functions
from image_processor import ImageProcessor  # Import ImageProcessor class
from executor import ImageProcessingExecutor  # Import executor class

if __name__ == "__main__":
    # Define input and output directories
    img_dir = "D:\Sem VII\Parallel and Distributed Computing\PDC_Project\Images"
    processed_dir = "processed"

    # Collect all image paths from the directory
    image_paths = collect_images(img_dir)

    # Create the processed directory if it doesn't exist
    create_directory(processed_dir)

    # Create an ImageProcessor object
    processor = ImageProcessor(output_directory=processed_dir)

    # Create an ImageProcessingExecutor object with the processor
    executor = ImageProcessingExecutor(processor)

    # Perform sequential processing
    print("Starting sequential processing...")
    sequential_time = executor.sequential_processing(image_paths)
    print(f"Sequential processing completed in {sequential_time:.2f} minutes")

    # Perform parallel processing
    print("Starting parallel processing...")
    parallel_time = executor.parallel_processing(image_paths)
    print(f"Parallel processing completed in {parallel_time:.2f} minutes")

    # Calculate and display speedup
    if parallel_time > 0:
        speedup = sequential_time / parallel_time
        print(f"Speedup: {speedup:.2f}x")
    else:
        print("Parallel time is zero; speedup cannot be calculated.")
