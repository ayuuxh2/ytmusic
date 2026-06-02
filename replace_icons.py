from PIL import Image, ImageDraw
import os

source_img = r'D:\downloads\30acdb3bb0b7678f08153ed6431313fb.jpg'
res_dir = r'D:\codes\ytmusic\ytmusic\androidApp\src\main\res'

sizes = {
    'mdpi': 48,
    'hdpi': 72,
    'xhdpi': 96,
    'xxhdpi': 144,
    'xxxhdpi': 192
}

# Adaptive foreground size is larger (108dp base)
fg_sizes = {
    'mdpi': 108,
    'hdpi': 162,
    'xhdpi': 216,
    'xxhdpi': 324,
    'xxxhdpi': 432
}

try:
    with Image.open(source_img) as img:
        img = img.convert('RGBA')
        
        # Function to make circle
        def make_circle(im):
            mask = Image.new('L', im.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + im.size, fill=255)
            output = im.copy()
            output.putalpha(mask)
            return output

        # Ensure all folders exist
        for dpi in sizes.keys():
            os.makedirs(os.path.join(res_dir, f'mipmap-{dpi}'), exist_ok=True)

        for dpi, size in sizes.items():
            folder = os.path.join(res_dir, f'mipmap-{dpi}')
            
            # Standard square/full image
            resized = img.resize((size, size), Image.Resampling.LANCZOS)
            resized.save(os.path.join(folder, 'ic_launcher.webp'), 'WEBP')
            
            # Round image
            round_img = make_circle(resized)
            round_img.save(os.path.join(folder, 'ic_launcher_round.webp'), 'WEBP')

        for dpi, size in fg_sizes.items():
            folder = os.path.join(res_dir, f'mipmap-{dpi}')
            # Foreground image
            fg_resized = img.resize((size, size), Image.Resampling.LANCZOS)
            fg_resized.save(os.path.join(folder, 'ic_launcher_foreground.webp'), 'WEBP')

    # Delete existing XML foreground/backgrounds that might conflict
    import glob
    for xml_file in glob.glob(os.path.join(res_dir, 'drawable*', 'ic_launcher_foreground.xml')):
        os.remove(xml_file)
    for xml_file in glob.glob(os.path.join(res_dir, 'drawable*', 'monochrome.xml')):
        os.remove(xml_file)
    
    print('Icons replaced successfully!')
except Exception as e:
    print(f'Error: {e}')
