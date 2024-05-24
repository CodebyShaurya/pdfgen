from flask import Flask, make_response , render_template
import pdfkit

from flask_cors import CORS, cross_origin
config = pdfkit.configuration(wkhtmltopdf='D:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

# pdfkit.from_url("http://google.com", "out.pdf", configuration=config)
# pdfkit.from_url('http://google.com', 'out.pdf')
# pdfkit.from_file('test.html', 'out.pdf')
# pdfkit.from_string('Hello!', 'out.pdf')
app = Flask(__name__)
cors = CORS(app)
@app.route("/<name>/<location>")
def pdf_template(name,location):

    config = pdfkit.configuration(wkhtmltopdf='D:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    res = render_template('index.html' , name=name , location = location)

    responsestring = pdfkit.from_string(res, False, configuration=config)

    # responsestring = pdfkit.from_string(res,False)
    
    response = make_response(responsestring)

    response.headers['Content-type'] = 'application/pdf'

    response.headers['Content-Disposition'] = 'attached;filename=output.pdf'

    return response

@app.route('/')
def index():
    print('listening')
    return 'Hello World'



if __name__ == "__main__":
    app.run(debug=True)
