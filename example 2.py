known_allergies = {"Aspirin", "Ibuprofen", "Penicillin"}

# List to store all patients
patient_list = []

# Function to create a patient record
def add_patient(patient_number):
    # Tuple for patient ID
    patient_id = ("PAT", patient_number)

    name = input("Enter patient name: ")
    age = int(input("Enter age: "))

    # List for symptoms
    symptoms = input("Enter symptoms (comma-separated): ").split(",")
    symptoms = [s.strip().capitalize() for s in symptoms]

    # Set for medications (unique items)
    meds = input("Enter medications (comma-separated): ").split(",")
    medications = set(m.strip().capitalize() for m in meds)

    # Allergy check using set intersection
    risk = medications & known_allergies  # same as: medications.intersection(known_allergies)

    # Dictionary to store the patient's data
    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "symptoms": symptoms,
        "medications": medications,
        "allergy_risk": list(risk) if risk else None
    }

    # Add to the list
    patient_list.append(patient)

# Function to display all patients
def show_patients():
    print("\n--- Patient Records ---")
    for p in patient_list:
        print(f"\nID: {p['id']}")
        print(f"Name: {p['name']}, Age: {p['age']}")
        print("Symptoms:", ", ".join(p["symptoms"]))
        print("Medications:", ", ".join(p["medications"]))
        if p["allergy_risk"]:
            print("Allergy Risk:", ", ".join(p["allergy_risk"]))
        else:
            print("No allergy risks.")

# Main program
def main():
    count = 1
    while True:
        print("\n1. Add Patient")
        print("2. Show Patients")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_patient(count)
            count += 1
        elif choice == '2':
            show_patients()
        elif choice == '3':
            print("Exiting system...")
            break
        else:
            print("Invalid input. Try again.")


main()

