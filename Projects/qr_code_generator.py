import qrcode
from PIL import Image
import os

urls = [
    "https://servicos.hsan.com.br:9091/apexdb/r/hsan/hsan/nps-evaluation?P181_DEPARTMENT_ID=105&P181_ROOM_ID=01",
    "https://servicos.hsan.com.br:9091/apexdb/r/hsan/hsan/nps-evaluation?P181_DEPARTMENT_ID=105&P181_ROOM_ID=02",
    "https://servicos.hsan.com.br:9091/apexdb/r/hsan/hsan/nps-evaluation?P181_DEPARTMENT_ID=105&P181_ROOM_ID=03",
    "https://servicos.hsan.com.br:9091/apexdb/r/hsan/hsan/nps-evaluation?P181_DEPARTMENT_ID=105&P181_ROOM_ID=04",
    "https://servicos.hsan.com.br:9091/apexdb/r/hsan/hsan/nps-evaluation?P181_DEPARTMENT_ID=105&P181_ROOM_ID=05",
    "https://servicos.hsan.com.br:9091/apexdb/r/hsan/hsan/nps-evaluation?P181_DEPARTMENT_ID=105&P181_ROOM_ID=06",
    "https://servicos.hsan.com.br:9091/apexdb/r/hsan/hsan/nps-evaluation?P181_DEPARTMENT_ID=105&P181_ROOM_ID=07",
    "https://servicos.hsan.com.br:9091/apexdb/r/hsan/hsan/nps-evaluation?P181_DEPARTMENT_ID=105&P181_ROOM_ID=08",
    "https://servicos.hsan.com.br:9091/apexdb/r/hsan/hsan/nps-evaluation?P181_DEPARTMENT_ID=105&P181_ROOM_ID=09",
    "https://servicos.hsan.com.br:9091/apexdb/r/hsan/hsan/nps-evaluation?P181_DEPARTMENT_ID=105&P181_ROOM_ID=10",
    "https://servicos.hsan.com.br:9091/apexdb/r/hsan/hsan/nps-evaluation?P181_DEPARTMENT_ID=105&P181_ROOM_ID=11",
    "https://servicos.hsan.com.br:9091/apexdb/r/hsan/hsan/nps-evaluation?P181_DEPARTMENT_ID=105&P181_ROOM_ID=12",
]

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

def generate_qr_code(data, output_path, size=1000):
    qr = qrcode.QRCode(
        version=10, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill="black", back_color="white")
    qr_img = qr_img.resize((size, size), Image.Resampling.LANCZOS)

    qr_img.save(output_path)

for i, url in enumerate(urls, start=1):
    file_name = f"QR_Code_Room_{str(i).zfill(2)}.png"
    file_path = os.path.join(downloads_folder, file_name)
    generate_qr_code(url, file_path)
    print(f"Saved: {file_path}")

print("All QR codes have been generated and saved in your Downloads folder.")
