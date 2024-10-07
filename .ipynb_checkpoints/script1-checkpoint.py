import module1
import module2_int

lists = [
    module2_int.list_1,
    module2_int.list_2,
    module2_int.list_3,
    module2_int.list_4]

with open("results.txt", "w") as file:
    for numbers in lists:
        smallest1, smallest2 = module1.find_two_smallest(numbers)
        file.write(f"List: {numbers}\n Smallest: {smallest1}, Second smallest: {smallest2} \n\n")

print("Results saved to results.txt")