
import sys
import pdfrw


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

pdf_template = "bth_time_report_template.pdf"

template_pdf = pdfrw.PdfReader(pdf_template)

def write_data_to_pdf():
    return 0

def read_data_from_calendar():
    return 0

def read_user_profile():
    return 0

def read_template():
    return 0

def main() -> int:
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    print(key)

    return 0

if __name__ == "__main__":
    sys.exit(main())