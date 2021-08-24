# GUIbasic-Expense.py
from tkinter import * # improt libary ทั้งหมด
from tkinter import ttk, messagebox # ttk is theme of Tk
import csv
from datetime import datetime


GUI = Tk() # กำหนดให้ GUI คือ tkinter
GUI.title("โปรแกรมบันทึกค่าใช้จ่าย v.1.0 By Theeraphan's")
GUI.geometry('600x800+500+50')
# กำหนดขนาด กว้่าง x ยาว +ห่างจากแกน x ของจอ + ห่างจากแกน y ของจอ

# x0 = Button(GUI,text='Hello1')
# ประกาศตัวแปร x0 = สร้างปุ่มของ GUI ที่ text เเขียนว่า hello
# x0.pack(ipadx=50,ipady=20)
# pack() ติดปุ่มเข้ากับ GUI หลัก ตรงกลาง
# ipadx=20 เพิ่มขนาดของปุ้มในแนวแกน x

##############Menu###################
menubar = Menu(GUI) # menu หลัก
GUI.config(menu=menubar) #เอาไปแปะกับ GUI หลัก

# File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')

# help
def About():
	print('About Menu')
	messagebox.showinfo('About','สวัสดีครับ โปรแกรมนี้คือโปรแกรมบันทึกข้อมูลรายจ่าย \nสนใจบริจาคเราไหม? ขอแค่ 1 BTC ก็พอแล้ว\nBTC address: x0abc')

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)

# donate
def Donate():
	messagebox.showinfo('Donate','สนใจบริจาค\nBTC address: x0abcsadasdasdkljfksjgkldsg')

donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
donatemenu.add_command(label='Donate',command=Donate)
#####################################


Tab = ttk.Notebook(GUI)
T1 = Frame(Tab) #สามารถใส่ wide,hight ได้
T2 = Frame(Tab)
Tab.pack(fill= BOTH, expand=1) # fill=BOTH แปะกว้างทั้ง x,y expand=1 ทำให้เห็นหน้า

icon1 = PhotoImage(file='T1_expenses.png') # ภาพ 24x24 pixel
icon2 = PhotoImage(file='T2_list.png')




Tab.add(T1, text=f'{"ค่าใช้จ่าย":^{30}}',image=icon1,compound='top') # ใช้ fstring มาช่วย
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon2,compound='top')




F1 = Frame(T1)
#F1.place(x=100,y=50)
F1.pack() #อยู่ตรงกลางเสมอแม้ขยายหน้าจอ

days = {'Mon':'จันทร์',
			'Tue':'อังคาร',
			'Wed':'พุธ',
			'Thu':'พฤหัสบดี',
			'Fri':'ศุกร์',
			'Sat':'เสาร์',
			'Sun':'อาทิตย์'}



def save(event=None):
	expense = V_expense.get()
	price = V_price.get()
	quantity = V_quantity.get()

	if expense =='':
		print('No Data')
		messagebox.showwarning('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')#showpopup warning ขึ้นมาหลัง error
		return
	elif price =='':
		messagebox.showwarning('Error','กรุณากรอกราคา')#showpopup warning ขึ้นมาหลัง error
		return
	elif quantity =='':
		messagebox.showwarning('Error','กรุณากรอกจำนวนชิ้น')#showpopup warning ขึ้นมาหลัง error
		return


	try: # เป็นการสั่งให้ทดลองทำสิ่งที่อยู่ใน Try ถ้าทำแล้วไม่มีปัญหาก็ รันได้
		total = int(price) * int(quantity) #ต้องแปลงเป็น int ถึงจะ คูณได้
		# ถ้าเป็น float จะใส่ จุดทศนิยมได้ด้วย แต่ต้องประกาศตัวแปรข้างบน
		# .get() ดึงค่ามาจาก V_expense = StringVar()
		print('รายการ: {} ราคา : {}'.format(expense,price))
		print('จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total))
		text = 'รายการ: {} ราคา : {}\n '.format(expense,price)
		text = text + 'จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total)
		v_result.set(text)
		# clear ข้อมูลเก่า
		V_expense.set('')
		V_price.set('')
		V_quantity.set('')
		

		# บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
		today = datetime.now().strftime('%a') # day['Mon'] = 'จันทร์'
		print(today)
		dt = datetime.now().strftime('%y-%m-%d-%H:%M:%S')
		dt = days[today] + '-' + dt 
		with open('savedata.csv','a',encoding='utf-8',newline='') as f:
			 # with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
			 # 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
			 # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
			 fw = csv.writer(f) # สร้างฟังก์ชันสำหรับเขียนข้อมูล
			 data = [dt,expense,price,quantity,total]
			 fw.writerow(data)
			 E1.focus() # ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
		update_table() #update ข้อมูลหลังจากกด save

	except Exception as e:# แต่ถ้ารันไม่ได้จะไปรัน except แทน
		# Exception as e คือ เวลาที่ error ก็จะให้มัน print บอกว่า error อะไร
		print('ERROR,e')
		messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกข้อมูลผิด')#showpopup warning ขึ้นมาหลัง error
		#clear ข้อมูลเก่า
		V_expense.set('')
		V_price.set('')
		V_quantity.set('')

	 
# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',save) # ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = (None,20) # None เปลี่ยนเป็น 'Angsana New' ก็ได้

#------------image-----------

main_icon = PhotoImage(file='icon_shop.png')

Mainicon = Label(F1,image=main_icon)
Mainicon.pack()



#--------text1--------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
V_expense = StringVar()
# StringVar() คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=V_expense,font=FONT1)
E1.pack() # คำสั่งนำไปแปะ
#---------------------

#--------text2--------
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
V_price = StringVar()
# StringVar() คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=V_price,font=FONT1)
E2.pack() # คำสั่งนำไปแปะ
#---------------------

#--------text3--------
L = ttk.Label(F1,text='จำนวน (ชิ้น)',font=FONT1).pack()
V_quantity = StringVar()
# StringVar() คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=V_quantity,font=FONT1)
E3.pack() # คำสั่งนำไปแปะ
#---------------------


icon_b1 = PhotoImage(file='B_save.png') 

x1 = ttk.Button(F1,text=f'{"Save": >{10}}',image=icon_b1,compound='left',command = save)
x1.pack(ipadx=50,ipady=20,pady=20)

v_result = StringVar()
v_result.set('---------ผลลัพท์---------')
result = ttk.Label(F1,textvariable=v_result,font=FONT1,foreground='Green')

result.pack(pady=20)


################TAB2####################

def read_csv():

	with open('savedata.csv',newline='',encoding='utf-8') as f:
		fr = csv.reader(f)
		data = list(fr)
	return data
	#เป็นการส่งค่าที่เราอ่านแล้วไปยังที่ๆเราต้องการ

# table

L = ttk.Label(T2,text='ตารางแสดงผลลัพท์ทั้งหมด',font=FONT1).pack(pady=10)

header = ['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=30)
resulttable.pack()

# for i in range(len(header)):
# 	resulttable.heading(header[i],text=header[i]) 
	#ตัวไหนที่ซ้ำกันควรทำการ reference
	#และ ใช้ for loop / นับด้วย len ก่อน เพื่อดึงข้อมูลมาใส่

for h in header:
	resulttable.heading(h,text=h)
# หรือแบบนี้ก็ได้จะง่ายกว่า

# ความกว้างของ Colume [ระยะ]
headerwidth = [150,170,80,80,80]
for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w)

# ใส่ข้อมูลลงในตาราง
#resulttable.insert('','end',value=['จันทร์','น้ำดื่ม',30,5,150])


# update ตาราง
def update_table():
	resulttable.delete(*resulttable.get_children()) #เป็นการสั่ง delete อัตโนมัติ
	# for c in resulttable.get_children():
	# 	resulttable.delete(c)
	data = read_csv()
	for d in data :
		resulttable.insert('',0,value=d)



update_table()








GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop() #ให้โปรแกรมรันตลอดเวลา
