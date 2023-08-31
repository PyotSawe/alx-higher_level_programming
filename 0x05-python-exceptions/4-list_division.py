#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nw_list = []

    for i in range(list_length):
        try:
            nw_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            nw_list.append(0)
            print('division by 0')
            continue
        except IndexError:
            nw_list.append(0)
            print('out of range')
            continue
        except TypeError:
            nw_list.append(0)
            print('wrong type')
            continue
        finally:
            pass

    return nw_list
