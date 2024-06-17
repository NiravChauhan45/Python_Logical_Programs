# Exercise:21 extract the email service provider name

email_list = ["niravc324@gmail.com","chauhannirav713@gmail.com","niravchauhan837@gmail.com"] 

for i in email_list:
 i=i.replace("@",".").split(".")
 print(i[1])
