import os
import shutil
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
from collections import Counter
from sklearn.model_selection import train_test_split

def create_directory(path):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def copy_images(source_folder, target_folder):
    """Copy all images from the source folder to the target folder."""
    if os.path.exists(source_folder):
        for file_name in os.listdir(source_folder):
            if file_name.endswith('.png'):
                source_file = os.path.join(source_folder, file_name)
                target_file = os.path.join(target_folder, file_name)
                shutil.copy2(source_file, target_file)

def analyze_folder(folder_path):
    """Analyze a folder: count images, sizes, etc."""
    image_sizes = []
    file_counts = Counter()

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.png'):
                file_counts[root] += 1
                image_path = os.path.join(root, file)
                try:
                    with Image.open(image_path) as img:
                        image_sizes.append(img.size)
                except Exception as e:
                    print(f"Error reading image {image_path}: {e}")

    return file_counts, image_sizes

def plot_image_size_distribution(image_sizes):
    """Plot the distribution of image sizes."""
    widths, heights = zip(*image_sizes)
    plt.figure(figsize=(12, 6))
    sns.histplot(widths, kde=True, color='blue', label='Width')
    sns.histplot(heights, kde=True, color='orange', label='Height')
    plt.xlabel('Pixels')
    plt.ylabel('Frequency')
    plt.title('Image Size Distribution')
    plt.legend()
    plt.show()

def eda():
    """Perform exploratory data analysis on the dataset."""
    print("Analyzing Recyclable Folder...")
    recyclable_counts, recyclable_sizes = analyze_folder(RECYCLABLE_FOLDER)
    print("Recyclable counts by folder:", recyclable_counts)

    print("Analyzing Household Waste Folder...")
    household_counts, household_sizes = analyze_folder(HOUSEHOLDWASTE_FOLDER)
    print("Household waste counts by folder:", household_counts)

    print("Plotting image size distribution for Recyclable...")
    plot_image_size_distribution(recyclable_sizes)

    print("Plotting image size distribution for Household Waste...")
    plot_image_size_distribution(household_sizes)

def split_dataset(source_folder, train_folder, val_folder, test_folder, test_size=0.15, val_size=0.15):
    """Split the dataset into train, validation, and test sets."""
    categories = os.listdir(source_folder)
    for category in categories:
        category_path = os.path.join(source_folder, category)
        if not os.path.isdir(category_path):
            continue

        images = [os.path.join(category_path, img) for img in os.listdir(category_path) if img.endswith('.png')]
        print(f"Found {len(images)} images in category: {category}")

        if len(images) == 0:
            print(f"No images found in {category}. Skipping...")
            continue

        # Split into train, val, and test
        train_imgs, temp_imgs = train_test_split(images, test_size=(test_size + val_size), random_state=42)
        val_imgs, test_imgs = train_test_split(temp_imgs, test_size=test_size / (test_size + val_size), random_state=42)

        # Helper function to copy files to target folders
        def copy_files(file_list, target_folder, category_name):
            target_category_path = os.path.join(target_folder, category_name)
            os.makedirs(target_category_path, exist_ok=True)
            for img_path in file_list:
                shutil.copy(img_path, target_category_path)

        # Copy images into respective folders
        copy_files(train_imgs, train_folder, category)
        copy_files(val_imgs, val_folder, category)
        copy_files(test_imgs, test_folder, category)
