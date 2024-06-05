from textnode import TextNode
from htmlnode import HtmlNode



def main():
    text = TextNode("This is a text node", "bold", "https://www.boot.dev")
    text2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(f"{text.__eq__(text2)}")
    print(f"{text.__repr__()}")

    html_props = HtmlNode(props={"href": "https://www.google.com", "target": "_blank"})
    print(html_props.__repr__())

if __name__ == "__main__":
    main()
