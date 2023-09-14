# ValueError
The code works as inteded until the user is prompted "Enter the price of the purchase: ", once user inputs ValueError occurs.

Traceback (most recent call last):
  File "C:\Users\Matthew\IdeaProjects\untitled\Homework 1.py", line 95, in <module>
    main()
  File "C:\Users\Matthew\IdeaProjects\untitled\Homework 1.py", line 92, in main
    displayresult(total)
  File "C:\Users\Matthew\IdeaProjects\untitled\Homework 1.py", line 82, in displayresult
    print("Here is the Original Price Of Everything", format(total, '.2f'))
                                                      ^^^^^^^^^^^^^^^^^^^^
ValueError: Unknown format code 'f' for object of type 'str'

![Screenshot 2023-09-13 200133](https://github.com/Vaunty/ValueError/assets/68826427/a6fdd7aa-5e60-4ed1-a9d6-98bd58d83a0c)
