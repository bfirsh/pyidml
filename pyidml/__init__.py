import copy
from models import Document
from xml.etree import ElementTree
import zipfile

PACKAGING_NS = '{http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging}'

def load_files(fh):
    """
    Load a zip file into a dicionary of filenames to ElementTree objects.
    """
    d = {}
    zf = zipfile.ZipFile(fh, 'r')
    for filename in zf.namelist():
        if not filename.endswith('.xml'):
            continue
        d[filename] = ElementTree.fromstring(zf.read(filename))
    return d

def normalize(element, files):
    """
    Recursively load all external idPkg references in `element` from `files` 
    into one tree.
    """
    for i, child in enumerate(element):
        if child.tag.startswith(PACKAGING_NS):
            src = child.get('src')
            if src is not None:
                root = copy.copy(files[src])
                root.tag = root.tag.replace(PACKAGING_NS, '')
                element[i] = root
        element[i] = normalize(element[i], files)
    return element
    

def parse(fh):
    files = load_files(fh)
    designmap = normalize(files['designmap.xml'], files)
    return Document.from_xml(designmap)


