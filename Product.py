class Product:
    def __init__(self, Price, Item_Name, Weight, Brand, Cost):
        self.Price = Price
        self.Item_Name = Item_Name
        self.Weight = Weight
        self.Brand = Brand
        self.Cost = Cost
        self.Status = "for sale"

    def Sell(self):
        self.Status = "sold"

    def Add_tax(self):
        self.Price = self.Price + self.Price * .12

    def Defective(self):
        self.Price = 0

    def Return(self,reason):
        if reason == "Defective": 
            self.Price = 0

        elif reason == "OpenBox":
            self.Price * .8
        
        else:
            self.Status = "for sale"



    def displayinfo(self):
        print '{} {} {} {} {} {}'.format(self.Price, self.Item_Name, self.Weight, self.Brand, self.Cost, self.Status)


Product_1 = Product(10, 'pen', '10oz', 'zebra', 5)


Product_1.Add_tax()
Product_1.displayinfo()
