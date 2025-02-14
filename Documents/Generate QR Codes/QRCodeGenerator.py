import csv
import qrcode
import qrcode.image.svg

# Requires you to install the following libraries
# qrcode
# pillow

with open('db.csv',newline='') as database: 
    csvreader = csv.reader(database, delimiter=";")
    for line in csvreader:
        data = line[0]
        name = line[1]
        
        filename = "{}.png".format(name)
        filenamesvg = "{}.svg".format(name)
        
        qr = qrcode.QRCode(
            box_size=20,
            border=1
        )
        qr.add_data(data)
        image = qr.make_image()
        image.save(filename)

        # Create SVG image

        factory = qrcode.image.svg.SvgImage
        svg = qrcode.make(data, image_factory=factory)
        svg.save(filenamesvg)
        

