text1, text2, text3 = input(), input(), input()

text = max(text1, text2, text3)

if "зайка" in text1 and text1 < text:
    text = text1
if "зайка" in text2 and text2 < text:
    text = text2
if "зайка" in text3 and text3 < text:
    text = text3

print(text, len(text))
