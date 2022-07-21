from main import summarize
from type2 import generate_summary

with open('message.txt', encoding='utf8') as file:
 article_text = file.read()


print(generate_summary(4,article_text))