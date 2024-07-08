import csv


with open('data.csv', 'r') as file:
    with open('target.csv', 'w') as target:
        writer = csv.writer(target,delimiter=";")
        reader = csv.reader(file,delimiter=";")
        for row in reader:
            line1 = f'<h3>Opmerking Control Bio 1.0.4zv {row[0]}</h3>'
            line2 = f'<h2>ISO 27001:2022 control {row[3]}</h2>'
            line3 = f'<h3>Control titel: {row[0]}</h3>'
            line4 = f'<h4>Control</h4>'
            line5 = f'<p>{row[4]}</p>'
            line6 = '<h4>Doel</h4>'
            line7 = f'<p>{row[5]}</p>'
            line8 = '<h4>Overheidsmaatregel</h4>'
            line9 = f'<p>{row[10]}</p>'
            line10 = '<h4>Verantwoordelijke</h4>'
            line11 = f'<p>{row[11]}</p>'
            line12 = '<h4>Type control</h4>'
            line13 = f'<p>{row[12]}</p>'
            line14 = '<h4>Informatiebeveiligingseigenschappen</h4>'
            line15 = f'<p>{row[13]}</p>'
            line16 = '<h4>Cybersecurity Concepten</h4>'
            line17 = f'<p>{row[14]}</p>'
            line18 = '<h4>Operationele Capaciteiten</h4>'
            line19 = f'<p>{row[15]}</p>'
            line20 = '<h4>Beveiligingsdomeinen</h4>'
            line21 = f'<p>{row[16]}</p>'
            line22 = '<h4>Opmerking Control Bio 1.04rv</h4>'
            line23 = f'<p>{row[6]}</p>'
            writer.writerow([f'{row[0]} {row[3]}',f'{line1} {line2} {line3} {line4} {line5} {line6} {line7} {line8} {line9} {line10} {line11} {line12} {line13} {line14} {line15} {line16} {line17} {line18} {line19} {line20} {line21} {line22} {line23}'])