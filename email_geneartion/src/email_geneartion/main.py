import sys
import warnings
from datetime import datetime
from .doc_reader import read_document
from email_geneartion.crew import EmailGeneartion  # keep typo
from email_geneartion.email_sender import send_email  # ✅ NEW import

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    print("Enter the info you want to send an email about:")
    topic = input("➤ ")

    print("Enter path to the document (e.g., email_geneartion/docs/info.txt):")
    doc_path = input("➤ ")

    print("Enter recipient's email address:")
    to_email = input("➤ ")

    print("Enter your Gmail address:")
    from_email = input("➤ ")

    print("Enter your 16-character Gmail app password:")
    app_password = input("➤ ")

    # Read and prepare
    doc_text = read_document(doc_path)

    inputs = {
        "topic": topic,
        "doc_text": doc_text,
        "current_year": str(datetime.now().year)
    }

    try:
        EmailGeneartion().crew().kickoff(inputs=inputs)

        # ✅ After generation, send email
        with open("generated_email.txt", "r", encoding="utf-8") as f:
            lines = f.read().strip().splitlines()

        subject = lines[0].replace("Subject: ", "") if lines[0].lower().startswith("subject") else "Generated Email"
        body = "\n".join(lines)

        send_email(subject, body, to_email, from_email, app_password, attachments=[doc_path])

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
