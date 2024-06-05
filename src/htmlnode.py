class HtmlNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props != None:
            props_string = " "
            for key, value in self.props.items():
                props_string = props_string + key + "=" + value + " "
            return props_string
        else:
            return " "
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, props={self.props})"
