#code to compute the WADM 
# choice 1 & 2 = c1 and c2 respectively 
# factors 1, 2 & 3 = f1, f2 and f3 respectively 

c1 = input("your first choice: ")
c2 = input("your second choice: ")

f1 = input("1st factor: ")
f1_scale = input(f'rate {f1} on a scale of 1 to 10')

f2 = input("2nd factor: ")
f2_scale = input(f'rate {f2} on a scale of 1 to 10')

f3 = input("3rd factor: ")
f3_scale = input(f'rate {f3} on a scale of 1 to 10')

c1_f1 = input(f'rate {c1} based on {f1} on a scale of 1 to 10')
c1_f2 = input(f'rate {c1} based on {f2} on a scale of 1 to 10')
c1_f3 = input(f'rate {c1} based on {f3} on a scale of 1 to 10')
c2_f1 = input(f'rate {c2} based on {f1} on a scale of 1 to 10')
c2_f2 = input(f'rate {c2} based on {f2} on a scale of 1 to 10')
c2_f3 = input(f'rate {c2} based on {f3} on a scale of 1 to 10')

result_c1_f1 = int(f1_scale) * int(c1_f1)
result_c1_f2 = int(f2_scale) * int(c1_f2)
result_c1_f3 = int(f3_scale) * int(c1_f3)
result_c2_f1 = int(f1_scale) * int(c2_f1)
result_c2_f2 = int(f2_scale) * int(c2_f2)
result_c2_f3 = int(f3_scale) * int(c2_f3)

c1_result = int(result_c1_f1 + result_c1_f2 + result_c1_f3)
c2_result = int(result_c2_f1 + result_c2_f2 + result_c2_f3)

if int(c1_result) > int(c2_result):
    print(f'your preferred choice is: {c1} with a total score of: {c1_result}')
else:
    print(f'your preferred choice is: {c2} with a total score of: {c2_result}')
    

