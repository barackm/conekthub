#!/usr/bin/env python
import sys
import os
import csv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.crew import TalentConnectionCrew 
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def load_candidate_profile_from_csv(csv_path, index=0):
    """Load a candidate profile from a CSV file, selecting the profile at the specified index."""
    with open(csv_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        candidates = list(reader)
        if candidates:
            selected_candidate = candidates[index]
            return {
                'name': selected_candidate.get("Name"),
                'location': selected_candidate.get("Location"),
                'skills': selected_candidate.get("Skills").split(", "),
                'experience_level': selected_candidate.get("Experience Level"),
                'industry': selected_candidate.get("Industry"),
                'current_role': selected_candidate.get("Current Role"),
                'interests': selected_candidate.get("Interests")
            }
        else:
            raise ValueError("No candidate profiles found in the CSV file.")


def run():
    candidate_profile = load_candidate_profile_from_csv('./src/data/talents.csv', index=6)
    print(candidate_profile)
    inputs = {
        'path_to_opportunities_csv': './src/data/opportunities.csv',
        'candidate_profile': candidate_profile
    }
    TalentConnectionCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
