from Source import Classes

debug_flag = True

myBoiler = Classes.Boiler("Boiler Object", debug_flag)
#myBoiler.my_method()

myOilBurner = Classes.OilBurner("Oil Burner Object")
myOilBurner.my_method()

myWoodBurner = Classes.WoodBurner("Wood Burner Object")
myWoodBurner.my_method()

myImmersion = Classes.Immersion("Immersion Object")
myImmersion.my_method()
