'''
This module contains functions for converting
between degrees Fahrenheit and degrees Celsius
'''

def to_celsius(fahrenheit: float) -> float:
    '''
    Input: fahrenheit, a float value representing a current temperature in fahrenheit
    Output: A float value representing the converted temperature to celsius
    '''
    return (fahrenheit - 32) * 5.0 / 9 # Instead of 5/9, use 5.0/9 because that is needed for other languages like Java

def to_fahrenheit(celsius: float) -> float:
    '''
    Input: celsius, a float value representing a current temperature in celsius
    Output: A float value representing the converted temperature to fahrenheit
    '''
    return celsius * 9.0 / 5 + 32 # Instead of 9/5, use 9.0/5 to be more like Java.