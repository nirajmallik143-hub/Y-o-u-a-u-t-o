import os
from PIL import Image, ImageDraw, ImageFont

def generate_auto_image(scene_title="Yummy Yummy Kids", output_path="assets/scene.jpg", is_short=True):
    # Ensure assets directory exists
    os.makedirs("assets", exist_ok=True)
    
    # 1. Set dimensions (Shorts: 1080x1920, Long: 1920x1080)
    if is_short:
        size = (1080, 1920)
        bg_color = (255, 182, 193) # Light pink for kids short
    else:
        size = (1920, 1080)
        bg_color = (135, 206, 235) # Sky blue for long video
        
    # 2. Create vibrant background image
    img = Image.new('RGB', size, color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # 3. Add decorative colorful shapes/frames for kids theme
    draw.rectangle([50, 50, size[0]-50, size[1]-50], outline=(255, 255, 255), width=15)
    
    # 4. Draw text title onto the image canvas
    text_y = size[1] // 2
    draw.text((100, text_y), scene_title, fill=(50, 50, 50))
    
    img.save(output_path)
    print(f"Auto-generated HD picture saved at: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_auto_image("Fun Adventure Time!", "assets/scene.jpg", True)
