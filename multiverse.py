import requests
import json
import datetime
from qiskit import *
from qiskit.visualization import plot_histogram

def print_colorful_header():
    print(r"""
█░█░█░█░░░█░█░█░░░█░█
░█░█░█░█░░░█░█░█░█░░░█░█
░░█░░░█░█░░░░█░░░█░█░░░█░█

       .
      / \
     / _ \
  /\/_/ \_\/\
  \/__\_/__\/
    /_/\_\
     \_\/\_/
       \_/
    """)

def display_history_data(month, day, year):
    response = requests.get(f"http://history.muffinlabs.com/date/{month}/{day}")
    data = json.loads(response.text)
    print(f"{year} in History:")
    print("Events:")
    events = data["data"]["Events"]
    for event in events:
        if event["year"] == year:
            print(f"  {event['text']}")
    return events

def generate_answers(events):
    num_events = len(events)

    qr = QuantumRegister(3)
    cr = ClassicalRegister(3)
    qc = QuantumCircuit(qr, cr)

    qc.h(qr)

    qc.measure(qr, cr)

    backend = Aer.get_backend("qasm_simulator")
    result = backend.run(qc, shots=1000).result()

    counts = result.get_counts()

    answers = {
        "Our Universe": [],
        "Multiverse A": [],
        "Multiverse B": [],
        "Multiverse C": [],
        "Multiverse D": []
    }

    for scenario in counts:
        probability = counts[scenario] / 1000
        for i, e in enumerate(scenario[::-1]):
            if e == "1":
                answers[list(answers.keys())[i]].append(events[i]["text"])

    return answers

def main():
    print_colorful_header()
    print("If there's a chance we can calculate infinite multiverses, here's an attempt to start calculating the roads not traveled. Let's begin!")

    user_input = input("Would you like to enter a specific date and time (y/n)? ")
    if user_input.lower() == "y":
        month = input("Enter the month (1-12): ")
        day = input("Enter the day (1-31): ")
        year = input("Enter the year: ")
        events = display_history_data(month, day, year)

        answers = generate_answers(events)
        print("\nQuantum Multiverse:")
        for universe, scenarios in answers.items():
            print(f"{universe}: ")
            for i, scenario in enumerate(scenarios):
                print(f"  Event {i + 1}: {scenario}")
    else:
        print("You decided not to enter a specific date and time.")

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()

    