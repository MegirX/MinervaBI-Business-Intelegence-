import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk

# Load data
file_path = r'C:\Users\For Students\Downloads\bi_survey_data.csv'
df = pd.read_csv(file_path)

# ===============================
# Define graph functions
# ===============================
def graph_1():
    fig, ax = plt.subplots(figsize=(8,6))
    role_distribution = df["respondent_role"].value_counts(normalize=True) * 100
    sns.barplot(x=role_distribution.index, y=role_distribution.values, palette="viridis", ax=ax)
    ax.set_title("Graph 1: Respondent Roles Distribution (%)")
    ax.set_ylabel("Percentage")
    plt.xticks(rotation=45)
    plt.tight_layout()
    fig.canvas.manager.set_window_title("Graph 1")
    plt.show()

def graph_2():
    fig, ax = plt.subplots(figsize=(8,6))
    company_size_distribution = df["company_size"].value_counts(normalize=True) * 100
    sns.barplot(x=company_size_distribution.index, y=company_size_distribution.values, palette="magma", ax=ax)
    ax.set_title("Graph 2: Company Size Distribution (%)")
    ax.set_ylabel("Percentage")
    plt.xticks(rotation=45)
    plt.tight_layout()
    fig.canvas.manager.set_window_title("Graph 2")
    plt.show()

def graph_3():
    fig, ax = plt.subplots(figsize=(10,6))
    industry_distribution = df["industry_sector"].value_counts()
    sns.barplot(x=industry_distribution.index, y=industry_distribution.values, palette="coolwarm", ax=ax)
    ax.set_title("Graph 3: Industry Sector Distribution")
    ax.set_ylabel("Number of Respondents")
    plt.xticks(rotation=45)
    plt.tight_layout()
    fig.canvas.manager.set_window_title("Graph 3")
    plt.show()

def graph_4():
    fig, ax = plt.subplots(figsize=(8,6))
    ab_testing = df.groupby("dashboard_version").agg({
        "usability_score": "mean",
        "conversion_impact": "mean"
    })
    ab_testing.plot(kind="bar", ax=ax, color=["#1f77b4", "#ff7f0e"])
    ax.set_title("Graph 4: Dashboard A/B Testing Results")
    ax.set_ylabel("Average Score")
    plt.xticks(rotation=0)
    plt.tight_layout()
    fig.canvas.manager.set_window_title("Graph 4")
    plt.show()

def graph_5():
    fig, ax = plt.subplots(figsize=(8,6))
    trend_summary = df.groupby("company_size").agg({"adoption_intent": "mean"})
    trend_summary["adoption_intent"].plot(kind="bar", color="#2ca02c", ax=ax)
    ax.set_title("Graph 5: Adoption Intent by Company Size")
    ax.set_ylabel("Average Adoption Intent")
    plt.xticks(rotation=45)
    plt.tight_layout()
    fig.canvas.manager.set_window_title("Graph 5")
    plt.show()

def graph_6():
    fig, ax = plt.subplots(figsize=(8,6))
    risk_factors = df[df["privacy_concern"] == "high"]
    risk_summary = risk_factors["company_size"].value_counts()
    sns.barplot(x=risk_summary.index, y=risk_summary.values, palette="Reds", ax=ax)
    ax.set_title("Graph 6: High Privacy Concern by Company Size")
    ax.set_ylabel("Number of Companies")
    plt.xticks(rotation=45)
    plt.tight_layout()
    fig.canvas.manager.set_window_title("Graph 6")
    plt.show()

# ===============================
# Tkinter GUI
# ===============================
root = tk.Tk()
root.title("📊 MinervaBI Graph Viewer")
root.geometry("350x450")
root.configure(bg="#2C3E50")

# Header
header_frame = tk.Frame(root, bg="#34495E", pady=15)
header_frame.pack(fill="x")
header_label = tk.Label(
    header_frame, 
    text="MinervaBI Graph Viewer", 
    font=("Helvetica", 18, "bold"), 
    fg="white", 
    bg="#34495E"
)
header_label.pack()

# Instruction
instr_label = tk.Label(
    root, 
    text="Click a button to view a graph", 
    font=("Helvetica", 12), 
    fg="white", 
    bg="#2C3E50"
)
instr_label.pack(pady=15)

# Buttons
button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack(pady=10)

buttons = [
    ("Graph 1", graph_1),
    ("Graph 2", graph_2),
    ("Graph 3", graph_3),
    ("Graph 4", graph_4),
    ("Graph 5", graph_5),
    ("Graph 6", graph_6)
]

for text, func in buttons:
    b = tk.Button(
        button_frame, 
        text=text, 
        command=func, 
        font=("Helvetica", 12, "bold"), 
        bg="#1ABC9C", 
        fg="white", 
        activebackground="#16A085", 
        activeforeground="white",
        width=25,
        pady=5
    )
    b.pack(pady=5)

# Footer
footer_label = tk.Label(
    root, 
    text="MinervaBI Project – Data Visualization", 
    font=("Helvetica", 10), 
    fg="white", 
    bg="#2C3E50"
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()
