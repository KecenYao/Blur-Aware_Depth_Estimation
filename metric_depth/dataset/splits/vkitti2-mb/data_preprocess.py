# with open('origion.txt', 'r') as f:
#     lines = f.readlines()

# with open('mb_dataset_depth_path.txt', 'w') as f:
#     for line in lines:
#         if line.strip():  # Skip empty lines
#             depth_path = line.strip().split()[1]  # Get first path before space
#             f.write(f"{depth_path}\n")

import os
import shutil

# Define the source file and the destination directory
source_file = '/w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/splits/vkitti2-mb/mb_dataset_depth_path.txt'
destination_dir = '/w/339/kecenyao/dataset/vKitti2-mb/depth_relative'

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Open the source file and process each line
with open(source_file, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        # Strip any leading/trailing whitespace from the line
        file_path = line.strip()
        
        # Skip empty lines
        if not file_path:
            continue
        
        # Define the new file name using the line number
        new_file_name = f"{line_number}.png"
        
        # Define the full path for the new file
        new_file_path = os.path.join(destination_dir, new_file_name)
        
        # Copy the file to the new location with the new name
        shutil.copy(file_path, new_file_path)

print("Files have been copied and renamed successfully.")

# import os

# # Define the directory to search and the output text file
# directory_to_search = '/w/339/kecenyao/dataset/vKitti2-mb/rgb'
# output_file = '/w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/splits/vkitti2/mb_dataset_rgb_path.txt'

# # Open the output file in write mode
# with open(output_file, 'w') as file:
#     # Walk through the directory
#     for root, dirs, files in os.walk(directory_to_search):
#         for name in files:
#             # Get the full path of the file
#             file_path = os.path.join(root, name)
#             # Write the file path to the output file
#             file.write(file_path + '\n')

# # print(f"All file paths have been written to {output_file}.")

# def transform_file(input_path, output_path):
#     with open(input_path, 'r') as f:
#         lines = f.readlines()
    
#     new_lines = []
#     for line in lines:
#         line = line.strip()
#         # Remove .jpg and get base path
#         base = line[:-4]
#         depth_path = line.replace('/rgb/', '/depth/').replace('.jpg', '.png')
        
#         # Add numbered suffixes
#         new_lines.append(f"{base}.jpg {depth_path}\n")
#         for i in range(1, 11):
#             new_lines.append(f"{base}-{i}.jpg {depth_path}\n")
    
#     with open(output_path, 'w') as f:
#         f.writelines(new_lines)

# transform_file('mb_dataset_rgb_path.txt', '/w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/splits/vkitti2-mb/mb_dataset_rgb_path_numbered.txt')

# Read the file
# import random
# with open('/w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/splits/vkitti2-mb/whole.txt', 'r') as file:
#     lines = file.readlines()

# # Print original length
# print(f"Original number of lines: {len(lines)}")

# # Remove any empty lines and strip whitespace
# lines = [line.strip() for line in lines if line.strip()]
# print(f"Number of non-empty lines: {len(lines)}")

# # Shuffle the lines
# random.shuffle(lines)

# # Write to a new file
# with open('/w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/splits/vkitti2-mb/whole_shuffled.txt', 'w') as file:
#     file.writelines(line + '\n' for line in lines)


# # Read the input file
# with open('/w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/splits/vkitti2-mb/test_infer.txt', 'r') as file:
#     lines = file.readlines()

# # Create output with three copies of each line
# output_lines = []
# for line in lines:
#     line = line.strip()  # Remove any trailing whitespace/newlines
#     line2 = line.replace('/w/339/kecenyao/dataset/vKitti2-mb/rgb/', '/w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/splits/vkitti2-mb/test_depthanythingv2/').replace('.jpg', '.png')
#     line3 = line.replace('/w/339/kecenyao/dataset/vKitti2-mb/rgb/', '/w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/splits/vkitti2-mb/test/').replace('.jpg', '.png')
#     output_lines.append(f"{line} {line2} {line3}\n")

# # Write to output file
# with open('test_infer_result.txt', 'w') as file:
#     file.writelines(output_lines)
