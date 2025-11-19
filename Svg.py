# generate_aryan_snake.py
# Custom "ARYAN" dot-matrix snake animation SVG generator (TRANSPARENT BG)

word = "ARYAN"

# 5x5 dot matrix font for each letter
A = [
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
]
R = [
    [1,1,1,1,0],
    [1,0,0,0,1],
    [1,1,1,1,0],
    [1,0,0,1,0],
    [1,0,0,0,1],
]
Y = [
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
]
N = [
    [1,0,0,0,1],
    [1,1,0,0,1],
    [1,0,1,0,1],
    [1,0,0,1,1],
    [1,0,0,0,1],
]

letters = {"A": A, "R": R, "Y": Y, "N": N}

# Grid & style settings
s = 8          # spacing between dots
margin_x = 8
margin_y = 8
r = 2.4        # dot radius
snake_speed_step = 0.25  # seconds per dot

# Build dot positions
circles = []
letter_index = 0
dot_index = 0

for ch in word:
    mat = letters[ch]
    letter_offset = letter_index * (5 + 1)  # 5 cols + 1 space
    for row in range(5):
        for col in range(5):
            if mat[row][col]:
                cx = margin_x + (letter_offset + col) * s
                cy = margin_y + row * s
                circles.append({
                    "id": dot_index,
                    "char": ch,
                    "cx": cx,
                    "cy": cy,
                })
                dot_index += 1
    letter_index += 1

# SVG size
svg_width = margin_x * 2 + ((5 + 1) * len(word) - 1) * s
svg_height = margin_y * 2 + (5 - 1) * s

# Build snake path
path_points = []
for i, c in enumerate(circles):
    cmd = "M" if i == 0 else "L"
    path_points.append(f"{cmd} {c['cx']} {c['cy']}")
path_d = " ".join(path_points)

# Build SVG
lines = []
lines.append(
    f'<svg viewBox="0 0 {svg_width} {svg_height}" '
    f'xmlns="http://www.w3.org/2000/svg" '
    f'xmlns:xlink="http://www.w3.org/1999/xlink">'
)

# Transparent background (none added)

# Snake path
lines.append(f'  <path id="snakePath" d="{path_d}" fill="none" stroke="none" />')

# Snake circle
total_duration = snake_speed_step * len(circles)
lines.append(f'''  <circle id="snake" r="{r*1.6}" fill="#30a14e">
    <animateMotion id="snakeAnim"
                   dur="{total_duration:.1f}s"
                   repeatCount="indefinite"
                   rotate="auto">
      <mpath xlink:href="#snakePath" />
    </animateMotion>
  </circle>''')

# Dots
for i, c in enumerate(circles):
    begin_offset = i * snake_speed_step
    lines.append(f'''  <circle id="dot{c['id']}" cx="{c['cx']}" cy="{c['cy']}" r="{r}" fill="#40c463">
    <animate attributeName="opacity"
             values="1;0;1"
             dur="1.2s"
             begin="{begin_offset:.2f}s; snakeAnim.repeat+{begin_offset:.2f}s"
             repeatCount="indefinite" />
  </circle>''')

lines.append('</svg>')

svg_content = "\n".join(lines)

output_file = "aryan_snake.svg"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(svg_content)

print("✅ Generated TRANSPARENT SVG: aryan_snake.svg")
