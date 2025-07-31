DDoS Query Analyst
DDoS Query Analyst is a Python-based AI agent designed to analyze large-scale DDoS (Distributed Denial of Service) network logs stored in a CSV file containing approximately 150,000 records. Leveraging LangChain and Google’s Gemini API, the project generates efficient Pandas queries to answer complex cybersecurity questions, such as filtering logs, aggregating data, detecting anomalies, and performing time-based or pattern-based analysis. Each query is accompanied by a concise report summarizing the findings, which is printed to the console and saved to an output directory. The project is optimized for large datasets, supports modular design for easy maintenance, and provides an interactive CLI for user queries.
Table of Contents

Project Overview
Features
Project Structure
Prerequisites
Setup Instructions
Usage
Example Queries
Contributing
License
Contact

Project Overview
DDoS Query Analyst processes a CSV file with DDoS logs, enabling cybersecurity analysts to extract actionable insights through natural language questions. The CSV schema includes columns like timestamp, epoch_time, src_ip, dst_ip, src_mac, dst_mac, protocol_type, packet_length, src_port, dst_port, user_agent, and url_path. The agent uses LangChain to interface with the Gemini API, generating Pandas-based queries and short reports for each analysis. Results are saved in data/output/results/ for further review. The project is designed to handle large datasets efficiently, with optional chunking for memory optimization, and is suitable for detecting potential DDoS attacks, identifying suspicious IPs, analyzing traffic patterns, and more.
Features

Natural Language Queries: Ask questions in plain English (e.g., "Find IPs with more than 50 connections to port 22") and receive tailored Pandas queries.
Comprehensive Analysis: Supports filtering, aggregation, time-based analysis, anomaly detection, protocol/port analysis, and pattern matching in user_agent or url_path.
Efficient Processing: Optimized for a 150,000-row CSV using vectorized Pandas operations and optional chunking for large datasets.
Short Reports: Generates concise, human-readable reports summarizing query results, saved to disk and printed to the console.
Modular Design: Organized into separate modules for LLM integration, query execution, prompt generation, and data handling.
Interactive CLI: Simple command-line interface for entering queries and viewing results.
Extensible: Optional config/ directory for future configuration extensions (e.g., CSV paths, chunk sizes).

Project Structure
The project is organized for clarity and maintainability, with each file/folder serving a specific purpose:

main.pyThe entry point of the application. It provides an interactive CLI where users input analytical questions and view results. It orchestrates the workflow by loading configurations, initializing the LLM connector, and invoking the analytical engine.

modules/analytical_engine.pyThe main logic controller. It coordinates the analysis process by loading the CSV, generating Pandas queries via the LLM connector, executing them, and producing reports. It handles both full dataset processing and chunked processing for large datasets.

modules/templates.pyResponsible for building dynamic prompt templates. It constructs the prompt sent to the Gemini API, incorporating the CSV schema and user question to ensure accurate query generation.

modules/llm_connector.pyManages communication with the Google Gemini API. It loads the prompt template, sends the user’s question and schema to the LLM, and retrieves the generated Pandas code and report.

modules/utils.pyHandles utility functions, including loading the CSV data and executing the generated Pandas code. It also includes logging functionality to track operations and errors for debugging.

data/  

input/ddos_logs.csv: The raw input CSV file containing approximately 150,000 DDoS logs with the specified schema.  
output/results/: Directory where query results and reports are saved as text files with timestamps (e.g., report_20250731_121401.txt).


prompts/analytical_template.txtContains the prompt template used by the Gemini API. It includes the CSV schema, instructions for generating Pandas code, and guidelines for creating a short report, with examples to guide the LLM’s output.

.envStores sensitive information, specifically the GOOGLE_API_KEY for accessing the Gemini API. This file is excluded from version control for security.

config/ (optional)Reserved for future configuration extensions (e.g., config.yaml for CSV paths or chunk sizes). Currently optional but included for scalability.


Prerequisites
To run DDoS Query Analyst, ensure you have the following:

Python: Version 3.8 or higher.
Virtual Environment: Recommended for dependency isolation (e.g., venv).
Gemini API Key: Obtain from Google AI Studio.
CSV File: A ddos_logs.csv file in data/input/ with the following schema:
timestamp: Datetime (e.g., '2025-07-31 10:00:00')
epoch_time: Integer (Unix timestamp, e.g., 1627647600)
src_ip: String (e.g., '192.168.1.1')
dst_ip: String (e.g., '10.0.0.1')
src_mac: String (e.g., '00:1A:2B:3C:4D:5E')
dst_mac: String (e.g., 'FF:FF:FF:FF:FF:FF')
protocol_type: String (e.g., 'TCP', 'UDP', 'ICMP')
packet_length: Integer (e.g., 1500)
src_port: Integer (e.g., 49152)
dst_port: Integer (e.g., 80)
user_agent: String (e.g., 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...')
url_path: String (e.g., '/login.php')



Setup Instructions
Follow these steps to set up the project locally:

Clone the Repository:
git clone https://github.com/yasirwali1052/ddos-query-analyst.git
cd ddos-query-analyst


Create and Activate a Virtual Environment:
python -m venv myvenv
# Windows
myvenv\Scripts\activate
# Linux/macOS
source myvenv/bin/activate


Install Dependencies:Install required Python packages listed in requirements.txt:
pip install -r requirements.txt


Set Up the .env File:Create a .env file in the root directory with your Gemini API key:
GOOGLE_API_KEY=your-gemini-api-key

Obtain the key from Google AI Studio.

Prepare the CSV File:Place your ddos_logs.csv file in data/input/. Ensure it matches the schema above. If using a different file name or path, update config/config.yaml (if used in the future).

Verify Configuration (Optional):If you add a config/config.yaml file for custom settings (e.g., CSV path, chunk size), ensure it’s correctly formatted:
data:
  csv_path: "data/input/ddos_logs.csv"
  chunk_size: 10000



Usage
Run the agent using the interactive CLI:
python main.py

The CLI prompts for a question:
DDoS Log Analyst - Enter your question (or 'exit' to quit):
>

Enter a question (e.g., "Find top 5 src_ips by total packet_length"). The agent will:

Generate a Pandas query using the Gemini API.
Execute the query on ddos_logs.csv.
Display the results and a short report in the console.
Save the results and report to data/output/results/ with a timestamped filename (e.g., report_20250731_121401.txt).

To exit, type exit at the prompt.
Example Queries
The agent supports a wide range of cybersecurity queries, including:

Filtering: "Show logs where url_path contains 'login' and dst_port is 80."
Aggregation: "Find top 5 src_ips by total packet_length."
Time-Based Analysis: "Find connections to dst_port 443 in the last 24 hours."
Anomaly Detection: "Find src_ip with more than 100 connections to dst_port 22."
Pattern Matching: "Show logs with user_agent containing 'bot' or 'crawler'."
DDoS-Specific: "Detect dst_ip with more than 1000 connections in 1 hour."

