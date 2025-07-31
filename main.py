from modules.analytical_engine import analyze_logs

if __name__ == "__main__":
    user_query = input("Ask a question about the logs: ")
    result = analyze_logs(
        query=user_query,
        csv_path="data/ddos_logs.csv",
        template_path="prompts/analytical_template.txt"
    )
    print("\nResult:\n", result)
