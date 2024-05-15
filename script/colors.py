import re
import sys
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import Rectangle

def match_hex_colors(text):
    return list(set(re.findall(r'#[a-fA-F0-9]{6}\b', text)))

def display_colors(colors):
    num_colors = len(colors)
    fig, ax = plt.subplots(figsize=(10,2))
    for i, color in enumerate(colors):
        rect = Rectangle((i, 0), 1, 1, color=color)
        ax.add_patch(rect)
        ax.text(
            i+0.5, 0.5, color,
            ha='center', va='center',
            color='black',
            path_effects=[pe.withStroke(linewidth=3, foreground='white')]
        )
    ax.set_xlim(0, num_colors)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.show()

def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <text_file>')
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except:
        printf("Error")
        sys.exit(1)

    matched_colors = match_hex_colors(text)

    display_colors(matched_colors)

if __name__ == "__main__":
    main()
