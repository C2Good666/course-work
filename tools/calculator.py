import ast
import operator as op
import re

# =========================
# 安全计算部分
# =========================
allowed_operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
}

def eval_expr(expr):
    def _eval(node):
        if isinstance(node, ast.Constant):
            return node.value

        elif isinstance(node, ast.BinOp):
            return allowed_operators[type(node.op)](
                _eval(node.left),
                _eval(node.right)
            )

        else:
            raise ValueError("Unsupported expression")

    node = ast.parse(expr, mode='eval').body
    return _eval(node)


# =========================
# 中文转数学表达式（核心🔥）
# =========================
def normalize(query: str) -> str:

    mapping = {
        "乘": "*",
        "x": "*",
        "X": "*",
        "加": "+",
        "减": "-",
        "除": "/",
        "（": "(",
        "）": ")"
    }

    for k, v in mapping.items():
        query = query.replace(k, v)

    # 提取数字+符号
    query = re.sub(r"[^0-9+\-*/().]", "", query)

    return query


# =========================
# 主入口
# =========================
def calculator_tool(query: str):
    try:
        expr = normalize(query)
        return eval_expr(expr)

    except Exception:
        return "❌ invalid expression"