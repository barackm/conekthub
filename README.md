# ConektHub: AI-Driven Talent and Opportunity Matching Platform for Rwanda

ConektHub is an AI-powered platform designed to connect talented individuals
with personalized job, collaboration, and funding opportunities in Rwanda. Built
with CrewAI and powered by OpenAI’s language models, ConektHub utilizes
specialized AI agents to analyze candidate profiles, match them with the most
relevant opportunities, and generate tailored insights. The platform's modular,
agent-based architecture allows for scalable and dynamic recommendations,
supporting talent growth and entrepreneurial connections across the country.

## Features

- **AI Agents**: Dedicated agents perform specialized tasks, from analyzing
  candidate skills and experience to refining opportunity matches.
- **Powered by OpenAI and CrewAI**: Utilizes OpenAI’s models through CrewAI for
  deep insights and personalized recommendations.
- **Scalable, Context-Aware Matching**: Efficiently organizes tasks to ensure
  each candidate receives the most relevant opportunities based on their unique
  profile.

ConektHub is built to grow with Rwanda’s talent and entrepreneurial ecosystem.
Join us in creating a smarter, AI-driven future for connecting opportunities and
people!

## Project Structure

```sh
├── LICENSE
├── README.md
├── outputs/
├── requirements.txt
└── src
 ├── __init__.py
 ├── config
 │   ├── agents.yaml
 │   └── tasks.yaml
 ├── crew.py
 ├── data
 │   ├── opportunities.csv
 │   └── talents.csv
 └── main.py
```

## Installation

1. **Clone the repository:**

```sh
git clone <https://github.com/barackm/conekthub.git>
cd <conekthub>
```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ```

## Usage

1. **Run the main script:**

   ```sh
   python src/main.py
   ```

2. **Candidate Profile:**

   - The candidate profile is loaded from `src/data/talents.csv`.
   - Modify the `index` parameter in the `run` function to select a different
     candidate.

3. **Opportunities:**
   - Opportunities are loaded from `src/data/opportunities.csv`.

## Project Components

### Agents

- **CSV Reader:** Reads and structures data from CSV files.
- **Talent Researcher:** Processes candidate profiles to find suitable matches.
- **Opportunity Hunter:** Searches for and summarizes relevant opportunities.

### Tasks

- **Read Opportunities Task:** Loads opportunities data from the CSV file.
- **Find Talent Matches Task:** Identifies relevant opportunities for the
  candidate.
- **Find Opportunities Task:** Refines and organizes the best opportunities.
- **Summarize Candidate Profile Task:** Summarizes the candidate’s profile.
- **Summarize Opportunities Task:** Summarizes the identified opportunities.

## Configuration

- **Agents Configuration:** `src/config/agents.yaml`
- **Tasks Configuration:** `src/config/tasks.yaml`

## Output

- **Opportunities Summary:** `outputs/opportunities_summary.txt`
- **Research Output:** `research_output.txt`
- **Blog Output:** `blog_output.txt`

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file
for details.
