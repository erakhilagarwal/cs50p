def main():
    inputStr = input("input math expression: ")
    value = processExpression(inputStr)
    print(f"{value:.1f}")

def processExpression(expr):
    expr = expr.strip()
    x, y, z = expr.split()
    x = float(x)
    z = float(z)
    match(y):
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x*z
        case "/":
            return x/z
    return ""

main()
