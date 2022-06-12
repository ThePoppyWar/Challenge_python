from User import User


class VIPUser(User):
    def __init__(self, name, last_name, mail, vip_card_number):
        super().__init__(mail=mail, name=name, surname=last_name)
        if self._check_card(vip_card_number):
            self._vip_card_number = vip_card_number
        else:
            self._vip_card_number = None

    @staticmethod
    def _check_card(new_number):
        return new_number > 999 and new_number % 2 == 0

    @staticmethod
    def user_vip_card():
        return None

    @property
    def vip_card_number(self):
        return self._vip_card_number

    @vip_card_number.setter
    def vip_card_number(self, vip_card_number):
        if self._check_card(vip_card_number):
            self._vip_card_number = vip_card_number
        else:
            return None

User_1 = VIPUser('Kaska', 'Nowak', 'mail@mail', 5698)
print(User_1.vip_card_number)
print('______________________')
User_2 = VIPUser('Gocha', 'Focha', 'maila@maila', 12888)
print(User_2.vip_card_number)
print('______________________')