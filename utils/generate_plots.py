import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define paths
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
KEY_DETAILS_CSV = os.path.join(BASE_PATH, 'data', 'key_details.csv')
PLOTS_DIR = os.path.join(BASE_PATH, 'plots')

# Ensure plots directory exists
os.makedirs(PLOTS_DIR, exist_ok=True)

def generate_thesis_timeline_plot(df):
    fig, ax = plt.subplots(figsize=(10, 2))
    
    date_str = df[df['detail_key'] == 'Date']['detail_value'].iloc[0]
    
    # Convert to datetime objects for plotting
    thesis_date = pd.to_datetime(date_str, format='%B %d, %Y')
    
    # Create a simple timeline
    ax.plot([thesis_date, thesis_date], [0, 0], marker='o', linestyle='-', color='blue')
    ax.text(thesis_date, 0.1, f'Submission: {date_str}', ha='center', va='bottom')
    
    ax.set_title('Master Thesis Timeline')
    ax.set_yticks([]) # Hide y-axis
    ax.set_xlabel('Date')
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, 'thesis_timeline.png'))
    plt.close()

def generate_concept_map_plot():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.text(0.5, 0.5, 'Concept Map Placeholder\n(Data Modeling Ontology, Cyber Intelligence, Smart Grids, Reinforcement Learning)',
            horizontalalignment='center', verticalalignment='center', fontsize=12, color='gray')
    ax.set_title('Thesis Concept Map (Placeholder)')
    ax.axis('off')
    plt.savefig(os.path.join(PLOTS_DIR, 'concept_map.png'))
    plt.close()

def generate_cyber_threat_landscape_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.text(0.5, 0.5, 'Cyber Threat Landscape Placeholder\n(Smart Grid Vulnerabilities, Attack Vectors, Anomaly Detection)',
            horizontalalignment='center', verticalalignment='center', fontsize=12, color='gray')
    ax.set_title('Smart Grid Cyber Threat Landscape (Placeholder)')
    ax.axis('off')
    plt.savefig(os.path.join(PLOTS_DIR, 'cyber_threat_landscape.png'))
    plt.close()

if __name__ == '__main__':
    try:
        key_details_df = pd.read_csv(KEY_DETAILS_CSV)
        generate_thesis_timeline_plot(key_details_df)
        generate_concept_map_plot()
        generate_cyber_threat_landscape_plot()
        print("Plots generated successfully.")
    except Exception as e:
        print(f"Error generating plots: {e}")
