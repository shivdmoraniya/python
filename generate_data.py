import pandas as pd
import random
from faker import Faker

# Initialize Faker (using Indian locales for realistic names/cities if preferred, or standard)
fake = Faker('en_IN') 

def generate_hospital_data(num_records=5000):
    departments = ['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'Oncology', 'Gynecology', 'General Medicine', 'Emergency']
    blood_groups = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
    genders = ['Male', 'Female', 'Other']
    doctors = ['Dr. Sharma', 'Dr. Gupta', 'Dr. Desai', 'Dr. Reddy', 'Dr. Krishnan', 'Dr. Verma', 'Dr. Patil', 'Dr. Nair']
    cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow']

    data = []

    for i in range(1, num_records + 1):
        record = {
            'Patient_ID': 10000 + i,
            'Patient_Name': fake.name(),
            'Age': random.randint(1, 90),
            'Gender': random.choices(genders, weights=[49, 49, 2])[0],
            'Blood_Group': random.choice(blood_groups),
            'Department': random.choice(departments),
            'City': random.choice(cities),
            'Doctor_Assigned': random.choice(doctors),
            
            # 10 Numeric Fields
            'Admission_Days': random.randint(1, 30),
            'Heart_Rate_BPM': random.randint(60, 120),
            'Systolic_BP': random.randint(90, 180),
            'Diastolic_BP': random.randint(60, 110),
            'Body_Temp_C': round(random.uniform(36.5, 39.5), 1),
            'Weight_kg': round(random.uniform(10.0, 120.0), 1), # Factoring in kids to adults
            'Height_cm': random.randint(90, 190),
            'Oxygen_Sat_pct': random.randint(85, 100),
            'Cholesterol_mgdl': random.randint(120, 300),
            'Total_Bill_Amount': round(random.uniform(5000.0, 500000.0), 2)
        }
        data.append(record)

    # Convert to Pandas DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    filename = 'data1.csv'
    df.to_csv(filename, index=False)
    print(f"Successfully generated {num_records} records and saved to '{filename}'.")

# Run the generator
if __name__ == "__main__":
    generate_hospital_data(40000)