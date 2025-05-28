# src/visualizer.py

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from src import config

def visualize_money_flow(fraud_only=True):
    """Visualize money flow graph from transaction data"""
    
    # Load data
    df = pd.read_csv(config.FRAUD_REPORT if fraud_only else config.FINAL_DATASET)

    # Create a graph
    G = nx.DiGraph()

    for _, row in df.iterrows():
        sender = f"{row['Sender UPI ID']} ({row['sender_bank']})"
        receiver = f"{row['Receiver UPI ID']} ({row['receiver_bank']})"
        amount = row['Amount (INR)']

        G.add_node(sender)
        G.add_node(receiver)

        G.add_edge(sender, receiver, weight=amount)

    # Position nodes
    pos = nx.spring_layout(G, k=0.5, iterations=50)

    # Draw nodes and edges
    plt.figure(figsize=(14, 10))
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")
    nx.draw_networkx_edges(G, pos, edge_color="red" if fraud_only else "gray", arrows=True)
    nx.draw_networkx_labels(G, pos, font_size=8)

    # Draw edge weights (amounts)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    edge_labels = {k: f"₹{v:.0f}" for k, v in edge_labels.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    plt.title("💸 Money Flow Graph - " + ("Fraudulent Only" if fraud_only else "All Transactions"))
    plt.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_money_flow(fraud_only=True)
