import os
import pandas as pd

def analyze_personal_csv():
    print("PERSONAL BUDGET ANALYZER")
    
    file_path = input("Enter the path to your CSV expense file (e.g., expenses.csv): ").strip()

    if not os.path.exists(file_path):
        print("\n[!] File not found. Creating a sample 'my_expenses.csv' for you to test with...")
        sample_data = {
            "Category": ["Food", "Transport", "Food", "Entertainment", "Utilities", "Food"],
            "Amount": [25.50, 12.00, 45.00, 30.00, 85.00, 15.20],
            "Date": ["2026-03-01", "2026-03-01", "2026-03-02", "2026-03-03", "2026-03-04", "2026-03-05"]
        }
        pd.DataFrame(sample_data).to_csv("my_expenses.csv", index=False)
        file_path = "my_expenses.csv"
        print("Created 'my_expenses.csv' in your current directory!")

    # FILE_LOADING
    df = pd.read_csv(file_path)
    print("\nFile preview (First 3 rows):")
    print(df.head(3))

    # 3. PANDAS FUNDAMENTALS: CLEAN & PROCESS DATA
    # Ensure standard column names
    df.columns = df.columns.str.strip().str.title()
    
    if "Amount" not in df.columns or "Category" not in df.columns:
        print("\nError: The CSV file must contain at least 'Category' and 'Amount' columns.")
        return

    # Convert Amount column to numeric and drop invalid entries
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df = df.dropna(subset=["Amount"])

    # 4. PANDAS FUNDAMENTALS: GROUPBY & AGGREGATIONS
    summary = df.groupby("Category")["Amount"].agg(
        Total_Spent="sum",
        Average_Cost="mean",
        Transaction_Count="count"
    ).reset_index()

    summary = summary.sort_values(by="Total_Spent", ascending=False)

    # 5. GENERATE PERSONALIZED REPORT & EXPORT
    total_overall = df["Amount"].sum()
    top_category = summary.iloc[0]["Category"]

    print("\n" + "=" * 40)
    print("      YOUR PERSONAL BUDGET SUMMARY      ")
    print("=" * 40)
    print(f"Total Overall Expenditure: ${total_overall:.2f}")
    print(f"Top Spending Category:     {top_category}")
    print("\nCategory Breakdown:")
    print(summary.to_string(index=False))

    # Export report to CSV
    output_filename = "personalized_budget_report.csv"
    summary.to_csv(output_filename, index=False)
    print(f"\nReport saved to: {os.path.abspath(output_filename)}")

if __name__ == "__main__":
    analyze_personal_csv()
