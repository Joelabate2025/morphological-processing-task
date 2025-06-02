import numpy as np
import multiprocessing
from functools import partial
from scipy.ndimage import binary_erosion, binary_dilation
import matplotlib.pyplot as plt

def generate_test_images(n=5, shape=(10, 10)):
    return [np.random.randint(0, 2, size=shape).astype(int) for _ in range(n)]

def morphological_operation(image, kernel_size, operation='erosion'):
    structure = np.ones((kernel_size, kernel_size), dtype=bool)
    if operation == 'erosion':
        return binary_erosion(image, structure=structure).astype(int)
    elif operation == 'dilation':
        return binary_dilation(image, structure=structure).astype(int)
    else:
        raise ValueError("Operation must be 'erosion' or 'dilation'")

def process_collection(images, kernel_size=3, operation='erosion'):
    with multiprocessing.Pool() as pool:
        func = partial(morphological_operation, kernel_size=kernel_size, operation=operation)
        return pool.map(func, images)

def visualize_images(original, eroded, dilated):
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    axes[0].imshow(original, cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    axes[1].imshow(eroded, cmap='gray')
    axes[1].set_title('Eroded Image')
    axes[1].axis('off')

    axes[2].imshow(dilated, cmap='gray')
    axes[2].set_title('Dilated Image')
    axes[2].axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_images = generate_test_images(n=5, shape=(10, 10))
    eroded_images = process_collection(test_images, kernel_size=3, operation='erosion')
    dilated_images = process_collection(test_images, kernel_size=3, operation='dilation')
    visualize_images(test_images[0], eroded_images[0], dilated_images[0])
    print("Original Image:\n", test_images[0])
    print("\nEroded Image:\n", eroded_images[0])
    print("\nDilated Image:\n", dilated_images[0])
