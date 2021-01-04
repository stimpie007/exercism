import re


def parse(markdown):
    string = markdown
    string = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>', string)
    string = re.sub(r'_([^\n]+?)_', r'<em>\1</em>', string)
    string = re.sub(r'^\* (.*?$)', r'<li>\1</li>', string, flags=re.M)
    string = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', string, flags=re.S)
    for i in range(6, 0, -1):
        string = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), string, flags=re.M)
    string = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', string, flags=re.M)
    string = re.sub(r'\n', '', string)
    return string
