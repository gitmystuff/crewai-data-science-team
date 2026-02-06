# 🌸 Agentic AI: End-to-End Iris Species Classification

Welcome to the DataScienceTeam Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

---

## 🚀 Project Overview

This project demonstrates a fully autonomous, **multi-agent AI workforce** designed to manage the entire Machine Learning lifecycle. Rather than a single script, this repository is the output of 12 specialized agents collaborating to take a raw dataset and transform it into a production-ready, ethically audited, and architecturally sound software product.

---

## 🤖 The Agentic Workforce

The project was built by a "Crew" of AI agents, each assigned a specific role, goal, and set of tools.

### **Leadership & Strategy**

* **Chief Data Officer (CDO):** Defined the high-level data strategy, focusing on data integrity, governance, and organizational alignment.
* **Product Manager:** Conducted user research for botanists, drafted the product roadmap, and defined the features for the Gradio interface.
* **AI Ethicist:** Conducted a comprehensive audit for algorithmic bias, transparency, and regulatory compliance (GDPR/CCPA).

### **Engineering & Architecture**

* **Data Architect:** Designed the system blueprint, including normalized schemas for raw data, feature sets, and interaction logs.
* **Data Engineer:** Built the ETL pipeline log, documenting the cleaning, validation, and standard scaling processes.
* **Frontend Engineer:** Developed the interactive Gradio interface to bridge the gap between complex ML models and end-users.
* **MLOps Engineer:** Established the deployment manifest and monitoring configuration, including drift thresholds and CI/CD triggers.

### **Science & Analysis**

* **Data Analyst:** Performed deep statistical analysis, identifying key differentiators (Petal Length/Width) and distribution skews.
* **Data Scientist:** Evaluated multiple models (Random Forest, Decision Trees, SVM), ultimately selecting the **SVM model (97.78% accuracy)** for deployment.
* **Technical Writer:** Consolidated agent outputs into the professional documentation suite you see in the `output/` folder.

---

## 🛠️ Tools & Technologies

### **The AI Orchestration Stack**

* **CrewAI:** The primary framework used to orchestrate agent tasks and handoffs.
* **Claude 3.7 Sonnet & GPT-4o:** The "brains" behind the agents, providing high-reasoning capabilities for strategy and code.

### **The Machine Learning Stack**

* **Python 3.10+:** The core programming language.
* **Scikit-Learn:** Used for training the SVM classifier and the `StandardScaler`.
* **Pandas & NumPy:** For data manipulation and statistical verification.
* **Joblib:** For model serialization and persistence.

### **The Deployment Stack**

* **Gradio:** For the interactive web interface.
* **Hugging Face Spaces:** The hosting environment for the live demo.
* **GitHub:** Version control and security monitoring (Secret Scanning).

---

## 📊 Key Findings

* **Model Accuracy:** The Support Vector Machine (SVM) achieved a **97.78% accuracy** rate, outperforming Random Forest and Decision Trees.
* **Feature Importance:** Statistical analysis confirmed that **Petal Dimensions** are the most critical features for distinguishing between Versicolor and Virginica species.
* **Ethics:** The model was found to have zero bias against protected demographic groups as it relies solely on botanical measurements, though continuous monitoring is recommended.

---

## 📂 Project Structure

* `src/`: The agentic logic and task definitions.
* `config/`: Configuration files for the AI agents.
* `output/`: The professional documentation suite (Strategy, Ethics, Performance Reports).
* `app.py`: The live production code for the Gradio interface.
* `*.joblib`: The serialized model and scaler artifacts.

---

**Live Demo:** [View the Botanist Interface on Hugging Face](https://huggingface.co/spaces/colab-user4567/iris-botanist-ai)

---

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/data_science_team/config/agents.yaml` to define your agents
- Modify `src/data_science_team/config/tasks.yaml` to define your tasks
- Modify `src/data_science_team/crew.py` to add your own logic, tools and specific args
- Modify `src/data_science_team/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the data_science_team Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The data_science_team Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the DataScienceTeam Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

