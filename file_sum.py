def file_sum(sums):
    total = 0
    with open(nums,'r') as my_file:
        for line in my_file:
            numbers=line.split(',')
            for num in numbers:
                total +=float(num)
    with open('sums','w') as outfile:
        outfile.write(str(total))
    my_file.close()
    outfile.close()
    return total
