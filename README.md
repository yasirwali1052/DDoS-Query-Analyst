

## 📌 Project Overview

DDoS Query Analyst processes a CSV file with DDoS logs, enabling cybersecurity analysts to extract actionable insights using natural language queries.

**CSV Schema includes:**

* `timestamp`: Datetime (e.g., `'2025-07-31 10:00:00'`)
* `epoch_time`: Integer (e.g., `1627647600`)
* `src_ip`, `dst_ip`: IP addresses
* `src_mac`, `dst_mac`: MAC addresses
* `protocol_type`: `'TCP'`, `'UDP'`, `'ICMP'`, etc.
* `packet_length`: Integer
* `src_port`, `dst_port`: Integer
* `user_agent`, `url_path`: Strings for user behavior

---

## ✨ Features

* **Natural Language Queries**
  Ask plain English questions like:

  > “Find IPs with more than 50 connections to port 22.”

* **Comprehensive Analysis**
  Supports filtering, aggregation, anomaly detection, protocol/port analysis, time-based and pattern-based queries.

* **Efficient for Large Datasets**
  Optimized for 150,000+ rows using vectorized Pandas, with optional chunking.

* **Short Summary Reports**
  Automatically generates human-readable summaries for each query, printed and saved to disk.

* **Modular Design**
  Organized into independent modules for maintainability and extension.

* **Interactive CLI**
  Command-line interface for seamless user input and result display.

* **Extensible Configuration**
  Support for optional config files (e.g., YAML) to customize paths and parameters.

---

## 📁 Project Structure

```plaintext
main.py                     # Entry point CLI
modules/
├── analytical_engine.py    # Core logic for query execution
├── llm_connector.py        # Google Gemini API interaction
├── templates.py            # Prompt builder
├── utils.py                # CSV loading, query execution
data/
├── input/ddos_logs.csv     # Input data
└── output/results/         # Timestamped reports
prompts/
└── analytical_template.txt # Prompt template for Gemini
config/                     # (Optional) YAML for paths/settings
.env                        # Gemini API key (not versioned)
```

---

## ✅ Prerequisites

* Python **3.8 or higher**
* `venv` (recommended)
* Google **Gemini API Key**
* A CSV file `ddos_logs.csv` in `data/input/` matching the required schema

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yasirwali1052/ddos-query-analyst.git
cd ddos-query-analyst
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv myvenv

# Windows
myvenv\Scripts\activate

# macOS/Linux
source myvenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up `.env` with Gemini API Key

Create a `.env` file in the root:

```
GOOGLE_API_KEY=your-gemini-api-key
```

### 5. Add Your CSV File

Place `ddos_logs.csv` inside:

```
data/input/ddos_logs.csv
```

*(Ensure it matches the schema mentioned above)*

### 6. (Optional) Add YAML Config

```yaml
# config/config.yaml
data:
  csv_path: "data/input/ddos_logs.csv"
  chunk_size: 10000
```

---

## 🧪 Usage

Run the CLI:

```bash
python main.py
```

You’ll be prompted to enter a question:

```
DDoS Log Analyst - Enter your question (or 'exit' to quit):
>
```

### What it does:

1. Sends your question to Gemini via LangChain.
2. Generates a Pandas query.
3. Executes it on `ddos_logs.csv`.
4. Prints the results and a short report.
5. Saves the report to `data/output/results/report_<timestamp>.txt`.

To exit, type `exit`.

---

## 💡 Example Queries

* **Filtering:**
  “Show logs where `url_path` contains `login` and `dst_port` is 80.”

* **Aggregation:**
  “Find top 5 `src_ips` by total `packet_length`.”

* **Time-Based Analysis:**
  “Find connections to `dst_port` 443 in the last 24 hours.”

* **Anomaly Detection:**
  “Find `src_ip` with more than 100 connections to `dst_port` 22.”

* **Pattern Matching:**
  “Show logs with `user_agent` containing `bot` or `crawler`.”

* **DDoS-Specific:**
  “Detect `dst_ip` with more than 1000 connections in 1 hour.”

---


---

## 📬 Contact

**Maintainer:** Yasir Wali
GitHub: [@yasirwali1052](https://github.com/yasirwali1052)
Email: *\[yasirwali301302@gmail.com]*

---

Let me know if you want this saved as a `README.md` file or need a version optimized for GitHub Pages or documentation tools like MkDocs.
