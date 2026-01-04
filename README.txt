Cell Phone Management System
============================

This application manages information about cell phones imported by a company.
It is designed for use by Marketing and Engineering teams.
The system focuses on data-structure–centered design and object-oriented principles.

--------------------------------
Requirements
--------------------------------
- Python 3.x

--------------------------------
Files Included
--------------------------------
- cellphone.py           : Defines the CellPhone class
- inventory_manager.py   : Manages phone records using a dictionary
- main.py                : Demonstrates system functionality
- phones.json            : Exported data file
- README.txt             : Instructions and documentation

--------------------------------
How to Run the Program
--------------------------------
1. Open Command Prompt
2. Navigate to the project folder:
   cd Desktop\CellPhoneManagement
3. Run the program:
   python main.py

--------------------------------
Features Implemented
--------------------------------
- Add new cell phones
- Remove phones by model
- Update stock quantity
- Search by model number
- Aggregate queries (total stock value, count by brand)
- Export inventory data to JSON

--------------------------------
Design Notes
--------------------------------
- A dictionary (hash map) is used to store cell phones using model number as the key.
- This allows fast search, update, and delete operations.
- The design supports scalability and maintainability.

--------------------------------
Author
--------------------------------
Name: K.D Umadi Alanka Munasinghe