from modules.templates import load_prompt
from modules.llm_connector import generate_code
from modules.utils import load_logs, execute_code

def analyze_logs(query: str, csv_path: str, template_path: str) -> str:
    df = load_logs(csv_path)                              # Load logs as DataFrame
    prompt = load_prompt(template_path, query)            # Format prompt using query and template
    code = generate_code(prompt)                          # Call LLM to generate Python code
    print("Generated Code:\n", code)

    # ✅ Clean up code: remove markdown formatting if present
    if "```" in code:
        code = code.replace("```python", "").replace("```", "").strip()

    result = execute_code(code, df)                       # Run the generated code using your DataFrame
    return result
