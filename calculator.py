"""المطلوب:
اكتب برنامجًا بلغة Python يقوم بما يلي:

1. يطلب من المستخدم إدخال رقمين (num1 و num2).

2. يطلب من المستخدم اختيار العملية التي يريد تنفيذها:

الجمع (+)
الطرح (-)
الضرب (*)
القسمة (/)

3. يستخدم عبارات if / elif / else لتحديد العملية.


4. بعد عرض الناتج، استخدم عوامل المقارنة لتوضيح العلاقة بين الرقمين (أكبر، أصغر، متساوي).
      
 أفكار إضافية للطلاب المتقدمين:

أضف خيارًا لإعادة العملية دون إعادة تشغيل البرنامج.

استخدم شرطًا يتحقق إن كانت الأرقام سالبة أو موجبة.

أضف عملية جديدة مثل الأس (num1 ** num2)."""



print("Welcome to the calculator")
# اله حاسبة بسيطة
num1 =  float(input("Enter first number: "))
option = input("choose [+, -, *, / , ** , %, //,]" )
num2 = float(input("Enter second number: "))
    
if option == "+":
    
    result = num1 + num2
    print("The result is: ", result)
     
elif option == "-":
    
    result = num1 - num2
    print("The result is: ", result)
elif option == "*":
    
    result = num1 * num2
    print("The result is: ", result)
    
elif option == "/":
   
    result = num1 / num2
    print("The result is: ", result)

elif option == "**":
   
    result = num1 ** num2
    print("The result is: ", result)

elif option == "%":
   
    result = num1 % num2
    print("The result is: ", result)

elif option == "//":
   
    result = num1 // num2
    print("The result is: ", result)
else:
    print("Error")

#
# مقارنة الرقمين
if num1 > num2:
    print(f"{num1} > {num2}")
elif num1 < num2:
    print(f"{num1} < {num2}")
elif num1 == num2:
    print(f"{num1} == {num2}")

#التحقق من الارقام السالبة والموجبة



if num1 > 0 or num2 > 0:
    print(f"{num1 or num2} is positive")
elif num1 < 0 or num2 < 0:
    print(f"{num1 or num2} is negative")
elif num1 == 0 or num2 == 0:
    print(f"{num1 or num2} is zero")
else:
    print("Error")


 