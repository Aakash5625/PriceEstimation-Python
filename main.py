from tkinter import *
master = Tk()
master.geometry('700x530')
master.title('Used Products Price Estimation')


dam = None
ent = None
price_red = None
price = None
catopt = None



#calcuation function
def check():
    global price_red
    global price
    global catopt
    
    ent = e1.get()
    a = int(ent)
    price = a - (a / 100) * price_red
    show_answer(price)

    
#damage switch
def show_choice():
    global price_red
    global dam
    global catopt
    
    dam = v.get()
    if dam == 1:
        price_red = 40
    elif dam == 2:
        price_red = 50
    elif dam == 3:
        price_red = 60
    elif dam == 4:
        price_red = 70
    

#price update according to category
def category_update():
    global catopt
    global price_red
    
    if catopt == 'Electronics':
        price_red =  price_red + 20
    elif catopt == 'Books':
        price_red =  price_red + 5
    elif catopt == 'Furniture':
        price_red =  price_red + 10
    elif catopt == 'Vehicles':
        price_red =  price_red + 15
    return price_red


#result display function
def show_answer(price):
    blank.delete(0,'end')
    blank.insert(0, price)
    

#category input
def callback(selection):
    global catopt
    global price_red
    
    catopt = selection
    category_update()
    
    
#Damage entry
v = IntVar()
damage = [('None',1),('Minimal',2),('Moderate',3),('Considerable',4)]

Label(master, text = 'Level of Damage:',padx = 70,pady = 30, font = ('Times',15)).pack(anchor = W)

for val, damage_ in enumerate(damage):
    Radiobutton(master, text = damage_, padx = 50, variable = v, command = show_choice, value = val+1).pack(anchor = W)
    

#Selling price entry
Label(master,text = 'Current Selling Price:',font = ('Times',15), pady = 30).place(x = 300, y = 0)
e1 = Entry(master, font = ('Verdana',20))  
e1.place(x = 300, y = 85)


#categories option
categories = ['Electronics','Books','Furniture','Vehicles']
variable = StringVar(master)
variable.set("Choose")

Label(master,text = 'Categories:',font = ('Times',15), pady = 30).place(x = 300, y = 160)
w = OptionMenu(master, variable, *categories, command = callback).place(y = 185, x = 450)


#submit button
b = Button(master,text = 'Submit', height = 2, width = 30, command = check, bg = '#32CD32')
b.place(y = 270,x = 230)


#result view
Label(master, text = 'The estimated price is',padx = 20, pady = 10,font = ('Times',15)).place(y = 330, x = 230)
blank = Entry(master,font = ('Verdana',20))
blank.place(y = 390, x = 170)


#exit button
b1 = Button(master,text = 'Exit', height = 2, width = 30, command = master.destroy, bg = '#DC143C')
b1.place(y = 460,x = 230)
    
    
master.mainloop()
