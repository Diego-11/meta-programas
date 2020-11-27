from django.template import Context
from metaprogramas.settings import MEDIA_ROOT
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.core.files.storage import default_storage


def generate_pdf(data, poll_id):
    data = data

    template = get_template('polls/result.html')
    html = template.render(data)

    file = open(f'./media/pdf/poll_{poll_id}.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
                                encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()
    # return HttpResponse(pdf, 'application/pdf')
    return True
