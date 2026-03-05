from PIL import Image, ImageDraw, ImageFont

# Create a new image with navy to gold gradient background
width, height = 2560, 1600
image = Image.new('RGB', (width, height))

for y in range(height):
    r = int(0 + (255 - 0) * (y / height))  # Gradient from navy to gold
    g = int(0 + (215 - 0) * (y / height))
    b = int(128 + (0 - 128) * (y / height))
    ImageDraw.Draw(image).line([(0, y), (width, y)], fill=(r, g, b))

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Load a font
try:
    title_font = ImageFont.truetype('arial.ttf', 120)  # Title font
    tagline_font = ImageFont.truetype('arial.ttf', 60)  # Tagline font
    author_font = ImageFont.truetype('arial.ttf', 80)  # Author font
except IOError:
    title_font = ImageFont.load_default()
    tagline_font = ImageFont.load_default()
    author_font = ImageFont.load_default()

# Define text
title_text = "30 DAYS OF DISCIPLINE"
tagline_text = "Build Focus • Consistency • Self-Control"
author_text = "David Sun"

# Define text sizes and positions
title_size = draw.textsize(title_text, font=title_font)
tagline_size = draw.textsize(tagline_text, font=tagline_font)
author_size = draw.textsize(author_text, font=author_font)

# Calculate positions
title_x = (width - title_size[0]) / 2
    title_y = (height - title_size[1]) / 3
    tagline_x = (width - tagline_size[0]) / 2
    tagline_y = title_y + title_size[1] + 20
    author_x = (width - author_size[0]) / 2
    author_y = tagline_y + tagline_size[1] + 80

# Draw text on the image
    draw.text((title_x, title_y), title_text, font=title_font, fill="white")
    draw.text((tagline_x, tagline_y), tagline_text, font=tagline_font, fill="white")
    draw.text((author_x, author_y), author_text, font=author_font, fill="white")

# Save the image
image.save('generate_book_cover.png')
