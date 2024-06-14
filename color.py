from collections import defaultdict

import webcolors
from PIL import Image
import os
import sys
import json

# Dictionnaire pour associer les noms de couleurs aux codes des slabs
slab_codes = {
    "Vert": "```H4sIAAAAAAAACjv369xFJgYmBgYGgUWHGX9Pme/S4z7T7pZdoRonUKwpbKfGFZWDHuscjn5QYTm5kQsoNoERSEhC6AYeKB8ITjBAxEE0SPwEAxKQhFAgcRhwZDjA8IGNgUGE6QCDASsDgyyQLlBkYPjMeIBhAl8D43YgvUG8gTECxOdqYLwLVF/A3sBYAKQdhBoYxYDiDRINjM1A/gEZkIkAp3hUUcwAAAA=```",
        "Vert foncé": "H4sIAAAAAAACAyWSa0iTURiA39ezVdYaX94WUTFnpGamAylrqd9ic4mXSaI5TJFICyyaZDUvxWdoTF06vIQjmWyZFPpDa0IJ4mcZCYZOspRIHWYR9KP1wz8rsXPyz3nO+5z3XN8zE5iZC4IwAODcb/BPZ6/OZnCkfk6tPCyhbjljNszpmNb2K2p39XDDfUhd83W98uezBV1P7VKFqljawtyPQWPC3dij6Y1ue/R20VTFXMmxA6dGV1yZnp3nDXN159aZS3bfKXyy5DK+jPDsm1zxdTNHrqaVyroMOT17bJkOU3wtc7a21bJW58bZgXHrysh8cglzI+XOClvcbFafL29waNF9Q8bOV/bCHJu1P7NV6mlu0XwKBFEnU83XWH41Gbus363TBr6NzdUffCCUPyzSenJM9z/m1z9mTsKjPX9zwzgQFjUhWBNimPv6VtOuf5rGdyyR4rHoi9XsDWZcnc87V6O0jeqC6uyxhQiWN1dYMf7BWaV1DnhV8U231pibWH632PTKqBUiT07/Vq9xzI1q8ny5cpeuIzymSN/ecJy52wHrevLgI51dJ1mVTKpE5pQnijeH+cCZ+m5Yfp+SUsjcFEzSVqDdLbJYkG3FjNmsZtsANGBBLlSESLShMlSUNsAl5MNF6AcbAsdLG9GMXpoXB6fRGwyS16BEMRTgG6UvAogDOEwMAXKPUpQDyaA0y4B0U/qDgVQhh3bKy5QCzbvGxoOARFOCHMDJ4h0AajruQyBH6P5+erYQuIJeAqBAymBRmosX0M+JkAFTWLpXwJt4CId2A6lEHfpoMWsoE+m6DRDzPyaYRPxyXpIOf1GQAiShBe30o/ZCHXK0MAX03l6FACXwBUsVdEP4B1yl+1zMAgAA",
        "Bleu": "```H4sIAAAAAAAACjv369xFJgZGBgaGjjPdlSann3l2zXo342iRSDonUGwCSEISQjfwQPlAcIIBIg6iQeInGJCAJIQCiSMAAKYeWxFoAAAA```",
        "Bleu foncé": "```H4sIAAAAAAAACk3SsUoDURCF4dkUAcFKbIKFLzCl9luat7AYsNdC7CwlAZlCRHwQaxvhghKxt7a0SmXlzp4/0VvkkJlvCfdkVz+rj4lNzOzmbXl19Po1Xzx+P7yc75/tDLPF7f3n00E/X172xxfvp3cnwyy74WOmvN7l+3CaaV5Z82b/zkxR881Zd9n1h8raVz7vKcuN+yn78XflE5/4xCc+8Y53vOMd73jHN5Ov1D3kK3Uf+caNAx/4wAc+8LFtSN7whje84TeNrrtm6qeZ+mmmfpqpn2E/ZT8+JZ/4xCc+8Yl3vOMd73jHO76ZfKX6ka9UP/KNfz7wgQ984AMf2zdF3vCGN7zh/96sX7RLngS8AgAA```",
        "Rouge": "```H4sIAAAAAAAACjv369xFJgZGBgYG8fu/vSf3bPJY++PTakvhOG5OoNgEkIQkhG7ggfKB4AQDRBxEg8RPMCABSQgFEkcAAKk4XpFoAAAA```",
        "Rouge foncé": "```H4sIAAAAAAAACjv369xFJgZmBgYG8fu/vSf3bPJY++PTakvhOG5OoFiGwp+zz74scJpWdHbmfzFVTiagmFjJ0k+vDq53n/NomZiUslksI1BsAoiQhNANPFA+EJxggIiDaJD4CQYkIAmhQOIwwM94guED0OKLQPoCkD4M1LFABiQDAEOGJb6oAAAA```",
        "Gris": "```H4sIAAAAAAAACk2RP2hTURSHfzf3UY2mzf8mqWCjiEXo0NFBMCBGBYcILjpICg/cNCA4ORwKooPIw6VgQSLBUQkOWlCkg8MrYkl00yVddBKCPFAExd/xncG3fJxzvnPuufft/NoZZ5ABsLR+8PSN18vte+0LR+982e21mdu+euL2/drzcxs3f/zMoTs4wtxZV5jpFYGL7m7QKgMbZDMvwRI5nJWgonFRgivuvC9UJHiAGL0GkHWb6C2Iu0yiIe4lNjXvX5Ar1ZSYgx+Q3X3wHzW/B/63xln4Ovsi5o9pfwG+ovPY90fr8/D7GffL8JfILilkh3xGDovwbzTm/Fsac94qKXvhH7r0vLH2k5/JKfvekc069yJHCzxH/Rr30T3y8N91D/rXbN6YexRy8H3dZ5bnkxN6T4HMFuO3pND/RjbJww4ZPfeMcc2l+VdklJXgPTnle47IlbIE22SvLsF1ZQ04Tvbn9V05l/GIcyfkE7JbBT6QnZK4A9pf0nenT67zv0yr4h6Rw6K4x+QkL25AYk7cGtnPiVslO+RJ9XmvRfVIaB/5FazzXp/IVkGCXXJSkuAQ603+91M6j8R/X2smpeRSbpWs0LD6IhBaKjQ/ND80PzQ/ND82PzY/Nj82PzY/Nn/Zpb5SfaX6SvX/1RtWpx+ZH5kfmR+ZH5kfmZ+Yn5ifmJ+Yn5ifmA/8BSIexDGEAwAA```",
        "Gris clair": "```H4sIAAAAAAAACjv369xFJgZGBgaGNuWqSddSZjltrmjaz6rFexkkhgAA6ChE2CgAAAA=```"
}

def format_slab_data(slab_instructions):
    asset_data = defaultdict(lambda: {'instance_count': 0, 'instances': []})
    unique_asset_count = 0

    for instruction in slab_instructions:
        slab_name = instruction['slab']
        x = instruction['x']
        y = instruction['y']
        z = 0  # Supposons que z est toujours 0 dans notre cas
        degree = 0  # Supposons que la rotation est toujours 0 dans notre cas

        # Générer un UUID unique pour chaque combinaison de slab_name et (x, y, z, degree)
        uuid = f"{slab_name}_{x}_{y}_{z}_{degree}"

        # Ajouter l'instance au dictionnaire asset_data
        asset_data[uuid]['uuid'] = uuid
        asset_data[uuid]['instance_count'] += 1
        asset_data[uuid]['instances'].append({'x': x, 'y': y, 'z': z, 'degree': degree})

        unique_asset_count += 1

    formatted_data = {
        'unique_asset_count': unique_asset_count,
        'asset_data': list(asset_data.values())
    }

    return formatted_data

# Fonction pour obtenir un nom approximatif de la couleur
def get_approximate_color_name(rgb_tuple):
    try:
        color_name = webcolors.rgb_to_name(rgb_tuple, spec='css3')
    except ValueError:
        r, g, b = rgb_tuple
        max_value = max(r, g, b)
        min_value = min(r, g, b)
        if max_value == r:
            color_name = "Rouge" if r >= 200 else "Rouge foncé"
        elif max_value == g:
            color_name = "Vert" if g >= 200 else "Vert foncé"
        else:
            color_name = "Bleu" if b >= 200 else "Bleu foncé"
        if max_value - min_value < 50:
            color_name = "Gris" if max_value < 128 else "Gris clair"
    return color_name

# Vérifier si un argument a été fourni
if len(sys.argv) < 2:
    print("Veuillez fournir le chemin de l'image en argument.")
    sys.exit(1)

image_path = sys.argv[1]

# Charger l'image
image = Image.open(image_path)
width, height = image.size

# Créer le dossier de sortie s'il n'existe pas
if not os.path.exists("testDecoupe"):
    os.makedirs("testDecoupe")

# Découper l'image en 100 morceaux
piece_width = width // 10
piece_height = height // 10
slab_instructions = []
for i in range(10):
    for j in range(10):
        left = j * piece_width
        top = i * piece_height
        right = left + piece_width
        bottom = top + piece_height
        piece = image.crop((left, top, right, bottom))
        piece_path = os.path.join("testDecoupe", f"piece_{i}_{j}.jpg")
        piece.save(piece_path)

        # Calculer la couleur dominante
        colors = piece.getcolors(piece_width * piece_height)
        sorted_colors = sorted(colors, key=lambda x: x[0], reverse=True)
        dominant_color = sorted_colors[0][1]
        color_name = get_approximate_color_name(dominant_color)

        # Ajouter l'instruction de placement du slab au tableau JSON
        if color_name in slab_codes:
            slab_name = slab_codes[color_name]
        else:
            slab_name = "default"
        slab_instructions.append({"slab": slab_name, "x": j, "y": i})

# Écrire les instructions dans un fichier JSON
with open("slab_instructions.json", "w") as file:
    json.dump(format_slab_data(slab_instructions), file, indent=2)

print("Les instructions de placement des slabs ont été générées dans le fichier 'slab_instructions.json'.")
print("Vous pouvez maintenant utiliser SlabelFish pour générer le code Unity pour Talespire.")