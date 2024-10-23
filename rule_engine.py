import re
from models.ast_node import Node

def create_rule(rule_string):
    def parse_expression(tokens):
        if len(tokens) == 1:
            return tokens[0]
        elif len(tokens) == 3:
            return {
                "type": "operand",
                "value": " ".join(tokens)
            }
        else:
            for i, token in enumerate(tokens):
                if token in ["AND", "OR"]:
                    return {
                        "type": "operator",
                        "value": token,
                        "left": parse_expression(tokens[:i]),
                        "right": parse_expression(tokens[i+1:])
                    }
            # If no AND/OR found, treat as a single operand
            return {
                "type": "operand",
                "value": " ".join(tokens)
            }

    tokens = rule_string.replace("(", "").replace(")", "").split()
    return parse_expression(tokens)

def combine_rules(rules):
    if len(rules) == 1:
        return create_rule(rules[0])
    
    combined_ast = create_rule(rules[0])
    for rule in rules[1:]:
        new_ast = create_rule(rule)
        combined_ast = {
            "type": "operator",
            "value": "AND",
            "left": combined_ast,
            "right": new_ast
        }
    return combined_ast

def evaluate_rule(ast, data):
    if not isinstance(ast, dict):
        print(f"Invalid AST structure: {ast}")
        return False
    
    if 'type' not in ast:
        print(f"Missing 'type' in AST node: {ast}")
        return False
    
    if ast['type'] == "operator":
        if ast['value'] == "AND":
            return evaluate_rule(ast['left'], data) and evaluate_rule(ast['right'], data)
        elif ast['value'] == "OR":
            return evaluate_rule(ast['left'], data) or evaluate_rule(ast['right'], data)
    elif ast['type'] == "operand":
        field, op, value = ast['value'].split()
        if field not in data:
            print(f"Field '{field}' not found in data")
            return False
        if op == '=':
            return data[field] == value.strip("'")
        elif op == '>':
            return data[field] > float(value)
        elif op == '<':
            return data[field] < float(value)
    
    print(f"Unhandled AST node: {ast}")
    return False

# Test cases
rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"

# Create individual rules
ast1 = create_rule(rule1)
ast2 = create_rule(rule2)

print("AST for rule1:", ast1)
print("AST for rule2:", ast2)

# Combine rules
combined_ast = combine_rules([rule1, rule2])
print("Combined AST:", combined_ast)

# Test evaluation
test_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 7}
result = evaluate_rule(combined_ast, test_data)
print("Evaluation result:", result)