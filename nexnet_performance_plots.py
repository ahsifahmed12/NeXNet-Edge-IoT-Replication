import matplotlib.pyplot as plt
import numpy as np

# 1. FIG 4(a): END-TO-END LATENCY COMPARISON
def plot_latency():
    systems = ['Existing WSN (Cloud)', 'NeXNet (Edge-AI)']
    latency_values = [6.5, 0.4]  # Values from Section IV-A
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(systems, latency_values, color=['#d9534f', '#5cb85c'])
    
    plt.ylabel('Average Latency (seconds)')
    plt.title('Fig 4(a): End-to-End Alert Latency Comparison')
    plt.ylim(0, 8)
    
    # Adding data labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval}s', ha='center', fontweight='bold')
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('fig4a_latency.png')
    plt.show()

# 2. FIG 4(b): NETWORK RESILIENCE (PDR OVER TIME)
def plot_resilience():
    # Simulating a node failure at T=30s and recovery by T=45s
    time = np.arange(0, 101, 10) 
    pdr = [98, 97, 98, 45, 88, 92, 94, 95, 96, 96, 97] # Significant drop at failure
    
    plt.figure(figsize=(8, 5))
    plt.plot(time, pdr, marker='o', linestyle='-', color='#0275d8', linewidth=2, label='Packet Delivery Rate')
    
    # Highlight failure and recovery points
    plt.annotate('Node Failure', xy=(30, 45), xytext=(10, 30),
                 arrowprops=dict(facecolor='red', shrink=0.05))
    plt.annotate('Self-Healing Complete (15s)', xy=(45, 90), xytext=(50, 70),
                 arrowprops=dict(facecolor='green', shrink=0.05))
    
    plt.xlabel('Time (seconds)')
    plt.ylabel('PDR (%)')
    plt.title('Fig 4(b): Network Resilience and Self-Healing Performance')
    plt.axhline(y=90, color='r', linestyle='--', label='90% Reliability Threshold')
    
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.savefig('fig4b_resilience.png')
    plt.show()

if __name__ == "__main__":
    plot_latency()
    plot_resilience()
