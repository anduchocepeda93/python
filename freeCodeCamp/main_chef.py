from Chef import Chef
print("This is the regular chef:")
myChef = Chef()
myChef.make_chicken()
myChef.make_salad()
myChef.make_special_dish()

print("\nThis is the Chinese chef:")
from Chinese_chef import ChineseChef
myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_salad()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()
