#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

# Assuming your crew class is named DataScienceTeam in data_science_team/crew.py
from data_science_team.crew import DataScienceTeam

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory for all 11+ artifacts
os.makedirs('output', exist_ok=True)

# The core requirements for the Iris project demonstration
requirements = """
Project: Iris Species Classification Demonstration.
1. The Data Engineer must fetch the Iris dataset using the custom IrisDataFetcher tool.
2. The Data Analyst must provide a statistical summary using the StatsSummaryTool.
3. The Data Scientist must train a classification model (Random Forest or similar).
4. The ML Engineer must save the model as 'iris_model.joblib' using the ModelPersistenceTool.
5. The Frontend Engineer must create 'app.py' using Gradio.
6. The app.py must load 'iris_model.joblib' and allow users to input sepal/petal dimensions 
   to predict if a flower is Setosa, Versicolor, or Virginica.
"""

project_name = "Iris_Classification_Demo"

def run():
    """
    Run the Data Science Team crew to generate the Iris project artifacts.
    """
    inputs = {
        'requirements': requirements,
        'project_name': project_name,
        'current_date': datetime.now().strftime("%Y-%m-%d")
    }

    print(f"### Starting the {project_name} Multi-Agent Workflow ###")
    
    # Create and run the crew
    result = DataScienceTeam().crew().kickoff(inputs=inputs)

    print("\n### Workflow Complete ###")
    print("Check the /output folder for the following artifacts:")
    print("- Strategy, Roadmap, and Architecture MD files")
    print("- iris_data.csv and iris_model.joblib")
    print("- app.py (The Gradio Interface)")
    print("- Ethical Review and Final Project Summary")

if __name__ == "__main__":
    run()