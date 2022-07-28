import pdfkit
pdfkit.from_file('pdf.html', 'out.pdf')

pdfkit.from_string('hi hello', 'hello.pdf')

pdfkit.from_url('https://www.google.co.in/','google.pdf')

