import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

def read_image_pairs(split_file):
    # Read the file containing image paths
    with open(split_file, 'r') as f:
        lines = f.readlines()
    
    # Extract RGB and depth image paths
    image_pairs = []
    for line in lines:
        rgb_path, depth_path, our_path = line.strip().split()
        image_pairs.append((rgb_path, depth_path, our_path))
    
    return image_pairs

def read_image_pairs_from_folders(rgb_folder, depth_folder, our_folder):
    # Get all image files from RGB folder
    rgb_files = sorted([f for f in os.listdir(rgb_folder) if f.endswith(('.png', '.jpg', '.jpeg'))])
    
    # Create corresponding paths for depth and our folders
    image_pairs = []
    for rgb_file in rgb_files:
        rgb_path = os.path.join(rgb_folder, rgb_file)
        depth_path = os.path.join(depth_folder, rgb_file.replace('.jpg', '.png'))
        our_path = os.path.join(our_folder, rgb_file.replace('.jpg', '.png'))
        
        # Only add if all files exist
        if os.path.exists(depth_path) and os.path.exists(our_path):
            image_pairs.append((rgb_path, depth_path, our_path))
    
    return image_pairs

def plot_image_pairs(image_pairs, num_pairs=5):
    # Create a figure with num_pairs rows and 2 columns
    fig, axes = plt.subplots(num_pairs, 3, figsize=(12, 4*num_pairs))
    
    # Plot image pairs
    for idx, (rgb_path, depth_path, our_path) in enumerate(image_pairs[:num_pairs]):
        print(rgb_path, depth_path, our_path)
        # Read images
        rgb_img = cv2.imread(rgb_path)
        rgb_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2RGB)
        depth_img = cv2.imread(depth_path, cv2.IMREAD_GRAYSCALE)
        our_img = cv2.imread(our_path, cv2.IMREAD_GRAYSCALE)
        # Normalize depth image for visualization
        depth_img = (depth_img - depth_img.min()) / (depth_img.max() - depth_img.min())
        our_img = (our_img - our_img.min()) / (our_img.max() - our_img.min())
        # Plot RGB image
        axes[idx, 0].imshow(rgb_img)
        axes[idx, 0].set_title(f'RGB Image {idx+1}')
        axes[idx, 0].axis('off')
        
        # Plot depth image
        axes[idx, 1].imshow(depth_img, cmap='plasma')
        axes[idx, 1].set_title(f'Depth Anything V2 Depth Image {idx+1}')
        axes[idx, 1].axis('off')
        
        # Plot our depth image
        axes[idx, 2].imshow(our_img, cmap='plasma')
        axes[idx, 2].set_title(f'Our Depth Image {idx+1}')
        axes[idx, 2].axis('off')
    
    plt.tight_layout()
    plt.savefig('vkitti2_mb_samples_real.png')
    plt.close()

def main():
    # Path to your split file
    split_file = '/w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/splits/vkitti2-mb/test_infer_result.txt'
    
    # Read image pairs
    # image_pairs = read_image_pairs(split_file)
    rgb_folder = '/w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/samples/raw'
    depth_folder = '/w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/samples/dav2'
    our_folder = '/w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/samples/ours-last'
    image_pairs = read_image_pairs_from_folders(rgb_folder, depth_folder, our_folder)
    
    # Plot the first 5 pairs (you can change this number)
    plot_image_pairs(image_pairs, num_pairs=5)

if __name__ == "__main__":
    main()