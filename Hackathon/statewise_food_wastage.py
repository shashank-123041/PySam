#part of the program 'Hostel_food_wastage_management.py' done by repo owner (Shashank P R)

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import numpy as np
import platform
import subprocess

def graph_state_cooked_consumed_wasted(self):
    file_path = os.path.join(os.getcwd(), 'state_wise_food_wastage_analysis.csv')
    df = pd.read_csv(file_path)

    sns.set_style("whitegrid")

    df_melted = df.melt(id_vars=["State"], 
                        value_vars=["Total_Food_Cooked", "Total_Food_Consumed", "Total_Food_Wasted"], 
                        var_name="Category", 
                        value_name="Food Quantity (kg)")

    plt.figure(figsize=(12, 6))
    sns.barplot(x="State", y="Food Quantity (kg)", hue="Category", data=df_melted, palette="viridis")
    plt.title("Total Food Cooked, Consumed, and Wasted per State")
    plt.xlabel("State")
    plt.ylabel("Food Quantity (kg)")
    plt.xticks(rotation=90)
    plt.legend(title="Category")
    plt.show()

#Done by Shashank P R(1RN23CS191)
def graph_avg_food_waste_state(self):
    file_path = os.path.join(os.getcwd(), 'state_wise_food_wastage_analysis.csv')
    df = pd.read_csv(file_path)

    sns.set_style("whitegrid")

    df_melted = df.melt(id_vars=["State"], 
                        value_vars=["Total_Food_Cooked", "Total_Food_Consumed", "Total_Food_Wasted"], 
                        var_name="Category", 
                            value_name="Food Quantity (kg)")
    plt.figure(figsize=(10, 8))
    sns.barplot(y=df["State"], x=df["Avg_Wastage_Percentage"], palette="viridis")  
    plt.title("Average Percentage of Food Wasted per State", fontsize=14, fontweight="bold")
    plt.xlabel("Wastage Percentage (%)")
    plt.ylabel("State")
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.show()

graph_state_cooked_consumed_wasted()
graph_avg_food_waste_state()