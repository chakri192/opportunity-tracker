# opportunity-tracker 

A Python CLI tool that scrapes upcoming hackathon and coding competition listings from [Unstop](https://unstop.com/hackathons) and displays them in a clean, formatted table. Optionally export results to a CSV file for tracking deadlines offline.

---

## Features

- Scrapes live hackathon listings from Unstop
- Displays results in a readable terminal table
- Export to CSV with a single prompt
- Lightweight — only 3 dependencies

---

## Requirements

- Python 3.7+
- pip

---

## Installation

```bash
git clone https://github.com/chakri192/opportunity-tracker.git
cd opportunity-tracker
pip install -r requirements.txt
```

---

## Usage

```bash
python tracker.py
```

The script will:
1. Fetch upcoming hackathon listings from `https://unstop.com/hackathons`
2. Parse and display them as a formatted table in your terminal
3. Prompt you to save the results to a CSV file

### Change the source URL

To scrape a different Unstop category (e.g., internships or competitions), open `tracker.py` and update the `url` variable in `main()`:

```python
url = "https://unstop.com/competitions"  # or any other Unstop listing page
```

---

## Dependencies

| Package        | Purpose                        |
|----------------|--------------------------------|
| `requests`     | Fetch page HTML over HTTP      |
| `beautifulsoup4` | Parse and extract event data |
| `tabulate`     | Render results as a table      |

Install all with:

```bash
pip install -r requirements.txt
```

---

## Example Output

```
+-------------------------------+------------------+------------+
| Event Name                    | Organization     | Deadline   |
+-------------------------------+------------------+------------+
| Smart India Hackathon 2025    | AICTE            | 2025-08-01 |
| HackWithInfy                  | Infosys          | 2025-07-15 |
| Code for Good                 | JPMorgan Chase   | 2025-07-30 |
+-------------------------------+------------------+------------+
Save results to CSV? (y/n): y
Saved to hackathons_2025-07-01.csv
```

---

## Automate with Cron

To run this automatically every day and keep your CSV updated:

```bash
# Run every morning at 8 AM
0 8 * * * cd /path/to/opportunity-tracker && python tracker.py >> tracker.log 2>&1
```

Add this to your crontab with `crontab -e`.

---

## Project Structure

```
opportunity-tracker/
├── tracker.py        # Main scraper and display logic
├── requirements.txt  # Python dependencies
└── .gitignore
```

---

## Known Limitations

- Scraping depends on Unstop's HTML structure — may break if their site layout changes
- No deduplication yet; running multiple times adds repeated entries to CSV
- Dates are scraped as raw strings and not yet parsed into sortable formats

---

