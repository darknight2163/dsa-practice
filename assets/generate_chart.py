import os

EASY_COLOR = "#2ea44f"
MEDIUM_COLOR = "#d97706"
HARD_COLOR = "#dc2626"
TEXT_COLOR = "#24292f"
MUTED_COLOR = "#57606a"
TRACK_COLOR = "#e5e7eb"

CATEGORIES = [
    "arrays",
    "sliding-window",
    "hashmap",
    "string",
    "bit-manipulation",
    "binary-search",
    "stack",
    "sorting+greedy",
    "linked-list",
]


def scan_repository():
    stats = {cat: {"easy": 0, "medium": 0, "hard": 0} for cat in CATEGORIES}

    for cat in CATEGORIES:
        if not os.path.exists(cat):
            continue
        for _, _, files in os.walk(cat):
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
    header_height = 70
    footer_height = 20
    label_x = 20
    label_width = 160
    bar_x = label_x + label_width
    bar_area_width = width - bar_x - 60  # leave room for the total count label
    max_bar_width = 400

    max_total = max(
        (s["easy"] + s["medium"] + s["hard"] for s in stats.values()), default=0
    )
    max_total = max(max_total, 1)  # avoid divide-by-zero when repo is empty
    scale = min(max_bar_width, bar_area_width) / max_total

    height = header_height + (len(CATEGORIES) * row_height) + footer_height

    svg_lines = [
        f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        f'xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI, Helvetica, Arial, sans-serif">',
        f'<rect width="{width}" height="{height}" fill="#ffffff" />',
        f'<text x="{label_x}" y="28" font-size="18" font-weight="600" fill="{TEXT_COLOR}">'
        f'DSA Topic Breakdown</text>',
        # Legend
        f'<rect x="{width - 260}" y="16" width="12" height="12" rx="2" fill="{EASY_COLOR}" />',
        f'<text x="{width - 244}" y="26" font-size="12" fill="{MUTED_COLOR}">Easy</text>',
        f'<rect x="{width - 200}" y="16" width="12" height="12" rx="2" fill="{MEDIUM_COLOR}" />',
        f'<text x="{width - 184}" y="26" font-size="12" fill="{MUTED_COLOR}">Medium</text>',
        f'<rect x="{width - 120}" y="16" width="12" height="12" rx="2" fill="{HARD_COLOR}" />',
        f'<text x="{width - 104}" y="26" font-size="12" fill="{MUTED_COLOR}">Hard</text>',
    ]

    y = header_height
    bar_height = 16

    for cat in CATEGORIES:
        e = stats[cat]["easy"]
        m = stats[cat]["medium"]
        h = stats[cat]["hard"]
        total = e + m + h

        bar_y = y + (row_height - bar_height) / 2

        svg_lines.append(
            f'<text x="{label_x}" y="{y + row_height / 2 + 4}" font-size="13" '
            f'fill="{TEXT_COLOR}">{cat}</text>'
        )

        track_w = max(int(total * scale), 1) if total else 6
        svg_lines.append(
            f'<rect x="{bar_x}" y="{bar_y}" width="{track_w}" '
            f'height="{bar_height}" rx="4" fill="{TRACK_COLOR}" />'
        )

        seg_x = bar_x
        for count, color in ((e, EASY_COLOR), (m, MEDIUM_COLOR), (h, HARD_COLOR)):
            if count <= 0:
                continue
            seg_w = max(count * scale, 2)
            svg_lines.append(
                f'<rect x="{seg_x:.1f}" y="{bar_y}" width="{seg_w:.1f}" '
                f'height="{bar_height}" fill="{color}" />'
            )
            seg_x += seg_w

        label_x_pos = seg_x + 10 if total else bar_x + 14
        svg_lines.append(
            f'<text x="{label_x_pos:.1f}" y="{y + row_height / 2 + 4}" font-size="12" '
            f'fill="{MUTED_COLOR}">{total}</text>'
        )

        y += row_height

    svg_lines.append("</svg>")

    os.makedirs("assets", exist_ok=True)
    with open("assets/progress.svg", "w") as f:
        f.write("\n".join(svg_lines))


if __name__ == "__main__":
    data = scan_repository()
    generate_svg(data)