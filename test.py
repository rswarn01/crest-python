import pandas as pd
import argparse


class Test:
    def result(self, file):
        try:
            columns = [
                "id",
                "first_name",
                "last_name",
                "email",
                "job_title",
                "basic_salary",
                "allowances",
                "Gross Salary",
            ]

            # Read the .dat file into a DataFrame
            # Adjust the parameters according to your file format
            # For example, specify the delimiter and column names if necessary
            df = pd.read_csv(
                file, delimiter="\t", header=None, names=columns, skiprows=1
            )

            # remove duplicates
            df.drop_duplicates(inplace=True)

            # change datatype into int.
            df["basic_salary"] = df["basic_salary"].astype(int)

            # calculate second heighest salary.
            second_highest_salary = df["basic_salary"].nlargest(2).iloc[-1]

            # Calculate the average salary
            average_salary = df["basic_salary"].mean().round(3)

            # Append the new row to the DataFrame
            new_row = {
                "id": "Second Highest Salary=" + str(second_highest_salary),
                "first_name": "average salary = " + str(average_salary),
                "last_name": "",
                "email": "",
                "job_title": "",
                "basic_salary": "",
                "allowances": "",
                "Gross Salary": "",
            }

            df = df.append(new_row, ignore_index=True)
            df.to_csv("output\\result.csv", index=False)

        except Exception as exc:
            return (500, "Failed to calculate data")


# Path to the .dat file
file_path = "input\\DATA1.dat"

# to pass file on command line.
if __name__ == "__main__":
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Process input CSV file")

    # Add argument for the input CSV file
    parser.add_argument("input_file", help="Path to the input CSV file")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the provided input CSV file
    test = Test()
    test.result(args.input_file)
