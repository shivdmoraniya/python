import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
import os
import numpy as np


output_dir="preparation_graphs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
sns.set_theme(style="whitegrid",context="talk",palette="muted")
sns.set_theme(style="whitegrid")

df=pd.read_csv('hospital_patients_40k.csv')

df['BMI']=df['Weight_kg']/((df['Height_cm']/100)**2)
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 17, 60, 120], labels=['Child', 'Adult', 'Senior'])
df['High_BP_Risk'] = np.where((df['Systolic_BP'] > 140) | (df['Diastolic_BP'] > 90), 'High Risk', 'Normal')
df['Stay_Category'] = pd.cut(df['Admission_Days'], bins=[0, 5, 15, 100], labels=['Short (<5)', 'Medium (6-15)', 'Long (>15)'])
df['Bill_Per_Day'] = df['Total_Bill_Amount'] / df['Admission_Days']

# Helper function to format and save plots consistently
def save_slide(p1, first, graph):
    plt.title(f"Slide {p1}: {first}", pad=20, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/{p1:02d}_{graph}.png", dpi=300)
    plt.close()
    print(f"Generated Slide {p1:02d}...")

print("Generating 40 Presentation-Ready Graphs. Please wait...\n")

# theme 1

plt.figure(figsize=(10, 6)); sns.histplot(df['Age'], bins=30, kde=True, color='skyblue'); save_slide(1, "Distribution of Patient Ages", "Age_Dist")
plt.figure(figsize=(8, 8)); df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', cmap='Set2', ylabel=''); save_slide(2, "Gender Breakdown", "Gender_Pie")
