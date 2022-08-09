import pyqrcode
from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "https://g.page/r/CYHWSRFa_uf4EBM/review"
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"
url.svg("greview.svg", scale = 8)
  
