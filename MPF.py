def calculate_mpf(salary, salary_growth_rate, mpf_rate, years, interest_rate):
    total_mpf = 0
    yearly_salary = salary * 12
    
    for year in range(years):
        if year >= 6: #salary increase 10% when year 2031 
            salary_growth_rate = 0.1
        
        # Calculate the yearly salary
        yearly_salary = yearly_salary * (1 + salary_growth_rate) 
        # Calculate the yearly MPF contribution (10% of monthly salary)
        
        if yearly_salary >= 360000: #MPF is capped 3000 monthly
            yearly_mpf = 3000 * 12 
        else:
            yearly_mpf = yearly_salary * mpf_rate  # MPF contribution for the year

        # Apply compound interest to the accumulated MPF
        total_mpf = total_mpf * (1 + interest_rate) + yearly_mpf
        
        print(f"year: {year + 1}")
        print(f"total_mpf: {yearly_mpf}")
        print(f"total_mpf: {total_mpf}")
       
    
    return total_mpf

# Initial parameters
salary = 15000            # Initial monthly salary (HKD)
salary_growth_rate = 0.05  # Annual salary growth rate (3%)
mpf_rate = 0.10           # MPF contribution rate (10% of monthly salary)
years = 40                # From age 25 to 65, total 40 years
interest_rate = 0.05      # Annual compound interest rate (5%)

# Calculate the final MPF balance after 40 years
final_mpf = calculate_mpf(salary, salary_growth_rate, mpf_rate, years, interest_rate)

print(f"After 40 years, Larry's MPF balance will be: {final_mpf:.2f} HKD")

