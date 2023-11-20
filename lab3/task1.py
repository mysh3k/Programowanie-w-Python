import os
import shutil

# Base directory containing folders with photos
base_directory = r'C:\Users\mateusz.rozycki\Desktop'

# Target directory where files will be copied
copy_directory = os.path.join(base_directory, 'copies')

# Create the "copies" directory if it doesn't exist
if not os.path.exists(copy_directory):
    os.makedirs(copy_directory)


# Function to copy files and generate a report
def copy_photos_and_generate_report(directory):
    with open(os.path.join(base_directory, 'report.txt'), 'a') as report:
        report.write(f'Folder: {directory}\n')
        i = 0
        for file in os.listdir(directory):
            if file.lower().endswith(('.jpg', '.png')):
                old_name = os.path.join(directory, file)
                new_name = os.path.join(copy_directory, f'{os.path.basename(directory)}_{i}.jpg')
                shutil.copy(old_name, new_name)
                report.write(f'{file} -> {os.path.basename(new_name)}\n')
                i += 1


# Iterate through folders in the base directory
for folder in os.listdir(base_directory):
    full_path = os.path.join(base_directory, folder)
    if os.path.isdir(full_path):
        copy_photos_and_generate_report(full_path)

print("Copying completed and a report has been generated.")
