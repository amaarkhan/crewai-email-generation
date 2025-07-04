#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from email_geneartion.crew import EmailGeneartion  # keep typo to match folder

from .doc_reader import read_document

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew with user input and document path.
    """
    print("Enter the info you want to send an email about:")
    topic = input("➤ ")

    print("Enter path to the document (e.g., docs/info.txt):")
    doc_path = input("➤ ")

    doc_text = read_document(doc_path)  # Read .txt, .pdf, or .docx content

    inputs = {
        "topic": topic,
        "doc_text": doc_text,
        "current_year": str(datetime.now().year)
    }

    try:
        EmailGeneartion().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    from .doc_reader import read_document  # Needed here too
    doc_text = read_document("sample_docs/sample.txt")

    inputs = {
        "topic": "Training Email",
        "doc_text": doc_text,
        "current_year": str(datetime.now().year)
    }

    try:
        EmailGeneartion().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    try:
        EmailGeneartion().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    from .doc_reader import read_document
    doc_text = read_document("sample_docs/sample.txt")

    inputs = {
        "topic": "Testing Email",
        "doc_text": doc_text,
        "current_year": str(datetime.now().year)
    }

    try:
        EmailGeneartion().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
