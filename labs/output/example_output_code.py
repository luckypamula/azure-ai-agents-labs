import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# solution plan
# i. Filter data for Carreterra in Germany for December
# ii. Extract profit information
# iii. Plot the profit

def plot(data: pd.DataFrame):
    # Filter data for Carreterra in Germany for December
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data = data[pd.notna(data['Date'])]
    filtered_data = data[(data['Product'] == 'Carretera') & (data['Country'] == 'Germany') & (data['Month Name'] == 'December')]
    
    # Extract profit information
    profit = filtered_data['Profit'].sum()
    
    # Plot the profit
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=['Carretera'], y=[profit], palette='viridis')
    ax.axhline(profit, color='red', linestyle='--', label=f'Profit: {profit:.2f}')
    ax.legend()
    plt.xlabel('Product')
    plt.ylabel('Profit')
    plt.title('What was the profit for Carreterra in Germany for Dec?', wrap=True)
    
    return plt

chart = plot(data)