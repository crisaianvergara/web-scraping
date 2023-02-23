# from googletrans import Translator
# from bs4 import BeautifulSoup

# # Load the HTML file
# with open("translate.html", "r", encoding="utf-8") as file:
#     html = file.read()

# # Parse the HTML using BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")

# # Extract all the text from the HTML and translate it to Hindi
# text_elements = soup.find_all(string=True)

# translator = Translator()
# for element in text_elements:
#     translated_text = translator.translate(element, dest="hi").text
#     element.replace_with(translated_text)

# # Write the modified HTML to a file
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(str(soup))


# from googletrans import Translator
# from bs4 import BeautifulSoup

# # Load the HTML file
# with open("translate.html", "r", encoding="utf-8") as file:
#     html = file.read()

# # Parse the HTML using BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")

# # Extract all the text from the HTML and translate it to Hindi
# text_elements = soup.find_all(string=True)

# translator = Translator()
# for element in text_elements:
#     if element.parent.name in ['style', 'script']:
#         continue
#     translated_text = translator.translate(element, dest="hi").text
#     element.replace_with(translated_text)

# # Write the modified HTML to a file
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(str(soup))



# from googletrans import Translator
# from bs4 import BeautifulSoup

# # Load the HTML file
# with open("translate.html", "r", encoding="utf-8") as file:
#     html = file.read()

# # Parse the HTML using BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")

# # List of tags to translate text from
# tags_to_translate = ['p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'a', 'title', 'input', 'label', 'select', 'option', 'table', 'th', 'tbody', 'tr', 'strong', 'td', 'textarea', 'ul', 'ol', 'li', 'b', 'i', 'ul', 'ol', 'li', 'b', 'i', 'button']


# # Extract text from specific tags and translate to Hindi
# translator = Translator()
# for tag in tags_to_translate:
#     elements = soup.find_all(tag)
#     for element in elements:
#         if element.parent.name not in ['script', 'style']:
#             if element.string is not None:
#                 translated_text = translator.translate(element.get_text(), dest="hi").text
#                 element.string.replace_with(translated_text)

# # Write the modified HTML to a file
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(str(soup))



# import os
# from googletrans import Translator
# from bs4 import BeautifulSoup

# # Set the path to the directory containing HTML files to be translated
# html_dir = r"C:\Users\Aian-PC\Desktop\final-output\taskone\www.classcentral.com"


# # List all the HTML files in the directory
# html_files = [os.path.join(html_dir, f) for f in os.listdir(html_dir) if f.endswith('.html')]

# # Loop through each HTML file
# for html_file in html_files:
#     # Load the HTML file
#     with open(html_file, "r", encoding="utf-8") as file:
#         html = file.read()

#     # Parse the HTML using BeautifulSoup
#     soup = BeautifulSoup(html, "html.parser")

#     # List of tags to translate text from
#     tags_to_translate = ['p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'a', 'title', 'input', 'label', 'select', 'option', 'table', 'th', 'tbody', 'tr', 'strong', 'td', 'textarea', 'ul', 'ol', 'li', 'b', 'i', 'ul', 'ol', 'li', 'b', 'i', 'button']

#     # Extract text from specific tags and translate to Hindi
#     translator = Translator()
#     for tag in tags_to_translate:
#         elements = soup.find_all(tag)
#         for element in elements:
#             if element.parent.name not in ['script', 'style']:
#                 if element.string is not None:
#                     translated_text = translator.translate(element.get_text(), dest="hi").text
#                     element.string.replace_with(translated_text)

#     # Write the modified HTML to the same file
#     with open(html_file, "w", encoding="utf-8") as file:
#         file.write(str(soup))



