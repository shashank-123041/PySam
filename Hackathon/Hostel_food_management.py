import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import numpy as np
import platform
import subprocess

def open_documentations():
    file_path = os.path.join(os.getcwd(), 'Enhanced_Hostel_Food_Wastage_Management_Documentation.docx')
    if platform.system() == 'Windows':
        os.startfile(file_path)  #Windows
    elif platform.system() == 'Darwin':
        subprocess.call(('open', file_path))  #macOS
    else:
        subprocess.call(('xdg-open', file_path))  #Linux

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class Hostel_food_wastage_managemnet:

    #Done by Shashank P R(1RN23CS191)
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
    
    #Done by Mayur B(1RN23CD059)
    def graph_food_consumption_vs_wastage(self):
        file_path = os.path.join(os.getcwd(),'food_wastage_sheet.csv')
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        required_columns = ['Total Food Prepared (kg)', 'Food Served (kg)', 'Food Wasted (kg)']
        total_prepared = df['Total Food Prepared (kg)'].sum()
        total_consumed = df['Food Served (kg)'].sum()
        total_wasted = df['Food Wasted (kg)'].sum()
        labels = ['Food Consumed', 'Food Wasted']
        sizes = [total_consumed, total_wasted]
        colors = ['#2E8B57', '#FF6347']
        plt.figure(figsize=(7, 7))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})
        plt.title("Food Consumption vs Wastage")
        plt.show()

    #Done by Roshini R(1RN23CS173)
    def graph_meal_waste(self):
        file_path = os.path.join(os.getcwd(),'food_wastage_data.csv')
        data=pd.read_csv(file_path)
        meal_prepared=data["Meal Prepared"]
        food_wasted=data["Food Wasted (kg)"]
        plt.figure()
        plt.bar(meal_prepared,food_wasted)
        plt.xlabel("Meal")
        plt.xticks(rotation=45, fontsize=10)
        plt.ylabel("Food Wasted [kg]")
        plt.show()

    #Done by Roshini R(1RN23CS173)
    def graph_cuisine_waste(self):
        file_path = os.path.join(os.getcwd(),'food_wastage_data.csv')
        data=pd.read_csv(file_path)
        cuisine_waste = data.groupby("Type of Cuisine")["Food Wasted (kg)"].sum()
        plt.figure()
        plt.pie(cuisine_waste,labels=cuisine_waste.index,autopct="%3.2f%%")
        plt.title("Food Wastage by Type of Cuisine")
        plt.axis()
        plt.show()

    #Done by Roshini R(1RN23CS173)
    def graph_meal_category_3d(self):
        file_path = os.path.join(os.getcwd(),'food_wastage_data.csv')
        data=pd.read_csv(file_path)
        column_name = "Food Wasted (kg)" 
        meal_waste = data.groupby("Meal Type")[column_name].sum().reset_index()

        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection="3d")

        x_pos = np.arange(len(meal_waste))
        y_pos = np.zeros(len(meal_waste)) 
        z_pos = np.zeros(len(meal_waste)) 

        dx = np.ones(len(meal_waste)) * 0.5  
        dy = np.ones(len(meal_waste)) * 0.5 
        dz = meal_waste[column_name]  

        colors = ["red", "blue", "green"] 

        ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=colors, alpha=0.8)

        ax.set_xlabel("Meal Type")
        ax.set_ylabel(" ")
        ax.set_zlabel("Food Wasted (kg)")
        ax.set_title("Food Wastage by Meal Category")
        ax.set_xticks(x_pos)
        ax.set_xticklabels(meal_waste["Meal Type"])
        plt.show()

    #Done by Prasad Reddy(1RN23CI039)
    def graph_reasons_for_waste(self):
        file_path = os.path.join(os.getcwd(),"food_wastage_sheet.csv")
        df = pd.read_csv(file_path)
        waste_reason_counts = df['Reasons for Waste'].value_counts()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=waste_reason_counts.index, y=waste_reason_counts.values, palette="viridis")
        plt.xlabel("Reasons for Food Waste")
        plt.ylabel("Number of Occurrences")
        plt.title("Reasons for Food Wastage in Hostels")
        plt.xticks(rotation=30, ha='right')
        plt.show()

    #Done by Prasad Reddy(1RN23CI039)
    def student_feedback():

        file_path = os.path.join(os.getcwd(),"food_wastage_sheet.csv")
        df = pd.read_csv(file_path)
        feedback_counts = df['Student Feedback'].value_counts()

        plt.figure(figsize=(10, 6))
        sns.barplot(x=feedback_counts.index, y=feedback_counts.values, palette="coolwarm")
        plt.xlabel("Student Feedback")
        plt.ylabel("Number of Responses")
        plt.title("Student Feedback on Hostel Food")
        plt.xticks(rotation=30, ha='right')
        plt.show()

    #Done by Anish U(1RN23CS027)
    def graph_food_quality_rating(self):
        #Average food quality rating
        file_path = os.path.join(os.getcwd(),"data2.csv")
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip().str.replace("'", "")
        df = df[~df['Date'].str.contains("#", na=False)]
        df['Date'] = pd.to_datetime(df['Date'].str.strip("'"), errors='coerce')
        df['QualityCheck'] = pd.to_numeric(df['QualityCheck'], errors='coerce')
        df['HostelName'] = df['HostelName'].str.strip("'")
        df['MealType'] = df['MealType'].str.strip("'")
        df['MealType'] = df['MealType'].replace({'Breakfast': 'Morning'})
        grouped = df.groupby(['MealType', 'HostelName'])['QualityCheck'].mean().reset_index()
        plt.figure(figsize=(10, 6))
        sns.barplot(data=grouped, x='MealType', y='QualityCheck', hue='HostelName', palette='Set2')
        plt.title('Average Food Quality Rating per Hostel by Meal Time')
        plt.xlabel('Meal Time')
        plt.ylabel('Average Food Quality Rating')
        plt.legend(title='Hostel Name', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

    #Done by Anish U(1RN23CS027)
    def graph_transport_cost(self):
        #Average Transportation Cost Incurred for Different NGOs
        file_path = os.path.join(os.getcwd(),"data2.csv")
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip().str.replace("'", "", regex=True)
        df['NGOName'] = df['NGOName'].str.strip().str.replace("'", "", regex=True)
        df['CostIncurred'] = pd.to_numeric(df["CostIncurred"].str.strip().str.replace("'", "", regex=True))
        cost_by_ngo = df.groupby('NGOName')['CostIncurred'].sum().reset_index()
        plt.figure(figsize=(10, 6))
        plt.bar(cost_by_ngo['NGOName'], cost_by_ngo['CostIncurred'], color='skyblue')
        plt.xlabel('NGO Name')
        plt.ylabel('Average Cost Incurred(in Rupees)')
        plt.title('Average Transportation Cost Incurred for Different NGOs')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    #Done by Anish Udupa N(1RN23CS027)
    def graph_leftover_quantity(self):
        #Average Leftover Quantity per Hostel
        file_path = os.path.join(os.getcwd(),"data2.csv")
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip().str.replace("'", "")
        df = df[~df['Date'].str.contains("#", na=False)]
        df['Date'] = pd.to_datetime(df['Date'].str.strip("'"), errors='coerce')
        df['LeftoverQty'] = pd.to_numeric(df['LeftoverQty'], errors='coerce')
        df['HostelName'] = df['HostelName'].str.strip("'")
        avg_leftover_per_hostel = df.groupby('HostelName')['LeftoverQty'].mean()
        plt.figure(figsize=(10, 6))
        avg_leftover_per_hostel.plot(kind='bar', color='skyblue')
        plt.title('Average Leftover Quantity per Hostel')
        plt.xlabel('Hostel Name')
        plt.ylabel('Average Leftover Quantity')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    #Done by Anish U(1RN23CS027)
    def graph_ngo_feedback(self):
        #NGO feedback
        file_path = os.path.join(os.getcwd(),"data2.csv")
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip().str.replace("'", "")
        df = df[~df['Date'].str.contains("#", na=False)]
        df['NGOName'] = df['NGOName'].str.strip().str.replace("'", "")
        df['NGOFeedback'] = df['NGOFeedback'].str.strip().str.replace("'", "")
        feedback_counts = df.groupby(['NGOName', 'NGOFeedback']).size().reset_index(name='Count')
        plt.figure(figsize=(12, 7))
        sns.barplot(data=feedback_counts, x='NGOName', y='Count', hue='NGOFeedback', palette='viridis')
        plt.title('NGO Feedback Distribution per NGO')
        plt.xlabel('NGO Name')
        plt.ylabel('Feedback Count')
        plt.xticks(rotation=45)
        plt.legend(title='Feedback')
        plt.tight_layout()
        plt.show()

    #Done by Anish U(1RN23CS027)
    def graph_transport_mode_usage(self):
        #Transport Mode Usage for Donations
        file_path = os.path.join(os.getcwd(),"data2.csv")
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip().str.replace("'", "")
        df['TransportMode'] = df['TransportMode'].str.strip().str.replace("'", "")
        transport_counts = df['TransportMode'].value_counts()
        plt.figure(figsize=(8, 8))
        plt.pie(transport_counts, labels=transport_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title('Transport Mode Usage for Donations')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

def main():
    obj = Hostel_food_wastage_managemnet()
    while True:
        clear_screen()
        print("\nFood Wastage Management System")
        print("1. State-wise Food Wastage Analysis")
        print("2. Hostel Food Wastage Analysis")
        print("3. Food Wastage Prevention Steps")
        print("4.Documentations")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                sys.exit("Program terminated!!")

            elif choice == 1:
                while True:
                    clear_screen()
                    print("\n--- State-wise Food Wastage Analysis ---")
                    print("1. Total Food Cooked, Consumed, and Wasted per State (Bar Graph)")
                    print("2. Average Percentage of Food Wasted per State (Horizontal Bar Graph)")
                    print("0. Go Back to Main Menu")

                    sub_choice = int(input("Enter your choice: "))
                    if sub_choice == 1:
                        obj.graph_state_cooked_consumed_wasted()
                    elif sub_choice == 2:
                        obj.graph_avg_food_waste_state()
                    else:
                        break

            elif choice == 2:
                while True:
                    clear_screen()
                    print("\n--- Hostel Food Wastage Analysis ---")
                    print("1. Food Consumption vs Wastage (Pie Chart)")
                    print("2. Food Wastage by Meal (Bar Graph)")
                    print("3. Food Wastage by Cuisine Type (Pie Chart)")
                    print("4. Food Wastage by Meal Category (3D Bar Graph)")
                    print("5. Reasons for Food Waste (Bar Graph)")
                    print("0. Go Back to Main Menu")

                    sub_choice = int(input("Enter your choice: "))
                    if sub_choice == 1:
                        obj.graph_food_consumption_vs_wastage()
                    elif sub_choice == 2:
                        obj.graph_meal_waste()
                    elif sub_choice == 3:
                        obj.graph_cuisine_waste()
                    elif sub_choice == 4:
                        obj.graph_meal_category_3d()
                    elif sub_choice == 5:
                        obj.graph_reasons_for_waste()
                    else:
                        break

            elif choice == 3:
                while True:
                    clear_screen()
                    print("\n--- Food Wastage Prevention Steps ---")
                    print("1. Average Food Quality Rating per Hostel (Bar Graph)")
                    print("2. Average Transportation Cost for NGOs (Bar Graph)")
                    print("3. Average Leftover Quantity per Hostel (Bar Graph)")
                    print("4. NGO Feedback Distribution (Bar Graph)")
                    print("5. Transport Mode Usage for Donations (Pie Chart)")
                    print("0. Go Back to Main Menu")

                    sub_choice = int(input("Enter your choice: "))
                    if sub_choice == 1:
                        obj.graph_food_quality_rating()
                    elif sub_choice == 2:
                        obj.graph_transport_cost()
                    elif sub_choice == 3:
                        obj.graph_leftover_quantity()
                    elif sub_choice == 4:
                        obj.graph_ngo_feedback()
                    elif sub_choice == 5:
                        obj.graph_transport_mode_usage()
                    else:
                        break

            elif choice==4:
                open_documentations()
            else:
                print("Invalid choice! Please enter a valid option.")
        except ValueError:
            print("Please enter a valid integer choice.")



if __name__ == "__main__":
    main()