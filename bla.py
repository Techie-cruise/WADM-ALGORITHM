#code to compute the WADM 
# choice 1 & 2 = c1 and c2 respectively 
# factors 1, 2 & 3 = f1, f2 and f3 respectively 

c1 = input("your first choice: ")
c2 = input("your second choice: ")

f1 = input("1st factor: ")
f1_scale = input("rate factor 1 on a scale of one to ten ")

f2 = input("2nd factor: ")
f2_scale = input("rate factor 2 on a scale of one to ten ")

f3 = input("3rd factor: ")
f3_scale = input("rate factor 3 on a scale of one to ten ")

c1_f1 = input("rate " + c1 + " based on " +  f1 + " on a scale of one to ten ")
c1_f2 = input("rate " + c1 + " based on " +  f2 + " on a scale of one to ten ")
c1_f3 = input("rate " + c1 + " based on " +  f3 + " on a scale of one to ten ")
c2_f1 = input("rate " + c2 + " based on " +  f1 + " on a scale of one to ten ")
c2_f2 = input("rate " + c2 + " based on " +  f2 + " on a scale of one to ten ")
c2_f3 = input("rate " + c2 + " based on " +  f3 + " on a scale of one to ten ")

result_c1_f1 = int(f1_scale) * int(f2_scale)
result_c1_f2 = int(f1_scale) * int(f2_scale)
result_c1_f3 = int(f1_scale) * int(f2_scale)
result_c2_f1 = int(f1_scale) * int(f2_scale)
result_c2_f2 = int(f1_scale) * int(f2_scale)
result_c2_f3 = int(f1_scale) * int(f2_scale)

c1_result = c1_f1 + c1_f2 + c1_f3
c2_result = c2_f1 + c2_f2 + c2_f3

if int(c1_result) > int(c2_result):
    print("your preferred choice is: " + c1 + "with a total score of: " + str(c1_result))
else:
    print("your preferred choice is: " + c2 + "with a total score of: " + str(c2_result))
    

