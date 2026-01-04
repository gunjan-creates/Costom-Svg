# generate_suyog_snake.py
# SUYOG SVG with full transparent background (GitHub-safe)

word = "SUYOG"

S = [
    [1,1,1,1,1],
    [1,0,0,0,0],
    [1,1,1,1,1],
    [0,0,0,0,1],
    [1,1,1,1,1],
]

U = [
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1],
]

Y = [
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
]

O = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1],
]

G = [
    [1,1,1,1,1],
    [1,0,0,0,0],
    [1,0,1,1,1],
    [1,0,0,0,1],
    [1,1,1,1,1],
]

letters = {
    "S": S,
    "U": U,
    "Y": Y,
    "O": O,
    "G": G
}

s = 8
margin_x = 8
margin_y = 8
r = 2.4
snake_speed_step = 0.25

circles = []
dot_index = 0
letter_index = 0

for ch in word:
    mat = letters[ch]
    letter_offset = letter_index * (5 + 1)
    for row in range(5):
        for col in range(5):
            if mat[row][col]:
                cx = margin_x + (letter_offset + col) * s
                cy = margin_y + row * s
                circles.append({
                    "id": dot_index,
                    "cx": cx,
                    "cy": cy
                })
                dot_index += 1
    letter_index += 1

svg_width = margin_x * 2 + ((5 + 1) * len(word) - 1) * s
svg_height = margin_y * 2 + (5 - 1) * s

# Snake path
path_points = []
for i, c in enumerate(circles):
    cmd = "M" if i == 0 else "L"
    path_points.append(f"{cmd} {c['cx']} {c['cy']}")
path_d = " ".join(path_points)

lines = []
lines.append(
    f'<svg viewBox="0 0 {svg_width} {svg_height}" '
    f'width="{svg_width}" height="{svg_height}" '
    f'xmlns="http://www.w3.org/2000/svg" '
    f'style="background:none;" fill="none" '
    f'xmlns:xlink="http://www.w3.org/1999/xlink">'
)

lines.append(f'<path id="snakePath" d="{path_d}" fill="none" stroke="none" />')

total_duration = snake_speed_step * len(circles)

# Snake head
lines.append(f'''
<circle r="{r*1.6}" fill="#30a14e">
  <animateMotion dur="{total_duration:.1f}s"
                 repeatCount="indefinite"
                 rotate="auto">
    <mpath xlink:href="#snakePath"/>
  </animateMotion>
</circle>
''')

# Dots
for i, c in enumerate(circles):
    begin_offset = i * snake_speed_step
    lines.append(f'''
<circle cx="{c['cx']}" cy="{c['cy']}" r="{r}" fill="#40c463">
  <animate attributeName="opacity"
           values="1;0;1"
           dur="1.2s"
           begin="{begin_offset:.2f}s"
           repeatCount="indefinite"/>
</circle>
''')

lines.append('</svg>')

with open("suyog_snake.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("✅ SUYOG Snake SVG generated with transparent background!")
# for the github User https://github.com/in/suyogchore