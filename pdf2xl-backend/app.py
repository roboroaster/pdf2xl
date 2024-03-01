import re
import uuid
from pdfminer.high_level import extract_pages, extract_text
from flask import Flask,request,send_file
from flask_cors import CORS, cross_origin

from pdfquery import PDFQuery
import pdfplumber
import pandas as pd
import requests

# app = Flask(__name__)
app = Flask(__name__)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

@app.route('/api/bill-convertor', methods=['POST'])
@cross_origin()
def sample_endpoint():

    # f = request.files['file']
    
    # print(f)
    if 'file' not in request.files:
        return 'no file is uploaded',400
    
    file = request.files['file']
    filename = str(uuid.uuid4())
    file.save(filename+'.pdf')
    
    
    # code to convert the pdf to excel report
    
    i = 0
    for page_layout in extract_pages(filename+'.pdf'):
        for element in page_layout:
            # text = extract_text(element)

            if i == 3:
                print(element)
        if i == 3:
            break
        i += 1
        
    
    pdf = PDFQuery(filename+'.pdf')
    pdf.load()
    invoices = pdf.pq('LTTextBoxHorizontal:in_bbox("109.774,496.869,159.075,504.416")').text()
    i = 0
    df = pd.DataFrame(columns=['Place of Supply', 'Invoice No.', 'Invoice Date', 'Markup Amount', 'Taxable Amount', 'IGST', 'CGST','SGST','Total Amount', 'Bill To'])

    with pdfplumber.open(filename+'.pdf') as pdf:
        pages = pdf.pages
        for page in pages:
            text = page.extract_text()
            elements = text.split('\n')
            print(elements)
            place = ''
            invoice_no = ''
            invoice_date = ''
            markup = ''
            taxable_amount = ''
            igst = ''
            cgst = ''
            sgst = ''
            total_amount = ''
            bill_to = ''
            for element in elements:
                if element.startswith('Place of Supply'):
                    print(' '.join(element.split(' ')[3:-2]))
                    place = ' '.join(element.split(' ')[3:-2])
                if element.startswith('Invoice No.'):
                    print(element.split(' ')[2])    
                    invoice_no = element.split(' ')[2]
                if element.startswith('Invoice Date'):
                    print(element.split(' ')[-1])    
                    invoice_date = element.split(' ')[-1]    
                if element.startswith('Markup:'):
                    print(element.split(' ')[-1])    
                    markup = element.split(' ')[-1]
                if element.startswith('Taxable Amount:'):
                    print(element.split(' ')[-1])    
                    taxable_amount = element.split(' ')[-1]
                if element.startswith('IGST:'):
                    print(element.split(' ')[-1])    
                    igst = element.split(' ')[-1]    
                if element.startswith('CGST:'):
                    print(element.split(' ')[-1])    
                    cgst = element.split(' ')[-1]    
                if element.startswith('SGST:'):
                    print(element.split(' ')[-1])    
                    sgst = element.split(' ')[-1]    
                if element.startswith('Description of charges: As per agreed terms, Total Amount'):
                    print(element.split(' ')[-1])
                    total_amount = element.split(' ')[-1]    
            try:
                x = elements.index('From Bill To')
                x += 1
                bill_to = elements[x].split(' , ')[-1]
                print(bill_to)
            except:
                print('error')
            finally:
                pass
            # break
            row = [place, invoice_no, invoice_date, markup, taxable_amount, igst, cgst, sgst,total_amount, bill_to]
            if row != [''] * 10:
                df.loc[len(df)] = row
    # df.to_csv('bills.csv')
    df.to_excel(f'{filename}.xlsx', sheet_name='bills', index=False, engine='xlsxwriter')
    
    return send_file(f'{filename}.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(port=8000,debug=True)
    # CORS(app, support_credentials=True)