import pytest
from unittest.mock import patch
from app import calculator

def test_calculator_addition():
    user_inputs = ['1', '10', '5']
    expected_output = "The result is: 15.0\n"
    with patch('builtins.input', side_effect=user_inputs), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_any_call(expected_output.strip())

def test_calculator_subtraction():
    user_inputs = ['2', '10', '5']
    expected_output = "The result is: 5.0\n"
    with patch('builtins.input', side_effect=user_inputs), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_any_call(expected_output.strip())

def test_calculator_multiplication():
    user_inputs = ['3', '10', '5']
    expected_output = "The result is: 50.0\n"
    with patch('builtins.input', side_effect=user_inputs), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_any_call(expected_output.strip())

def test_calculator_division():
    user_inputs = ['4', '10', '5']
    expected_output = "The result is: 2.0\n"
    with patch('builtins.input', side_effect=user_inputs), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_any_call(expected_output.strip())

def test_calculator_division_by_zero():
    user_inputs = ['4', '10', '0']
    expected_output = "Error! Division by zero."
    with patch('builtins.input', side_effect=user_inputs), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_any_call(expected_output)

def test_calculator_percentage():
    user_inputs = ['5', '50', '200']
    expected_output = "The result is: 25.0%"
    with patch('builtins.input', side_effect=user_inputs), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_any_call(expected_output)

def test_calculator_percentage_division_by_zero():
    user_inputs = ['5', '50', '0']
    expected_output = "Error! Division by zero."
    with patch('builtins.input', side_effect=user_inputs), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_any_call(expected_output)

def test_calculator_invalid_choice():
    user_inputs = ['6']
    expected_output = "Invalid choice! Please select a valid operation."
    with patch('builtins.input', side_effect=user_inputs), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_any_call(expected_output)

def test_calculator_invalid_numeric_input():
    user_inputs = ['1', 'a', '5']
    expected_output = "Invalid input! Please enter numeric values."
    with patch('builtins.input', side_effect=user_inputs), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_any_call(expected_output)