#plan : prendre une image
import argparse
import os
import mimetypes


def get_image_info(image_path):
    # Vérifier si le fichier existe
    if not os.path.isfile(image_path):
        return None, "File does not exist."

    # Obtenir la taille du fichier en octets
    file_size = os.path.getsize(image_path)

    # Obtenir le type MIME du fichier
    mime_type, _ = mimetypes.guess_type(image_path)

    return {
        "file_size": file_size,
        "mime_type": mime_type,
    }, None



def main():
    # Configuration de l'argument parser
    parser = argparse.ArgumentParser(description='Process an image.')
    parser.add_argument('image_path', type=str, help='Path to the image file')
    args = parser.parse_args()

    # Obtenir des informations sur l'image
    info, error = get_image_info(args.image_path)
    if error:
        print(f"Failed to process image {args.image_path}. Error: {error}")
    else:
        print(f"Image {args.image_path} successfully processed.")
        print(f"File size: {info['file_size']} bytes")
        print(f"MIME type: {info['mime_type']}")

    # fonction pour découper une image en "x carré"

    # determine la couleur majoritaire dans le bout d'image


if __name__ == "__main__":
    main()
