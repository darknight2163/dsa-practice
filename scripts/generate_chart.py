import os
import re

# Color codes
EASY_COLOR = "#2ea44f"   # Green
MEDIUM_COLOR = "#d97706"    # Orange
HARD_COLOR = "#dc2626"   # Red

CATEGORIES = [
    "Arrays", 
    "SlidingWindow", 
    "HashMap", 
    "String", 
    "BitManipulation", 
    "BinarySearch", 
    "Stack", 
    "Sorting+Greedy", 
    "LinkedList"
]

def scan_repository():
    stats = {cat: {"easy": 0, "medium": 0, "hard": 0} for cat in CATEGORIES}
    
    for cat in CATEGORIES:
        if not os.path.exists(cat):
            continue
        for root, _, files in os.walk(cat):
            for file in files:
                filename = file.lower()
                if filename.startswith("easy_"):
                    stats[cat]["easy"] += 1
                elif filename.startswith("med_") or filename.startswith("medium_"):
                    stats[cat]["medium"] += 1
                elif filename.startswith("hard_"):
                    stats[cat]["hard"] += 1

    return stats

def generate_svg(stats):
    width = 700
    row_height = 40
    header_height = 60
    height = header_height + (len(CATEGORIES) * row_height) + 30
    
    svg_lines = [
        f'',
        f'',
        f'DSA Topic Breakdown',
        # Legend
        f'',
        f'Easy',
        f'',
        f'Medium',
        f'',
        f'Hard'
    ]

    y = header_height + 10
    scale = 20  # Pixel width multiplier per problem solved

    for cat in CATEGORIES:
        e = stats[cat]["easy"]
        m = stats[cat]["medium"]
        h = stats[cat]["hard"]
        
        e_w, m_w, h_w = e * scale, m * scale, h * scale
        
        svg_lines.append(f'{cat}')
        
        start_x = 200
        if e > 0:
            svg_lines.append(f'')
            start_x += e_w + 2
        if m > 0:
            svg_lines.append(f'')
            start_x += m_w + 2
        if h > 0:
            svg_lines.append(f'')
            start_x += h_w + 2

        total = e + m + h
        svg_lines.append(f'{total}')
        
        y += row_height

    svg_lines.append('')
    
    os.makedirs("assets", exist_ok=True)
    with open("assets/progress.svg", "w") as f:
        f.write("\n".join(svg_lines))

if __name__ == "__main__":
    data = scan_repository()
    generate_svg(data)
