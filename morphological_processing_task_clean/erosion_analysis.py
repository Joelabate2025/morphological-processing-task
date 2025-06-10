import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

# Loading control arm image
image_path = r"C:\Users\Administrator\Desktop\3D CAD model of control rm.jpg"
img = cv2.imread(image_path)

if img is None:
    raise FileNotFoundError("Check if the image exists and path is correct.")

# Converting the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Applying threshold
_, binary_mask = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
binary = (binary_mask // 255).astype(np.uint8)

# Defining erosion function

def apply_erosion(binary_img, kernel_size, repetitions=100):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    import time
    start = time.perf_counter()
    for _ in range(repetitions):
        eroded = cv2.erode(binary_img * 255, kernel, iterations=1)
    end = time.perf_counter()
    avg_time_ms = ((end - start) / repetitions) * 1000
    return eroded, avg_time_ms


# Applying erosion with different kernels
results = {}
for k in [3, 5, 7]:
    eroded_img, t_ms = apply_erosion(binary, k)
    results[k] = {"image": eroded_img, "time_ms": t_ms}

# Plot results side by side
fig, axs = plt.subplots(1, 4, figsize=(18, 5))
axs[0].imshow(binary, cmap='gray')
axs[0].set_title("Original Binary Mask")
axs[0].axis("off")

for idx, k in enumerate([3, 5, 7]):
    axs[idx + 1].imshow(results[k]["image"], cmap='gray')
    axs[idx + 1].set_title(f"Eroded (Kernel {k}x{k})\nTime: {results[k]['time_ms']:.4f} ms")
    axs[idx + 1].axis("off")

plt.tight_layout()
plt.show()
