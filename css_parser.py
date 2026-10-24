
import re
import json


def parse_css(css_text):
    # Remove CSS comments
    css_text = re.sub(
        r"/\*.*?\*/", "", css_text, flags=re.DOTALL
    )

    # Find CSS rules
    pattern = r"([^{}]+)\{([^{}]*)\}"
    matches = list(re.finditer(pattern, css_text))

    # Check for unmatched braces or invalid text
    remaining = re.sub(pattern, "", css_text).strip()
    if remaining:
        raise ValueError("Invalid CSS: unmatched braces or incomplete rule")

    results = []

    for match in matches:
        selectors_text = match.group(1).strip()
        body = match.group(2).strip()
        properties = {}

        for declaration in body.split(";"):
            if not declaration.strip():
                continue

            if ":" not in declaration:
                raise ValueError("Invalid CSS declaration")

            key, value = declaration.split(":", 1)
            key, value = key.strip(), value.strip()

            if not key or not value:
                raise ValueError("CSS property or value is missing")

            properties[key] = value

        for selector in selectors_text.split(","):
            selector = selector.strip()
            if selector:
                results.append({
                    "selector": selector,
                    "properties": properties.copy()
                })

    return results


if __name__ == "__main__":
    sample_css = """
    /* Sample CSS */
    .card, .panel {
        color: blue;
        padding: 10px;
        background-color: white;
    }

    h1 {
        font-size: 24px;
        color: black;
    }
    """

    try:
        result = parse_css(sample_css)
        print("CSS Parser Output:")
        print(json.dumps(result, indent=2))
    except ValueError as error:
        print("Error:", error)

    # Edge-case test
    try:
        parse_css(".card { color: blue;")
    except ValueError:
        print("\nEdge-case test passed: malformed CSS detected.")
