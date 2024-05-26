import json
import qrcode
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from PIL import Image

def create_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

def create_pdf(config_file, output_file):
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(config_file, 'r') as file:
        config = json.load(file)
    
    c = canvas.Canvas(output_file, pagesize=(4 * 72, 5 * 72))  # 4x5 inches at 72 DPI
    width, height = 4 * 72, 5 * 72
    
    # Define positions for the stickers
    sticker_width = width / 2
    sticker_height = height / 2
    positions = [
        (0, height - sticker_height),
        (sticker_width, height - sticker_height),
        (0, height - 2 * sticker_height),
        (sticker_width, height - 2 * sticker_height)
    ]
    
    # Generate QR codes and place them with subtitles
    for i, pos in enumerate(positions):
        qr_filename = os.path.join(output_dir, f"qr_{i}.png")
        create_qr_code(config[f'sticker_{i+1}']['text'], qr_filename)
        
        qr_image = Image.open(qr_filename)
        qr_width, qr_height = sticker_width - 20, sticker_height - 40
        c.drawImage(qr_filename, pos[0] + 10, pos[1] + 30, width=qr_width, height=qr_height)
        
        # Center the subtitle text below the QR code
        subtitle_text = config[f'sticker_{i+1}']['subtitle']
        text_width = c.stringWidth(subtitle_text, "Helvetica", 10)
        x_centered = pos[0] + (sticker_width - text_width) / 2
        c.drawString(x_centered, pos[1] + 25, subtitle_text)

    c.save()

# Example config.json content:
# {
#     "sticker_1": {"text": "https://example.com/1", "subtitle": "Link 1"},
#     "sticker_2": {"text": "https://example.com/2", "subtitle": "Link 2"},
#     "sticker_3": {"text": "https://example.com/3", "subtitle": "Link 3"},
#     "sticker_4": {"text": "https://example.com/4", "subtitle": "Link 4"}
# }

create_pdf("config.json", "out/stickers.pdf")
