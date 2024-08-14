# Housing Prices Predictor Repo
## Week 1 Overview

    The housing price predictor repository will house an application that will predict the house prices given historic data. In Homework 1, we will be setting up a GitHub rep to house the application which we will build in the following weeks. The homeowrk will emphasize collaboration using GitHub and excerise Git skills learned.

## Road Map

    1. GitHUb Desktop/CLI/VSCode
    2. Cloning a repo
    3. Forking a repo
    4. Branching
    5. Adding/modifying a repo
    6. Staging changes
    7. Commiting
    8. Push/Fetch/Pull
    9. Creating a pull request
    10. Code Reviews
    11. GitHub Workflows
    12. Documentation

## Software/Accesses needed

    1. Visual Studio Code
    2. GitHub Desktop
    3. Git
    4. Python

## How To Run

    1. Clone the Repository:
        Open VS Code.
        Press Ctrl+Shift+P and type Git: Clone.
        Paste the repository URL (https://github.com/lorr010/housing_price_predictor) and choose a folder to clone the repository.

    2. Open the Project:
        Once cloned, VS Code will ask to open the folder. Click "Open".

    3. Install Dependencies:
        Open a terminal in VS Code (`Ctrl+``).
        Navigate to the project folder if not already there.
        Run the command pip install -r requirements.txt to install the necessary dependencies.

    4. Run the Code:
        Locate the main script (e.g., main.py).
        Run it using the terminal with python main.py or by clicking the run button in VS Code.


## Week 2  Overview  

    You will be required to develop a command-line application using the "Home Prices" dataset from Week 1. The application should be capable of reading and writing data from a file and utilize Object-Oriented Programming (OOP) techniques and data manipulation in Python to perform Create, Read, Update, and Delete (CRUD) operations.  


## Task 1: Project Setup and Basic Structure  

    - Use GitHub repository created in Week 1. Create a new branch for this week so that the name has the prefix of ‘Week2_YourInitial_’ and check out that branch. 

    - Initialize the project including necessary folders, files and confirm the Python is installed on the machine.  

    - Data file for download  

    - data.xlsx 

        my-app/ 
        
        ├─ housing_price_predictor/ 
        
        ├─ src/ 
        
        │  ├─ utils/	 
        
        │  ├─ classes/ 
        
        ├─ tests/ 

## Task 2: Reading and Writing Data  

    - Develop a function for reading the "Home Prices" dataset from a file. 

    - def  read_from_file(file_name: str) -> []: 

    - Implement a function to write data back to the file.  

    - def write_to_file(file_name:str, content: str) -> None: 

## Task 3: Object-Oriented Programming  

    - Design and implement classes representing the dataset. Include methods to perform CRUD operations.  

    - Create the House class including a number of fields including id, neighborhood, house_style, overall_condition, year_built, roof_type, roof_material, foundation_material, heating, central_air, electrical, fireplace_num, garage_area, date_sold (MM/YYYY) 

    - Create a dictionary with key-value pairs from “id” to House instances 

## Task 4: Data Manipulation  

    - Implement methods to filter, update, and delete specific records in the dataset.   

    - def update_house_by_id(self, house_id->int, updated_fields: {}) -> None or def updated_house(self, updated_data->{})-> None 

    - def delete_house_by_id(self, house_id) -> None 

    - def get_houses_by_filters(self, filters: []) -> [] 

## Task 5: Add Test Cases   

    - Utilizing Pytest for writing unit test cases. 

    - Write at least one test for each of the created functions 

 
