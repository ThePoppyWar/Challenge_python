def validate_pesel(pesel):
    pesel = str(pesel)
    suma_pesel = (
                (1 * int(pesel[0])) + (3 * int(pesel[1])) + (7 * int(pesel[2])) + (9 * int(pesel[3])) + (1 * int(pesel[4])) + (3 * int(pesel[5])) + (
                    7 * int(pesel[6])) + (9 * int(pesel[7])) + (1 * int(pesel[8])) + (3 * int(pesel[9])))
    result = 10 - (suma_pesel % 10)
    if result == int(pesel[10]):
        return True
    else:
        return False

check_pesel_1 = 75051948487
print(validate_pesel(check_pesel_1))
print('+++++++++++++++++++++++++++')
check_pesel_2 = 77110518767
print(validate_pesel(check_pesel_2))
print('+++++++++++++++++++++++++++')
check_pesel_3 = 44051401358
print(validate_pesel(check_pesel_3))