# This is a calculation module.

class cal:

    def cal_plus(self, *args):
        addition_result = 0
        for element in args:
            addition_result += element
        return addition_result


if __name__ == "__main__":
    my_cal = cal()
    print(my_cal.cal_plus(1, 2))



