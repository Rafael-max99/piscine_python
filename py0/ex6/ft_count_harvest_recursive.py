#!/usr/bin/python3

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(count: int):
        if count > days:
            print("Harvest time!")
            return
        else:
            print(f"Day {count}")
            helper(count + 1)

    helper(1)
