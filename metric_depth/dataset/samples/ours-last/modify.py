import os
import numpy as np
from PIL import Image

# Directory containing depth maps
depth_map_dir = './archiev'  # current directory
save_dir = './'
increment_value = 10  # adjust this value as needed

# Process all png files in the directory
for filename in os.listdir(depth_map_dir):
    if filename.endswith('.png'):
        file_path = os.path.join(depth_map_dir, filename)
        
        # Read depth map
        depth_map = np.array(Image.open(file_path))
        
        # Add increment value and clip at 255
        modified_depth = np.clip(depth_map + increment_value, 0, 255)
        
        # Save modified depth map
        modified_depth_img = Image.fromarray(modified_depth.astype(np.uint8))
        modified_depth_img.save(os.path.join(save_dir, filename))
        
        print(f"Processed: {filename}")
