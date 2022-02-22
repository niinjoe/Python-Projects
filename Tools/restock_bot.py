from bs4 import BeautifulSoup

with open("Raspberry Pi Zero 2 W.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

soup = BeautifulSoup(
    "<html>https://www.canakit.com/raspberry-pi-zero-2-w.html</html>", "html.parser"
)

print(
    BeautifulSoup(
        "<html><head></head><body>Sacr&eacute; bleu!</body></html>", "html.parser"
    )
)
# <html><head></head><body>Sacré bleu!</body></html>
