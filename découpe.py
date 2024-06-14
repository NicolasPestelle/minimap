import argparse
import os
from PIL import Image


def create_directories():
    if not os.path.exists('testDécoupe'):
        os.makedirs('testDécoupe')
    if not os.path.exists('testRegroupe'):
        os.makedirs('testRegroupe')


def split_image(image_path):
    # Ouvrir l'image
    image = Image.open(image_path)
    width, height = image.size

    # Dimensions de chaque morceau
    chunk_width = width // 10
    chunk_height = height // 10

    # Diviser l'image en morceaux de 10x10
    for i in range(10):
        for j in range(10):
            left = j * chunk_width
            upper = i * chunk_height
            right = (j + 1) * chunk_width
            lower = (i + 1) * chunk_height

            chunk = image.crop((left, upper, right, lower))
            chunk_filename = os.path.join('testDécoupe', f'chunk_{i}_{j}.png')
            chunk.save(chunk_filename)

    print("Image split into 100 chunks successfully.")


def main():
    # Configuration de l'argument parser
    parser = argparse.ArgumentParser(description='Process and split an image.')
    parser.add_argument('image_path', type=str, help='Path to the image file')
    args = parser.parse_args()

    # Créer les répertoires nécessaires
    create_directories()

    # Découper l'image en morceaux
    split_image(args.image_path)


if __name__ == "__main__":
    main()