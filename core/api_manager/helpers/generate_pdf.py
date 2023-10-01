import os
from datetime import datetime
from django.forms import model_to_dict
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image

from core.api_manager.helpers.format_with_thousands import format_with_thousands
from core.api_manager.models.report import Report

def generate_pdf(body_data):
    report = body_data['report']
    pricing_results = body_data['pricing_results']
    report_obj = Report.objects.get(id=report['id'])
    report = model_to_dict(report_obj)
    nazwa_raportu = f"raport_{report['id']}"
    pdf_filename = f"{nazwa_raportu}.pdf"
    if not os.path.isdir('media/raporty'):
        os.makedirs('media/raporty')
    pdf_file_path = os.path.join('media/raporty/', pdf_filename)
    pdfmetrics.registerFont(TTFont('LatoRegular', 'static/fonts/Lato/Lato-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('LatoBold', 'static/fonts/Lato/Lato-Bold.ttf'))
    doc = SimpleDocTemplate(pdf_file_path, pagesize=A4)
    ctr = 1
    data = []
    for result in pricing_results:
        data.append(['#', 'Nazwa', "Symbol", "Ilość", '', '', ])
        # print(result)
        data.append([ctr,result['asset']['name'],result['asset']['ticker'],result['asset']['amount'],'',''])
        data.append(['', 'Nazwa', "Symbol", "Giełda", 'Kurs [zł]', 'Wartość [zł]', ])
        for asset_data in result['providers_data']:
            # print(asset_data)
            data.append([
                '',
                result['asset']['name'],
                result['asset']['ticker'],
                asset_data['exchange_name'],
                f"{format_with_thousands(asset_data['unit_price'])} zł",
                f"{format_with_thousands(asset_data['asset_price'])} zł",
            ])
            ctr += 1
        data.append(['', '', "", "Średnia:",
                      f"{format_with_thousands(result['average_unit_price'])} zł",
                     f"{format_with_thousands(result['average_asset_price'])} zł", ])

    data.append(['', '', '', '', 'Łącznie wartość', f"{format_with_thousands(body_data['total_value'])} zł"])
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        # ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#003E68")),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Text alignment
        ('FONTNAME', (0, 0), (-1, 0), 'LatoBold'),  # Header font
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header bottom padding
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Cell background color
        ('GRID', (0, 0), (-1, -1), 1, "#D9D9D9"),  # Gridlines
        ('FONTNAME', (0, 0), (-1, -1), 'LatoRegular'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical alignment
        ('INNERGRID', (0, 0), (-1, -1), 0.25, "#D9D9D9"),  # Inner gridlines
        # create margin
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))

    elements = []
    # elements.append(Image(filename='static/img/el_sun_logo.png', width=52, height=14, hAlign='LEFT'))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(text="Szacowanie wartości kryptoaktywów", style=ParagraphStyle(
        name='CustomStyle',
        fontName='LatoBold',
        fontSize=16,
        textColor='#000000',
    )))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(text=f"Numer ID raportu: {report['id']}", style=ParagraphStyle(
        name='CustomStyle',
        fontName='LatoRegular',
        fontSize=13,
        textColor='#000000',
    )))
    elements.append(Spacer(1, 10))
    # elements.append(Paragraph(text=f"Data wykonania raportu: {report['created']}", style=ParagraphStyle(
    formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elements.append(Paragraph(text=f"Data wykonania raportu: {formatted_date}", style=ParagraphStyle(
        name='CustomStyle',
        fontName='LatoRegular',
        fontSize=13,
        textColor='#000000',
    )))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(text=f"Numer sprawy: {report['nr_sprawy']}", style=ParagraphStyle(
        name='CustomStyle',
        fontName='LatoRegular',
        fontSize=13,
        textColor='#000000',
    )))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(text=f"Dane właściciela kryptoaktywów: {report['owner_data']}", style=ParagraphStyle(
        name='CustomStyle',
        fontName='LatoRegular',
        fontSize=13,
        textColor='#000000',
    )))
    elements.append(Spacer(2, 10))
    elements.append(table)
    doc.build(elements)
    return pdf_file_path, pdf_filename
