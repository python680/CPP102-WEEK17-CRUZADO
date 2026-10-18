# Simulated Device Monitoring System

**Student Name:** Charles William E. Cruzado  
**Student Number** 2601345
**Section:** 1CpE-B

## Project Description

The Simulated Device Monitoring System is a terminal-based Python application designed to manage, classify, and analyze simulated device temperature readings. The system allows users to view existing readings, add new temperature values, classify readings according to predefined thresholds, and generate a statistical summary to evaluate the device's temperature status.

## Features

- View all stored temperature readings with indexed labels.
- Add a new temperature reading using whole numbers from 0 to 100.
- Classify each reading as NORMAL, WARNING, or CRITICAL.
- Generate a summary containing the total, average, minimum, and maximum temperatures.
- Display the number and percentage of readings in each classification category.
- Determine the overall monitoring status based on the recorded readings.
- Reject invalid menu choices and invalid temperature inputs.
- Handle keyboard interruptions and end-of-input situations.

## Requirements

- Python 3
- A terminal or code editor, such as Visual Studio Code

## How to Run

1. Open the project folder in Visual Studio Code.
2. Open the integrated terminal.
3. Run the following command:

   `python device_monitor.py`

   On macOS or Linux, you may use:

   `python3 device_monitor.py`

4. Choose an option from the menu by entering a number from 1 to 5.

## Sample Output

```text
SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 1

CURRENT READINGS
----------------
Reading 1: 28 °C
Reading 2: 31 °C
Reading 3: 35 °C
Reading 4: 37 °C
Reading 5: 29 °C
```

## Test Cases

The program can be tested using valid temperature readings, invalid inputs, menu selections, classification results, and summary calculations. Test results should be recorded in `test_cases.md` after the tests have been performed.

## Known Limitations

- Temperature readings are stored in memory and are not saved permanently to a file or database. The readings reset to their initial values when the program is restarted.
- The system accepts whole-number temperature readings only. Decimal values are not accepted.
- The program simulates device monitoring and does not collect temperature data from actual hardware.

## Reflection

This activity strengthened my understanding of modular programming in Python. Through the development of the system, I applied functions, loops, conditional statements, input validation, and return values to organize the program into manageable parts.

The activity also emphasized the importance of accurate calculations, threshold-based classification, and handling invalid inputs. Separating the program into functions made it easier to understand, maintain, and debug the code. Overall, this project demonstrated how structured programming and systematic testing contribute to software reliability and help prepare developers to build more dependable applications.
