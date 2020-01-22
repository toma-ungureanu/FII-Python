def build_xml_element(tag, value, href, _class, id1):
    return "<" + tag + " href=\\\"" + href + "_class=\"" + _class + tag + "/>"


def main():
    build_xml_element("a", "Hello there", "http://python.org")