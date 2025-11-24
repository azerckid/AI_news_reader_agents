# AI News Reader Agent

An intelligent news aggregation and reporting system built with [CrewAI](https://crewai.com) and [Google Gemini](https://deepmind.google/technologies/gemini/). This agentic workflow automates the process of discovering, summarizing, and curating news on specific topics, delivering professional-grade briefings in Korean.

## 🚀 Features

- **Automated Content Harvesting**: 
  - Searches for recent news articles using Serper API.
  - Filters for credibility and relevance.
  - Scrapes full article content.
- **Multi-Tier Summarization (Korean)**:
  - **Headline Summary**: Tweet-style, under 280 characters.
  - **Executive Summary**: Concise briefing for quick reading.
  - **Comprehensive Summary**: Detailed context and analysis.
- **Professional Curation**:
  - Assembles a cohesive "Daily News Briefing".
  - Includes editorial analysis, key themes, and looking-ahead sections.
  - Formatted as a publication-ready Markdown report.

## 🤖 Agents

The system utilizes three specialized agents:

1.  **News Hunter Agent**: Responsible for searching the web, filtering irrelevant content, and scraping article text.
2.  **Summarizer Agent**: Analyzes the scraped content and generates structured summaries in Korean.
3.  **Curator Agent**: Compiles the summaries into a final, polished report with editorial insights.

## 🛠️ Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- API Keys:
  - **Google Gemini API Key**: For the LLM.
  - **Serper API Key**: For Google Search capabilities.

## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd 2_news-reader-agent
    ```

2.  **Install dependencies**:
    Using `uv` (recommended):
    ```bash
    uv sync
    ```
    Or using pip:
    ```bash
    pip install crewai crewai-tools python-dotenv
    ```

## ⚙️ Configuration

1.  Create a `.env` file in the root directory:
    ```bash
    touch .env
    ```

2.  Add your API keys to `.env`:
    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    SERPER_API_KEY=your_serper_api_key_here
    ```

## 🏃 Usage

Run the news reader agent:

```bash
python news_reader.py
```

By default, it searches for news about **"near protocol news"**. You can change the topic in `news_reader.py`:

```python
result = NewsReaderCrew().crew().kickoff(
    inputs={
        "topic": "your desired topic",
    }
)
```

## 📂 Output

The agent generates the following files in the `output/` directory:

-   `content_harvest.md`: Raw collected articles with metadata.
-   `summary.md`: Structured summaries for each article.
-   `final_report.md`: The final, polished daily news briefing.
