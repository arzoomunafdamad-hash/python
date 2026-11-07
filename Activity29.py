class Italy:
    def capital(self):
        print("Capital: Rome")

    def language(self):
        print("Language: Italian")

    def country_type(self):
        print("Type: Beautiful Mediterranean Country with Rich History and Culture")



class Azores:
    def capital(self):
        print("Capital: Ponta Delgada")

    def language(self):
        print("Language: Portuguese")

    def country_type(self):
        print("Type: Island Region of Portugal with Stunning Landscapes")

obj_italy = Italy()
obj_azores = Azores()


for country_obj in(obj_italy, obj_azores):
    country_obj.capital()
    country_obj.language()
    country_obj.country_type()





