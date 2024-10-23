from flask import Flask, request, jsonify
from flask_cors import CORS
from rule_engine import create_rule, combine_rules, evaluate_rule
import json

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return "Welcome to the Rule Engine API"

@app.route('/create_rule', methods=['POST'])
def api_create_rule():
    rule_string = request.json['rule']
    ast = create_rule(rule_string)
    return jsonify({"message": "Rule created successfully", "ast": str(ast)})

@app.route('/combine_rules', methods=['POST'])
def api_combine_rules():
    rules = request.json['rules']
    print(f"Received rules for combination: {rules}")  # Debug print
    combined_ast = combine_rules(rules)
    print(f"Combined AST: {combined_ast}")  # Debug print
    return jsonify({"message": "Rules combined successfully", "ast": combined_ast})

@app.route('/evaluate_rule', methods=['POST'])
def api_evaluate_rule():
    try:
        data = request.json
        ast = data['ast']
        user_data = data['data']
        
        # Check if ast is a string and try to parse it
        if isinstance(ast, str):
            ast = json.loads(ast)
        
        # If ast is a dict with an 'ast' key, extract the actual AST
        if isinstance(ast, dict) and 'ast' in ast:
            ast = ast['ast']
        
        print(f"Received AST: {ast}")  # Debug print
        print(f"Received user data: {user_data}")  # Debug print
        
        result = evaluate_rule(ast, user_data)
        return jsonify({"result": result})
    except Exception as e:
        print(f"Error in evaluate_rule: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)