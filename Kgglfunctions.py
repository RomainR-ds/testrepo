# Define the function
def add_three(input_var):
    output_var = input_var + 3
    return output_var

# Run the function with 10 as input
new_number = add_three(10)

# Check that the value is 13, as expected
print(new_number)


# Naming functions / more complex example // taxes calculations
def get_pay(num_hours):
    pay_aftertax = num_hours * 15 * 0.88
    return pay_aftertax

# Calculate pay based on working 40 hours
pay_fulltime = get_pay(40)
print(pay_fulltime)
pay_parttime = get_pay(32)
print(pay_parttime)

#Functions with multiple arguments
def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    #pretax pay
    pay_pretax = num_hours * hourly_wage
    #aftertax pay
    pay_aftertax = pay_pretax * ( 1 - tax_bracket )
    return pay_aftertax
higher_pay_aftertax = get_pay_with_more_inputs(40, 24, .22)
print(higher_pay_aftertax)
same_pay_fulltime = get_pay_with_more_inputs(40, 15, .12)
print(same_pay_fulltime)

# Define the function with no arguments and with no return
def print_hello():
    print("Hello, you!")
    print("Good morning!")
    
# Call the function
print_hello()