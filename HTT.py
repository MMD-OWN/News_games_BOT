from bs4 import BeautifulSoup
import translate_google as tg

def get_texts(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    text_content = ''
    i = 1
    find = soup.find_all(['h2', 'p'])

    for tag in find:
        if tag.name == 'h2':
            if tag.get_text() != '' and tag.get_text() != ' ':
                text_content = text_content + f"**{tg.translate('fa', tag.get_text())}**"
                if i < len(find):
                    text_content = text_content + '\n'
        elif tag.name == 'p':
            if tag.get_text() != '' and tag.get_text() != ' ':
                text_content = text_content + tg.translate('fa', tag.get_text())
                if i < len(find):
                    text_content = text_content + '\n'
        i = i + 1

    return text_content