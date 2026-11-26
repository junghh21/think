import markdown, pathlib, re
from bs4 import BeautifulSoup
root = pathlib.Path(__file__).parent
src = (root / "원문.md").read_text(encoding="utf-8")
lines = []
for ln in src.split("\n"):
    if ln.startswith("> "):
        ln = ln[2:]
    ln = re.sub(r"^ {3}\* ", "    * ", ln)
    lines.append(ln)
html = markdown.markdown("\n".join(lines), extensions=["tables", "sane_lists"])
soup = BeautifulSoup(html, "html.parser")
for t in soup.find_all("table"):
    heads = [th.get_text(strip=True) for th in t.find_all("th")]
    for tr in t.find("tbody").find_all("tr"):
        for i, td in enumerate(tr.find_all("td")):
            td["data-label"] = heads[i] if i < len(heads) else ""
            if not td.get_text(strip=True):
                td["class"] = "empty"
tpl = (root / "template.html").read_text(encoding="utf-8")
(root / "index.html").write_text(tpl.replace("{{BODY}}", str(soup)), encoding="utf-8")
