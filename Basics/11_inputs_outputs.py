# برنامج بسيط يأخذ اسم المستخدم في البداية ويقوم بطباعة رسالة تحية
# بعد رسالة التحية يطلب من المستخدم ان يقوم بإدخال رقمين ثم جمعهم ويطبع النتيجة

name = input("Enter your name: ") # الحصول على اسم المستخدم
print(f"Hello {name}") # طباعة رسالة تحية للمستخدم

first_number = input("Enter the first number: ") # استلام الرقم الاول 
second_number = input("Enter the second number: ") # استلام الرقم الثاني

print(f"result: {float(first_number) + float(second_number)}") # طباعة ناتج جمع الارقام



