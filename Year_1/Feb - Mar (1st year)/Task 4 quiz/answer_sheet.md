# Task 4 Practice Quiz: Comprehensive Answer Key

This document provides the correct answers and the technical rationale for the questions found in the Task 4a and 4b revision quiz. Use this as a guide for understanding what examiners look for in a "Distinction" grade response.

---

## 🛠 Section 1: Task 4a – Developing the Solution

### 1. Data File Format
* **Correct Answer:** **B (.csv)**
* **Rationale:** Comma Separated Values (.csv) are the standard format for the ESP because they are lightweight and can be easily parsed by Python's `csv` module or `pandas`.

### 2. Modular Programming
* **Model Answer:** Breaking code into functions makes the solution easier to **test, debug, and maintain**.
* **Rationale:** It allows for "Unit Testing" (testing one function at a time). It also makes your code more readable for the examiner, as they can see exactly what each part of the script does without getting lost in a "wall of code."



### 3. Unit Testing
* **Correct Answer:** **A (Unit testing)**
* **Rationale:** Unit testing specifically checks the smallest "units" of code (functions or methods) in isolation to ensure they produce the correct output for a given input.

### 4. Error Handling (Missing Files)
* **Model Answer:** You should use **Exception Handling** (specifically `try...except` blocks).
* **Rationale:** Without this, the program will crash with a `FileNotFoundError`. Catching the exception allows the program to display a professional error message to the user instead of terminating.



### 5. Input Validation
* **Correct Answer:** **C (To prevent invalid or harmful data)**
* **Rationale:** Validation (like checking if a number is positive or if a string is not empty) ensures the program is **robust**. It prevents the logic from breaking when a user enters something unexpected.

### 6. Global Constants vs. Hard-coding
* **Model Answer:** Using a Global Constant allows you to update a value in **one single place** at the top of the script.
* **Rationale:** If you hard-code a file path inside five different functions and that path changes, you have to find and fix all five. A constant at the top makes the code "maintainable."

### 7. Time-Series Visualization
* **Correct Answer:** **B (A Line Graph)**
* **Rationale:** Line graphs are specifically designed to show **trends and patterns over time**. Pie charts show parts of a whole, but they are poor at showing change.



### 8. Internal Documentation (Comments)
* **Model Answer:** Comments act as a **roadmap** for your logic.
* **Rationale:** In Task 4b, you are required to explain *why* you wrote your code a certain way. If you commented your code well in 4a, you can quickly find the line numbers and logic you need to reference as evidence.

---

## 📝 Section 2: Task 4b – Reflective Evaluation

### 11. Purpose of Task 4b
* **Correct Answer:** **B (To evaluate and suggest improvements)**
* **Rationale:** Task 4b is not about writing more code; it is about reflecting on your work in 4a and proving you understand how it meets the client's needs.

### 12. The Three Areas of Justification
* **Model Answer:** You must justify the **System Requirements**, **User Requirements**, and **Future Developments**.
* **Rationale:** To hit the high-mark bands, you must address all three. System is about the "math/logic," User is about "usability," and Future is about "scaling/upgrading."



### 13. Core Data Trends
* **Correct Answer:** **B (Lunch and dinner services)**
* **Rationale:** Identifying patterns in service times is a specific technical requirement mentioned in the official ESP brief.

### 14. Supporting Your Claims
* **Model Answer:** Support claims with **specific evidence** such as code line numbers or screenshots of the UI.
* **Rationale:** General statements like "my code is good" get zero marks. You must prove it by saying, "As seen in lines 45-50, I implemented a loop that..."

### 15. Professional Evaluation Content
* **Correct Answer:** **A (Comparison against original requirements)**
* **Rationale:** A professional developer always maps their final product back to the "Success Criteria" defined at the start of the project.

### 16. Justifying Graphical Output
* **Model Answer:** Explain how the graph is **meaningful to the manager** and helps them make business decisions.
* **Rationale:** It isn't enough to say "I made a graph." You must say, "This bar chart allows the manager to instantly see which BBQ item is underperforming so they can adjust their stock."

### 17. Handling Limitations
* **Correct Answer:** **B (Note it as a non-functional improvement)**
* **Rationale:** Admitting your code has a flaw (like speed) and explaining *how* it could be fixed shows the examiner you have a high level of technical understanding.

### 18. Future UI Improvements
* **Model Answer:** Justify improvements through **Accessibility** (e.g., a GUI) or **Advanced Layouts** (e.g., using a library like `Rich`).
* **Rationale:** Technical justification means explaining *why* a change helps the user (e.g., "A GUI reduces the chance of user input errors compared to a CLI").

### 20. Quality Evaluation Comments
* **Correct Answer:** **A (Identifying optimization)**
* **Rationale:** Good evaluation comments are **specific** and **technical**. They identify exactly what could be improved (loops) and why (optimization).

---
*Generated for T-Level Core Digital ESP Revision*
