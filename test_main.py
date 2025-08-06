from pathlib import Path
from unittest import TestCase
from main import load_document, get_fonts, main, get_title_elements
from py_pdf_parser.components import PDFDocument


class TestMain(TestCase):
    doc_dir = "documents"
    doc_path = "documents/AfterImageDec74(1016).pdf"

    def test_load_document(self):
        document = load_document(self.doc_path)
        self.assertEqual(type(document), PDFDocument)

    def test_get_fonts(self):
        document = load_document(self.doc_path)
        expected = {'UFont00000,8.0', 'UFont00000,9.0', 'UFont00000,11.0', 'UFont00000,52.0'}
        fonts = get_fonts(document=document)
        self.assertEqual(fonts, expected)

    def test_get_title_elements(self):
        document = load_document(self.doc_path)
        actual = get_title_elements(document)
        expected = "Video Conference H eld at Albany"
        self.assertEqual(actual.extract_single_element().text(), expected)
