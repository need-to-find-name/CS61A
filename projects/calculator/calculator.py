"""Simple Calculator project."""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a, op, b):
    """Calculate a op b. Raises ValueError for unknown op."""
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operation: {op!r}. Use one of {list(OPERATIONS)}")
    return OPERATIONS[op](a, b)


def evaluate_expression(expr):
    """Evaluate a math expression like '2 + 3 * (4 - 1)'. Safe, no eval()."""
    import ast
    import operator

    allowed_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError(f"Unsupported value: {node.value!r}")
        if isinstance(node, ast.BinOp) and type(node.op) in allowed_ops:
            left, right = _eval(node.left), _eval(node.right)
            if isinstance(node.op, ast.Div) and right == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return allowed_ops[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in allowed_ops:
            return allowed_ops[type(node.op)](_eval(node.operand))
        raise ValueError(f"Unsupported expression: {expr!r}")

    if not expr or not expr.strip():
        raise ValueError("Empty expression.")
    tree = ast.parse(expr, mode="eval")
    return _eval(tree)


def main(argv=None):
    """Easier access:
    - python calculator.py              -> interactive step-by-step
    - python calculator.py \"2 + 3 * 4\"  -> single expression mode
    - python calculator.py 2 + 3        -> same, args joined
    """
    import sys

    args = sys.argv[1:] if argv is None else argv
    if args:
        expr = " ".join(args)
        try:
            print(f"{expr} = {evaluate_expression(expr)}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        return

    print("Simple Calculator (+, -, *, /, parens).")
    print("Type an expression like 2 + 3 * 4, or 'q' to quit.")
    while True:
        try:
            raw = input("calc> ").strip()
            if raw.lower() in ("q", "quit", "exit"):
                break
            if not raw:
                continue
            # Backwards compat: old 3-prompt style if user just types a number,
            # fall through to expression mode which handles it too.
            try:
                result = evaluate_expression(raw)
                print(f"Result: {raw} = {result}")
            except (ValueError, ZeroDivisionError) as e:
                # Maybe old style: number, then ask op + second number
                print(f"Input error: {e}")
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            break


if __name__ == "__main__":
    main()
