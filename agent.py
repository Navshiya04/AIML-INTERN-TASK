
import ast
import operator
import re

# TOOL 1: Knowledge base
KNOWLEDGE_BASE = {
    "python": "Python is widely used in AI and Machine Learning.",
    "machine learning": "Machine Learning learns patterns from data.",
    "artificial intelligence": "AI enables machines to perform tasks that require human intelligence.",
    "css": "CSS is used to style web pages."
}


def search_tool(question):
    question = question.lower()
    matches = [
        (topic, answer)
        for topic, answer in KNOWLEDGE_BASE.items()
        if topic in question
    ]
    if matches:
        return max(matches, key=lambda item: len(item[0]))[1]
    return None


# TOOL 2: Calculator
def calculator_tool(question):
    match = re.search(
        r"\d+(?:\.\d+)?\s*[+*/-]\s*\d+(?:\.\d+)?",
        question
    )
    if not match:
        return None

    tree = ast.parse(match.group(), mode="eval").body
    ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }

    if not isinstance(tree, ast.BinOp):
        return None
    if type(tree.op) not in ops:
        return None
    if not (
        isinstance(tree.left, ast.Constant)
        and type(tree.left.value) in (int, float)
        and isinstance(tree.right, ast.Constant)
        and type(tree.right.value) in (int, float)
    ):
        return None

    return ops[type(tree.op)](tree.left.value, tree.right.value)


# AGENT: Selects a tool
def ask_agent(question):
    if not question.strip():
        return "Please enter a question."

    if re.search(r"\d\s*[+*/-]\s*\d", question):
        try:
            result = calculator_tool(question)
            if result is not None:
                return f"Calculator tool result: {result}"
        except (ValueError, SyntaxError, ZeroDivisionError):
            return "Unable to calculate this expression."

    answer = search_tool(question)
    if answer:
        return f"Knowledge tool result: {answer}"

    return "I don't have enough information to answer that."


# DEMO
if __name__ == "__main__":
    questions = [
        "What is Python?",
        "Explain machine learning",
        "Calculate 25 * 4",
        "Who won the World Cup in 2026?"
    ]

    for question in questions:
        print("\nQuestion:", question)
        print("Answer:", ask_agent(question))

    question = "What is Python?"
    print("\nRepeatability test:",
          ask_agent(question) == ask_agent(question))
