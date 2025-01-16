import os
import shutil
import uuid

# Paths
#DATA_PATH = '/content/drive/My Drive/Colab Notebooks/recycling'
#DATASET_PATH = os.path.join(DATA_PATH, 'images', 'images')
#RECYCLABLE_FOLDER = os.path.join(DATA_PATH, 'recyclable')
#HOUSEHOLDWASTE_FOLDER = os.path.join(DATA_PATH, 'householdwaste')

# Category classification
'''
RECYCLABLE_CATEGORIES = [
    "aerosol_cans",
    "aluminum_food_cans",
    "aluminum_soda_cans",
    "cardboard_boxes",
    "cardboard_packaging",
    "glass_beverage_bottles",
    "glass_cosmetic_containers",
    "glass_food_jars",
    "magazines",
    "newspaper",
    "office_paper",
    "plastic_detergent_bottles",
    "plastic_food_containers",
    "plastic_soda_bottles",
    "plastic_water_bottles",
    "steel_food_cans"
]

HOUSEHOLDWASTE_CATEGORIES = [
    "clothing",
    "coffee_grounds",
    "disposable_plastic_cutlery",
    "eggshells",
    "food_waste",
    "paper_cups",
    "plastic_cup_lids",
    "plastic_shopping_bags",
    "plastic_straws",
    "plastic_trash_bags",
    "shoes",
    "styrofoam_cups",
    "styrofoam_food_containers",
    "tea_bags"
]
'''

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


def copy_images_with_unique_names(source_folder, target_folder, category_name):
    """Copy images from source to target folder with unique names."""
    if os.path.exists(source_folder):
        for file_name in os.listdir(source_folder):
            if file_name.endswith('.png'):
                source_file = os.path.join(source_folder, file_name)

                # Generate a unique name using category and UUID
                unique_name = f"{category_name}_{uuid.uuid4().hex[:8]}.png"
                target_file = os.path.join(target_folder, unique_name)

                shutil.copy2(source_file, target_file)


def organize_images(RECYCLABLE_FOLDER, HOUSEHOLDWASTE_FOLDER, DATASET_PATH, RECYCLABLE_CATEGORIES, HOUSEHOLDWASTE_CATEGORIES):
    """Organize images into recyclable and household waste folders."""
    # Create target directories
    create_directory(RECYCLABLE_FOLDER)
    create_directory(HOUSEHOLDWASTE_FOLDER)

    # Iterate through dataset folders
    for category in os.listdir(DATASET_PATH):
        category_path = os.path.join(DATASET_PATH, category)

        if not os.path.isdir(category_path):
            continue

        target_folder = None

        # Determine if the category is recyclable or household waste
        if category in RECYCLABLE_CATEGORIES:
            target_folder = RECYCLABLE_FOLDER
        elif category in HOUSEHOLDWASTE_CATEGORIES:
            target_folder = HOUSEHOLDWASTE_FOLDER

        real_world_path = os.path.join(category_path, 'real_world')
        default_path = os.path.join(category_path, 'default')

        if os.path.exists(real_world_path):
            print(f"Copying images from 'real_world' in {category} -> {target_folder}")
            copy_images_with_unique_names(real_world_path, target_folder, category)
        if os.path.exists(default_path):
            print(f"Copying images from 'default' in {category} -> {target_folder}")
            copy_images_with_unique_names(default_path, target_folder, category)
        

