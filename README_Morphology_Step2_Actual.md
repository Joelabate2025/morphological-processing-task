
# Morphological Erosion on Control Arm (Step 2)

This demonstration applies a custom morphological erosion method to a binary mask of an automotive control arm component. The image was preprocessed into a binary mask and eroded with three different kernel sizes.

## 🔍 Visual Results

- **3x3 Kernel**: Mild edge thinning.
- **5x5 Kernel**: Noticeable feature erosion.
- **7x7 Kernel**: Aggressive thinning, simulating material loss.

## 📊 Updated Performance Summary

| Kernel Size | Execution Time (ms) |
|-------------|---------------------|
| 3x3         | 0.92                |
| 5x5         | 1.05                |
| 7x7         | 0.87                |

## 🧩 Application Context

This method supports post-processing in lightweight structure design, particularly for robustness evaluation in the presence of manufacturing tolerances.

> Prepared for Prof. Michal Nowak as part of Step 2 evaluation.
