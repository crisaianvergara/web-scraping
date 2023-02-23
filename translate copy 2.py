import os
from googletrans import Translator
from bs4 import BeautifulSoup

# List of tags to translate text from
# List of tags to translate text from
tags_to_translate = [
    "p",
    "div",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "span",
    "a",
    "title",
    "input:not([type=submit]):not([type=button]):not([type=radio]):not([type=checkbox]):not([type=hidden])[placeholder]",
    "label",
    "select",
    "option",
    "table",
    "th",
    "tbody",
    "tr",
    "strong",
    "td",
    "textarea",
    "ul",
    "ol",
    "li",
    "b",
    "i",
    "ul",
    "ol",
    "li",
    "b",
    "i",
    "button",
    "img",
    "time",
    "figcaption",
    "&nbsp;",
    "footer",
    '" ',
    '" "',
    "mark",
    "pre",
    "em",
    "small",
    "sub",
    "sup",
    "code",
    "cite",
    "blockquote",
    "figure",
    "main",
    "aside",
    "nav",
    "header",
    "article",
    "section",
]


# Translator object for translating to Hindi
translator = Translator()


# Function to translate text in HTML file
def translate_html_file(file_path):
    # Load the HTML file
    with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Extract text from specific tags and translate to Hindi
    for tag in tags_to_translate:
        elements = soup.find_all(tag)
        for element in elements:
            if element.parent.name not in ["script", "style"]:
                if element.string is not None:
                    # Translate tag content
                    translated_text = translator.translate(
                        element.get_text(), dest="hi"
                    ).text
                    element.string.replace_with(translated_text)
                if element.has_attr("placeholder"):
                    # Translate placeholder attribute
                    translated_placeholder = translator.translate(
                        element.get("placeholder"), dest="hi"
                    ).text
                    element["placeholder"] = translated_placeholder

    # Write the modified HTML to the same file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(soup))


# Function to recursively search for HTML files in directory and translate them
def translate_html_in_directory(directory_path):
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path) and item_path.endswith(".html"):
            translate_html_file(item_path)
        elif os.path.isdir(item_path):
            translate_html_in_directory(item_path)


# Translate all HTML files in directory "abc"
directory_path = r"C:\Users\Aian-PC\Desktop\Final 2\classcentral\www.classcentral.com"

translate_html_in_directory(directory_path)
