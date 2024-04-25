#codificacion y obtencion de informacion de  una imagen con codigos de barra o qr


import zxing

# Crear un lector de códigos de barras
reader = zxing.BarCodeReader()

# Decodificar el código de barras en la imagen deseada
barcode = reader.decode("C:/Users/Eduardo/Pictures/Nueva carpeta/descarga.png")

qrCode = reader.decode("C:/Users/Eduardo/Pictures/Nueva carpeta/hola_qrcode.png")

# Verificar si se pudo decodificar correctamente el código de barras
if barcode:
    # Obtener el contenido del código de barras decodificado
    contenido_codigo = barcode.parsed
    print("Contenido del código de barras:", contenido_codigo)
    print("Formato del codigo QR:",barcode.format) #para mostrar el formato del codigo
    print("Tipo del código de barras:", barcode.type)
    print("Puntos del contorno del código de barras:", barcode.points)
    
    print("")
    
    contenido_qr =qrCode.parsed
    print("Contenido del codigo qr:",contenido_qr)
    print("Formato del codigo QR:",qrCode.format) #para mostrar el formato  del codigo
    print("Tipo del código de barras:", qrCode.type)
    print("Puntos del contorno del código QR:", qrCode.points)
else:
    print("No se pudo decodificar el código de barras en la imagen.")

    



