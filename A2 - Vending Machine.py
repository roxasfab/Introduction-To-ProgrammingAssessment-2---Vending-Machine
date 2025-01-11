# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:30:38 2025

@author: roxas
"""

#Step 1: Display the items together with the item code and price for each item.
print("Welcome To Five Rice Vending Machine\n")

print("Product                 Code                Price\n")
print("\n")
print("CHIPS")
print("Oman Chips				101					AED 3.50")
print("Lays					102					AED 3.50")
print("Doritos 				103					AED 5.00\n")
print("CRACKERS & FLAVORED BISCUITS")
print("Oreo					201					AED 2.00")
print("Caprice Choc. Sticks	202					AED 10.00")
print("Ritz Crackers			203					AED 2.00\n")
print("CHOCOLATE BARS")
print("Kitkat					301					AED 2.50")
print("Snickers				302					AED 2.50")
print("Break Chocolate			303					AED 2.00\n")
print("DRINKING WATER")
print("Mai Dubai				401					AED 1.50")
print("Masafi					402					AED 2.00")
print("Star Carbonated			403					AED 2.00\n")
print("SOFT BEVERAGES")
print("Coca - Cola				501					AED 2.50")
print("Fanta					502				    AED 2.50")
print("Sprite					503				    AED 2.50\n")
print("JUICES")
print("Lacnor Orange Juice		601					AED 1.50")
print("Lacnor Apple Juice		602				    AED 1.50")
print("Lacnor Mango Juice		603					AED 1.50\n")
print("FLAVORED MILK")
print("Lacnor Strawberry Milk	701					AED 1.50")
print("Lacnor Chocolate Milk	702					AED 1.50")
print("Lacnor Banana Milk		703					AED 1.50\n")
print("\n")

#Step 2: Create a list of variables dedicated for each item.
omanchipsprice = 3.50
laysprice = 3.50
doritosprice = 5.00
oreoprice = 2.00
capricesticksprice = 10.00
ritzcrackersprice = 2.00
kitkatprice = 2.50
snickersprice = 2.50
breakchocolateprice = 2.00
maidubaiprice = 1.50
masafiprice = 2.00
starcarbonatedprice = 2.00
cocacolaprice = 2.50
fantaprice = 2.50
spriteprice = 2.50
lacnororangeprice = 1.50
lacnorappleprice = 1.50
lacnormangoprice = 1.50
lacnorstrawberryprice = 1.50
lacnorchocolateprice = 1.50
lacnorbananaprice = 1.50

#Step 3: Create a user input.
print("Please type a product code: ")
itemcode = int(input())

#Step 4: Create an IF condition to validate the user input.
if itemcode == 101:
    print("You have selected Oman Chips. Please pay AED 3.50")
    #Step 6(a): Create a variable for the amount inserted and use FLOAT function to classify the user input.
    paidamount = float(input())
    #Step6(b): Using IF & ELIF conditions, the following three scenarios should be applied:
    #1.If the paid amount is equal to the actual item price, print a statement that tells the customer that their transaction is successful and they can claim their purchased item.
    if paidamount == omanchipsprice:
        print("Purchase successful. Please claim your item below.")
    #2.If the paid amount is more than the actual item price, print a statement that tells the customer that their transaction is successful and they will receive a change together with the purchased item.
    elif paidamount > omanchipsprice:
        print("Purchase successful. Please claim your item and change below.")
    #3.If the paid amount is less than the actual item price, print a statement that tells the customer that their transaction is unsuccessful and will not be able to purchase the item.
    elif paidamount < omanchipsprice:
        print("Insufficient amount. Please insert the amount needed.")
        
#Step 5: Create an ELIF condition to allow other items to be available for purchasing.
elif itemcode == 102:
    print("You have selected Lays. Please pay AED 3.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == laysprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > laysprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < laysprice:
        print("Insufficient amount. Please insert the amount needed.")
        
elif itemcode == 103:
    print("You have selected Doritos. Please pay AED 5.00")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == doritosprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > doritosprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < doritosprice:
        print("Insufficient amount. Please insert the amount needed.")
        
elif itemcode == 201:
    print("You have selected Oreo. Please pay AED 2.00")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == oreoprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > oreoprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < oreoprice:
        print("Insufficient amount. Please insert the amount needed.")
        
elif itemcode == 202:
    print("You have selected Caprice Choc Sticks. Please pay AED 10.00")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == capricesticksprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > capricesticksprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < capricesticksprice:
        print("Insufficient amount. Please insert the amount needed.")
        
elif itemcode == 203:
    print("You have selected Ritz Crackers. Please pay AED 2.00")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == ritzcrackersprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > ritzcrackersprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < ritzcrackersprice:
        print("Insufficient amount. Please insert the amount needed.")
    
elif itemcode == 301:
    print("You have selected Kitkat. Please pay AED 2.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == kitkatprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > kitkatprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < kitkatprice:
        print("Insufficient amount. Please insert the amount needed.")
        
elif itemcode == 302:
    print("You have selected Snickers. Please pay AED 2.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == snickersprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > snickersprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < snickersprice:
        print("Insufficient amount. Please insert the amount needed.")
        
elif itemcode == 303:
    print("You have selected Break Chocolate. Please pay AED 2.00")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == breakchocolateprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > breakchocolateprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < breakchocolateprice:
        print("Insufficient amount. Please insert the amount needed.")
        
elif itemcode == 401:
    print("You have selected Mai Dubai. Please pay AED 1.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == maidubaiprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > maidubaiprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < maidubaiprice:
        print("Insufficient amount. Please insert the amount needed.")
    
elif itemcode == 402:
    print("You have selected Masafi. Please pay AED 2.00")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == masafiprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > masafiprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < masafiprice:
        print("Insufficient amount. Please insert the amount needed.")
    
elif itemcode == 403:
    print("You have selected Star Carbonated. Please pay AED 2.00")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == starcarbonatedprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > starcarbonatedprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < starcarbonatedprice:
        print("Insufficient amount. Please insert the amount needed.")
    
elif itemcode == 501:
    print("You have selected Coca - Cola. Please pay AED 2.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == cocacolaprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > cocacolaprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < cocacolaprice:
        print("Insufficient amount. Please insert the amount needed.")

elif itemcode == 502:
    print("You have selected Fanta. Please pay AED 2.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == fantaprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > fantaprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < fantaprice:
        print("Insufficient amount. Please insert the amount needed.")
    
elif itemcode == 503:
    print("You have selected Sprite. Please pay AED 2.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == spriteprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > spriteprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < spriteprice:
        print("Insufficient amount. Please insert the amount needed.")

elif itemcode == 601:
    print("You have selected Lacnor Orange Juice. Please pay AED 1.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == lacnororangeprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > lacnororangeprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < lacnororangeprice:
        print("Insufficient amount. Please insert the amount needed.")
    
elif itemcode == 602:
    print("You have selected Lacnor Apple Juice. Please pay AED 1.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == lacnorappleprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > lacnorappleprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < lacnorappleprice:
        print("Insufficient amount. Please insert the amount needed.")
        
elif itemcode == 603:
    print("You have selected Lacnor Mango Juice. Please pay AED 1.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == lacnormangoprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > lacnormangoprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < lacnormangoprice:
        print("Insufficient amount. Please insert the amount needed.")
    
elif itemcode == 701:
    print("You have selected Lacnor Strawberry Milk. Please pay AED 1.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == lacnorstrawberryprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > lacnorstrawberryprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < lacnorstrawberryprice:
        print("Insufficient amount. Please insert the amount needed.")
        
elif itemcode == 702:
    print("You have selected Lacnor Chocolate Milk. Please pay AED 1.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == lacnorchocolateprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > lacnorchocolateprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < lacnorchocolateprice:
        print("Insufficient amount. Please insert the amount neededd.")
    
elif itemcode == 703:
    print("You have selected Lacnor Banana Milk. Please pay AED 1.50")
    #User input for making payment.
    paidamount = float(input())
    #If paid amount is equal to the actual price.
    if paidamount == lacnorbananaprice:
        print("Purchase successful. Please claim your item below.")
    #If paid amount is more than the actual price.
    elif paidamount > lacnorbananaprice:
        print("Purchase successful. Please claim your item and change below.")
    #If paid amount is less than the actual price.
    elif paidamount < lacnorbananaprice:
        print("Insufficient amount. Please insert the amount needed.")