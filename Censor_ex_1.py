# Napisz funkcję censor, która przyjmie jako parametr dowolnie długi łańcuch tekstowy. Następnie:
# -rozbije łańcuch tekstowy na listę wyrazów,
# -sprawdzi, czy nie znajdują się w nim słowa niedozwolone,
# -jeśli tak -- zamieni je na cztery gwiazdki (****)
# -ponownie połączy listę w string i zwróci wartość.""

def censor(tekst):
    list1 = ["Java", "C#", "Ruby", "PHP"]
    tekst_censor = " ".join(["****" if i in list1 else i for i in tekst.split()])
    return tekst_censor


c = censor("Java is the best, but PHP is the bestest!")  # ;-)
print(c)


