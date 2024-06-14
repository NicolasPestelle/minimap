import os
from PIL import Image


def reassemble_image(output_image_path):
    # Supposer que chaque morceau a la même taille
    chunk_path = 'testDécoupe/chunk_0_0.png'
    chunk = Image.open(chunk_path)
    chunk_width, chunk_height = chunk.size

    # Créer une nouvelle image vide de la taille originale
    new_image = Image.new('RGB', (chunk_width * 10, chunk_height * 10))

    # Reconstituer l'image complète
    for i in range(10):
        for j in range(10):
            chunk_filename = os.path.join('testDécoupe', f'chunk_{i}_{j}.png')
            chunk = Image.open(chunk_filename)
            new_image.paste(chunk, (j * chunk_width, i * chunk_height))

    # Sauvegarder l'image reconstituée
    new_image.save(output_image_path)
    print(f"Image reassembled successfully and saved to {output_image_path}.")


def main():
    # Reconstituer l'image à partir des morceaux
    reassemble_image('testRegroupe/reassembled_image.png')


if __name__ == "__main__":
    main()

    # Dictionnaire pour associer les noms de couleurs aux codes des slabs
    slab_codes = {
        "Vert": "```H4sIAAAAAAAACjv369xFJgYmBgYGgUWHGX9Pme/S4z7T7pZdoRonUKwpbKfGFZWDHuscjn5QYTm5kQsoNoERSEhC6AYeKB8ITjBAxEE0SPwEAxKQhFAgcRhwZDjA8IGNgUGE6QCDASsDgyyQLlBkYPjMeIBhAl8D43YgvUG8gTECxOdqYLwLVF/A3sBYAKQdhBoYxYDiDRINjM1A/gEZkIkAp3hUUcwAAAA=```\n",
        "Vert foncé": "H4sIAAAAAAACAyWSa0iTURiA39ezVdYaX94WUTFnpGamAylrqd9ic4mXSaI5TJFICyyaZDUvxWdoTF06vIQjmWyZFPpDa0IJ4mcZCYZOspRIHWYR9KP1wz8rsXPyz3nO+5z3XN8zE5iZC4IwAODcb/BPZ6/OZnCkfk6tPCyhbjljNszpmNb2K2p39XDDfUhd83W98uezBV1P7VKFqljawtyPQWPC3dij6Y1ue/R20VTFXMmxA6dGV1yZnp3nDXN159aZS3bfKXyy5DK+jPDsm1zxdTNHrqaVyroMOT17bJkOU3wtc7a21bJW58bZgXHrysh8cglzI+XOClvcbFafL29waNF9Q8bOV/bCHJu1P7NV6mlu0XwKBFEnU83XWH41Gbus363TBr6NzdUffCCUPyzSenJM9z/m1z9mTsKjPX9zwzgQFjUhWBNimPv6VtOuf5rGdyyR4rHoi9XsDWZcnc87V6O0jeqC6uyxhQiWN1dYMf7BWaV1DnhV8U231pibWH632PTKqBUiT07/Vq9xzI1q8ny5cpeuIzymSN/ecJy52wHrevLgI51dJ1mVTKpE5pQnijeH+cCZ+m5Yfp+SUsjcFEzSVqDdLbJYkG3FjNmsZtsANGBBLlSESLShMlSUNsAl5MNF6AcbAsdLG9GMXpoXB6fRGwyS16BEMRTgG6UvAogDOEwMAXKPUpQDyaA0y4B0U/qDgVQhh3bKy5QCzbvGxoOARFOCHMDJ4h0AajruQyBH6P5+erYQuIJeAqBAymBRmosX0M+JkAFTWLpXwJt4CId2A6lEHfpoMWsoE+m6DRDzPyaYRPxyXpIOf1GQAiShBe30o/ZCHXK0MAX03l6FACXwBUsVdEP4B1yl+1zMAgAA\n",
        "Bleu": "```H4sIAAAAAAAACjv369xFJgZGBgaGjjPdlSann3l2zXo342iRSDonUGwCSEISQjfwQPlAcIIBIg6iQeInGJCAJIQCiSMAAKYeWxFoAAAA```\n",
        "Bleu foncé": "```H4sIAAAAAAAACk3SsUoDURCF4dkUAcFKbIKFLzCl9luat7AYsNdC7CwlAZlCRHwQaxvhghKxt7a0SmXlzp4/0VvkkJlvCfdkVz+rj4lNzOzmbXl19Po1Xzx+P7yc75/tDLPF7f3n00E/X172xxfvp3cnwyy74WOmvN7l+3CaaV5Z82b/zkxR881Zd9n1h8raVz7vKcuN+yn78XflE5/4xCc+8Y53vOMd73jHN5Ov1D3kK3Uf+caNAx/4wAc+8LFtSN7whje84TeNrrtm6qeZ+mmmfpqpn2E/ZT8+JZ/4xCc+8Yl3vOMd73jHO76ZfKX6ka9UP/KNfz7wgQ984AMf2zdF3vCGN7zh/96sX7RLngS8AgAA```\n",
        "Rouge": "```H4sIAAAAAAAACjv369xFJgZGBgYG8fu/vSf3bPJY++PTakvhOG5OoNgEkIQkhG7ggfKB4AQDRBxEg8RPMCABSQgFEkcAAKk4XpFoAAAA```\n",
        "Rouge foncé": "```H4sIAAAAAAAACjv369xFJgZmBgYG8fu/vSf3bPJY++PTakvhOG5OoFiGwp+zz74scJpWdHbmfzFVTiagmFjJ0k+vDq53n/NomZiUslksI1BsAoiQhNANPFA+EJxggIiDaJD4CQYkIAmhQOIwwM94guED0OKLQPoCkD4M1LFABiQDAEOGJb6oAAAA```\n",
        "Gris": "```H4sIAAAAAAAACk2RP2hTURSHfzf3UY2mzf8mqWCjiEXo0NFBMCBGBYcILjpICg/cNCA4ORwKooPIw6VgQSLBUQkOWlCkg8MrYkl00yVddBKCPFAExd/xncG3fJxzvnPuufft/NoZZ5ABsLR+8PSN18vte+0LR+982e21mdu+euL2/drzcxs3f/zMoTs4wtxZV5jpFYGL7m7QKgMbZDMvwRI5nJWgonFRgivuvC9UJHiAGL0GkHWb6C2Iu0yiIe4lNjXvX5Ar1ZSYgx+Q3X3wHzW/B/63xln4Ovsi5o9pfwG+ovPY90fr8/D7GffL8JfILilkh3xGDovwbzTm/Fsac94qKXvhH7r0vLH2k5/JKfvekc069yJHCzxH/Rr30T3y8N91D/rXbN6YexRy8H3dZ5bnkxN6T4HMFuO3pND/RjbJww4ZPfeMcc2l+VdklJXgPTnle47IlbIE22SvLsF1ZQ04Tvbn9V05l/GIcyfkE7JbBT6QnZK4A9pf0nenT67zv0yr4h6Rw6K4x+QkL25AYk7cGtnPiVslO+RJ9XmvRfVIaB/5FazzXp/IVkGCXXJSkuAQ603+91M6j8R/X2smpeRSbpWs0LD6IhBaKjQ/ND80PzQ/ND82PzY/Nj82PzY/Nn/Zpb5SfaX6SvX/1RtWpx+ZH5kfmR+ZH5kfmZ+Yn5ifmJ+Yn5ifmA/8BSIexDGEAwAA```\n",
        "Gris clair": "```H4sIAAAAAAAACjv369xFJgZGBgaGNuWqSddSZjltrmjaz6rFexkkhgAA6ChE2CgAAAA=```\n"
        # Ajouter d'autres couleurs et leurs codes de slabs ici
    }