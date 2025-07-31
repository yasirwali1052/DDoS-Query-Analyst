import pandas as pd

def load_logs(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(csv_path)

def execute_code(code: str, df: pd.DataFrame) -> str:
    local_vars = {"df": df}
    try:
        exec(code, {}, local_vars)
        result = local_vars.get("result", "No 'result' variable returned.")
        return str(result)
    except Exception as e:
        return f"Execution Error: {e}"
