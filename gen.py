import matplotlib.pyplot as plt
import numpy as np
import os

def remove_vowels(name):
    vowels = 'AEIOUaeiou'
    return ''.join([letter for letter in name if letter not in vowels])

def letter_to_points(letter):
    base_points = {
        'A': [(0, 0), (1, 2), (2, 0), (1, 1)],
        'B': [(0, 0), (0, 2), (1, 2), (1, 1), (0, 1), (1, 1), (1, 0), (0, 0)],
        'C': [(1, 2), (0, 2), (0, 0), (1, 0)],
        'D': [(0, 0), (0, 2), (1, 2), (1, 0), (0, 0)],
        'F': [(1, 2), (0, 2), (0, 0), (0, 1), (1, 1)],
        'G': [(1, 2), (0, 2), (0, 0), (1, 0), (1, 1), (0, 1)],
        'H': [(0, 0), (0, 2), (0, 1), (1, 1), (1, 2), (1, 0)],
        'J': [(1, 2), (1, 0), (0, 0)],
        'K': [(0, 0), (0, 2), (0, 1), (1, 2), (0, 1), (1, 0)],
        'L': [(0, 2), (0, 0), (1, 0)],
        'M': [(0, 0), (0, 2), (1, 1), (2, 2), (2, 0)],
        'N': [(0, 0), (0, 2), (1, 1), (1, 0), (1, 2)],
        'P': [(0, 0), (0, 2), (1, 2), (1, 1), (0, 1)],
        'Q': [(1, 0), (0, 0), (0, 2), (1, 2), (1, 1), (0.5, 0.5), (1, 0)],
        'R': [(0, 0), (0, 2), (1, 2), (1, 1), (0, 1), (1, 0)],
        'S': [(1, 2), (0, 2), (0, 1), (1, 1), (1, 0), (0, 0)],
        'T': [(0, 2), (2, 2), (1, 2), (1, 0)],
        'V': [(0, 2), (1, 0), (2, 2)],
        'W': [(0, 2), (0.5, 0), (1, 1), (1.5, 0), (2, 2)],
        'X': [(0, 2), (2, 0), (1, 1), (0, 0), (2, 2)],
        'Y': [(0, 2), (1, 1), (2, 2), (1, 1), (1, 0)],
        'Z': [(0, 2), (2, 2), (0, 0), (2, 0)],
    }
    return base_points.get(letter.upper(), [])

def name_to_sigil(name, save_path):
    name_no_vowels = remove_vowels(name)
    points = []
    for letter in name_no_vowels:
        points.extend(letter_to_points(letter))
    
    if not points:
        return

    points = np.array(points)
    plt.figure(figsize=(6, 6))
    plt.plot(points[:, 0], points[:, 1], 'o-')
    plt.axis('equal')
    plt.axis('off')
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()

def process_monster_names(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as file:
        monster_names = file.read().splitlines()

    for name in monster_names:
        if name.strip():
            save_path = os.path.join(output_dir, f"{name.strip()}.png")
            name_to_sigil(name.strip(), save_path)

# Example usage:
input_file = 'monster_names.txt'  # The file containing monster names
output_dir = 'sigils'  # Directory where sigil images will be saved
process_monster_names(input_file, output_dir)
