#here we have developed to find out the Repeat Customer of a Particular brand using Reports of that Particular brand
#Complex Logic & Python modules have been used

import pandas as pd
data= pd.read_csv("file_1.csv")
#data = pd.read_excel("16th_Excel.xlsx")
#Tackle no>12 or no.<12 digits
print(data.columns)
data.fillna('',inplace = True)
main_count =  0
li_phone = []
li_name = []
li11 = []
li12 = []
"""
prod_var = 'Product Name'
name_var = 'Customer Name'
phone_var = 'Customer Mobile'
"""
prod_var = 'Item Type Name'
name_var = 'Billing Address Name'
phone_var = 'Shipping Address Phone'
product =['product1','product2','product3','product4']
for count in range(len(data[prod_var])):
    if data[prod_var][count] == product[0] or data[prod_var][count] == product[1] or data[prod_var][count] == product[2] or data[prod_var][count] == product[3]:
        if data[phone_var][count] != '' and data[phone_var][count] in li11 and data[phone_var][count] not in li12 and 'cip' not in str(data[phone_var][count]):
            main_count+=1
            li11.append(data[phone_var][count])
            li_phone.append('91'+str(data[phone_var][count]))
            li_name.append(data[name_var][count])
            li12.append(data[phone_var][count])
        else:
            li11.append(data[phone_var][count])


"""
for count in range(len(data[prod_var])):
    if data[prod_var][count]=="Nursing Moms Milk Multi Jaggery Choco Spread" or data[prod_var][count]=="Women Stop Hair Fall Masala Spread" or data[prod_var][count]=="Women Fertility Booster Masala Spread" or data[prod_var][count]=="Men Fertility Booster Masala Spread" or data[prod_var][count]=="Bye Bye Age Plum Niacinamide Facedropsd" or data[prod_var][count]=="Ready Steady Glow Guava Botanical Facedrops":
   # if data[prod_var][count]=='Kids and Teens Brain Booster Chocolate Spread' or data[prod_var][count]=='Kids & Teens Brain Booster Chocolate Spread 500gm' or data[prod_var][count]=='Kids & Teens Brain Booster Chocolate Spread 1000gm' or data[prod_var][count]=='Kids & Teens Brain Booster Veggies and Dal powder' or data[prod_var][count]=='Kids & Teens Brain Booster Savoury Spread':# or :
        if data[phone_var][count] not in li100:
            li100.append(data[phone_var][count])
        else:
            if data[phone_var][count] in li11 and data[phone_var][count] not in li22:
                li22.append(data[phone_var][count])
                li_name.remove(li_name[li_phone.index('91'+str(data[phone_var][count]))])
                li_phone.remove('91'+str(data[phone_var][count]))
"""
print('CCCCCCC - ',len(li_name))

data1=pd.DataFrame()
for count in range(len(li_phone)):
    if '.' in li_phone[count]:
        li_phone[count] = (li_phone[count].split('.'))[0]

li_phone= [x.replace(' ','') for x in li_phone]

li_phone_ = []
for x in li_phone:
   if '910' in str(x):
       if len(x)>12:
           y = x.replace('0','',1)
           li_phone_.append(y)
       else:
           li_phone_.append(x)
   else:
       li_phone_.append(x)

li100 = []
li22 = []
"""
li_final_phone = []
li_final_name = []
for count in range(len(li_name)):
    if li_phone_[count] in li100 and li_phone_[count] not in li_final_phone:
        li_final_name.append(li_name[count])
        li_final_phone.append(li_phone_[count])
    else:
        li100.append(li_phone[count])
"""
li_final_phone = li_phone_
li_final_name = li_name
print('Name  - ',len(li_final_phone))
li_name_final = []
li_phone_final = []
for count in range(len(li_final_phone)):
    if len(str(li_final_phone[count]))==12:
        li_phone_final.append(li_final_phone[count])
        li_name_final.append(li_final_name[count])
print('FINAL - ',len(li_name_final))
data1['name'] = li_name_final
data1['phone'] = li_phone_final
data1.to_excel('9_may_1.xlsx',index = False)
"""
data = pd.read_csv('1_.csv')
li1 = []
li2 = []
for x in data['Shipping Address Phone']:
    if x in li1:
        li2.append(x)
    else:
        li1.append(x)
li2 = list(set(li2))
print('repeat - ',len(li2))
print(data.columns)
count = 0
li3 = []
for main_count in range(len(data['Total Price'])):
    if data['Shipping Address Phone'][main_count] not in li3:
        if int(data['Total Price'][main_count])>1750:
            li3.append(data['Shipping Address Phone'][main_count])
            count+=1
print(count)
"""