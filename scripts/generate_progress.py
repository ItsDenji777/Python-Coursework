
import json
import urllib.request
from pathlib import Path

DATA_URL = "https://kasra-seydi.ir/data/techstack.json"
OUTPUT = Path("assets/learning-progress.svg")

def fetch_progress():
    request = urllib.request.Request(
        DATA_URL,
        headers={"User-Agent": "Python-Coursework-Progress/1.0"}
    )

    with urllib.request.urlopen(request, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))

    python = next(
        (item for item in data if item.get("name") == "Python"),
        None
    )

    if not python or not python.get("Learning"):
        raise ValueError("Python learning entry not found or inactive.")

    percentage = python.get("learntpercentage")

    if isinstance(percentage, bool) or not isinstance(percentage, (int, float)):
        raise ValueError("Invalid learning percentage.")

    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100.")

    return percentage




def generate_svg(percentage):
    width = 514
    bar_height = 30
    bar_x = 3
    bar_y = 8

    progress_width = width * percentage / 100

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
        width="600" height="52" viewBox="0 0 600 52">

    <defs>
        <linearGradient id="pythonGradient" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#3776AB"/>
            <stop offset="55%" stop-color="#458FC0"/>
            <stop offset="100%" stop-color="#FFD43B"/>
        </linearGradient>

        <linearGradient id="empty" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#DCEAF5"/>
            <stop offset="100%" stop-color="#91B0C9"/>
        </linearGradient>

        <linearGradient id="glass" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#FFFFFF" stop-opacity=".55"/>
            <stop offset="45%" stop-color="#FFFFFF" stop-opacity=".08"/>
            <stop offset="100%" stop-color="#769AB8" stop-opacity=".2"/>
        </linearGradient>

        <clipPath id="barClip">
            <rect x="{bar_x}" y="{bar_y}"
                width="{width}" height="{bar_height}" rx="9"/>
        </clipPath>

        <clipPath id="emptyClip">
            <rect x="{bar_x + progress_width:.3f}" y="{bar_y}"
                width="{width - progress_width:.3f}"
                height="{bar_height}"/>
        </clipPath>
    </defs>

    <!-- Shadow -->
    <rect x="4" y="11" width="514" height="30"
        rx="9" fill="#263C50" opacity=".17"/>

    <g clip-path="url(#barClip)">

        <!-- Filled layer -->
        <rect x="{bar_x}" y="{bar_y}"
            width="{width}" height="{bar_height}"
            fill="url(#pythonGradient)"/>

        <!-- Empty overlay -->
        <g clip-path="url(#emptyClip)">
            <rect x="{bar_x}" y="{bar_y}"
                width="{width}" height="{bar_height}"
                fill="url(#empty)"/>
        </g>

        <!-- Glass reflection -->
        <rect x="{bar_x}" y="{bar_y}"
            width="{width}" height="{bar_height}"
            fill="url(#glass)"/>

        <!-- Glossy highlight -->
        <path d="M 4 17 Q 4 9 13 9 H 507
                 Q 515 9 515 17
                 Q 260 23 4 17 Z"
            fill="#FFFFFF" opacity=".25"/>

    </g>

    <!-- Metallic border -->
    <rect x="{bar_x}" y="{bar_y}"
        width="{width}" height="{bar_height}"
        rx="9" fill="none"
        stroke="#6D8FA9" stroke-width="1.8"/>

    <!-- Inner highlight -->
    <rect x="5" y="10" width="510" height="26"
        rx="7" fill="none"
        stroke="#FFFFFF" stroke-opacity=".55"/>

    <!-- Percentage -->
        <text x="530" y="31"
        font-family="Segoe UI, Arial, sans-serif"
        font-size="25" font-weight="700"
        fill="#3776AB">
        {percentage:g}%
    </text>

    </svg>'''

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(svg, encoding="utf-8")

if __name__ == "__main__":
    progress = fetch_progress()
    generate_svg(progress)
    print(f"Learning progress updated: {progress:g}%")
