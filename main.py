from pathlib import Path
from py_pdf_parser.loaders import load_file
from py_pdf_parser.components import PDFDocument
from py_pdf_parser.filtering import ElementList


def load_document(doc_path: str) -> PDFDocument:
    """
    Wrapper around 3rd party pdf loading method. Creates a PDFDocument object
    :param doc_path: string filepath of the input PDF
    :return: the input pdf as a PDFDocument
    """
    return load_file(doc_path)


def get_fonts(document: PDFDocument) -> set:
    """
    Gets the set of each element's font in a given document
    :param document: the pdf
    :return: a set containing the fonts present in the document
    """
    return set(element.font for element in document.elements)


def get_title_elements(document: PDFDocument) -> ElementList:
    """
    Gets the title elements from a PDFDocument
    :param document: input pdf doc
    :return: ElementList of the elements that match the title criteria (largest font size)
    """
    fonts = get_fonts(document=document)
    fonts_and_sizes = [{"name": font, "size": float(font.split(",")[1])} for font in fonts]
    # Going with the assumption that the largest font is the title
    title_font = sorted(fonts_and_sizes, key=lambda x: x['size'], reverse=True)[0]['name']
    return document.elements.filter_by_font(title_font)


def main(document_dir: Path) -> list[ElementList]:
    document_paths = list(document_dir.iterdir())
    titles = []
    for path in document_paths:
        document = load_document(doc_path=str(path))
        titles.append(get_title_elements(document))
    return titles


if __name__ == '__main__':
    documents_dir = Path("documents")
    titles = main(documents_dir)
    for title in titles:
        [print(title_element.text()) for title_element in title]

