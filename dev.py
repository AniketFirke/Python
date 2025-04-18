{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Data_Types_Operators.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WdDeRs8nwsse"
      },
      "source": [
        "<b><h1>Data Types and Operators</h1></b>\n",
        "<h4>Welcome to this lesson on Data Types and Operators! You'll learn about:\n",
        "</h4>\n",
        "\n",
        "* **Data Types:** Integers, Floats, Booleans, \n",
        "Strings, Lists, Tuples, Sets, Dictionaries\n",
        "\n",
        "* **Operators:** Arithmetic, Assignment, Comparison, Logical, Membership, Identity\n",
        "\n",
        "* Built-In Functions, Compound Data Structures, Type Conversion\n",
        "\n",
        "* Whitespace and Style Guidelines"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PR-M6YwHxkoW"
      },
      "source": [
        "<br><br>\n",
        "\n",
        "<h2><b>1. Print() function in python:</b></h2>\n",
        "\n",
        "You will be seeing this print function very frequently in python programming. It helps us to see what exactly is happening in our code.\n",
        "\n",
        "Try to run the next lines of code and see what happens next:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "x_R9bFHvvu1f"
      },
      "source": [
        "2+7\n",
        "2*7"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_nKLdWFIyZt-"
      },
      "source": [
        "* You will see that even though you had written 2 lines of code only the last line of code gets seen in the output area.\n",
        "\n",
        "Now this happens because you haven't told python what to alctually do with it.\n",
        "\n",
        "This is where *print()* comes in. *print()* in python is a useful builtin function that we can use to display input value as text in the output. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p2xPUnXMyYA7"
      },
      "source": [
        "print(2+7)\n",
        "print(2*7)"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZoMyiceiJTAp"
      },
      "source": [
        "print('Hello World!!!!')"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uVi1mZvCCuSV"
      },
      "source": [
        "<br><br>\n",
        "\n",
        "## **4. Variables:**<br>\n",
        "Understanding variables is very important in any programming language they are used all the time in python. Using variables in place of direct numbers have many advantages. Variables are used to store information to be referenced and manipulated in a computer program.\n",
        "\n",
        "Creating a new variable in python is very simple, lets create one together, here in this example below the variable name is *month*, the equal sign is the assignment operator and the value of the variable is 12."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kIeQxFP67CNX"
      },
      "source": [
        "month=12\n",
        "print(month)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hfgtXMqGDI2l"
      },
      "source": [
        "Now its your turn create a variable named *rent* with its value being 1700"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "slBwG5njDHik"
      },
      "source": [
        "# create and print the varibale rent down below"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dCgFMQt8Dc6a"
      },
      "source": [
        "##### Expected output:<br>1700"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ESJS8yE9J0zB"
      },
      "source": [
        "In any case, whatever term is on the left side, is now a name for whatever value is on the right side. Once a value has been assigned to a variable name, you can access the value from the variable name.\n",
        "\n",
        "For example if we run this code we will get 3 as the output here as in the first line we assigned 3 to *a* and in the second line we assigned *a* to *b* so when we print *b* we get 3 as the output."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0Kg1PjaUDaLl"
      },
      "source": [
        "a=3\n",
        "b=a\n",
        "print(b)"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "icTPtDSAKjEr"
      },
      "source": [
        "If we don't declare the variable and try to print the output then we will get the following error "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "P_KmqiPBJ5_Z"
      },
      "source": [
        "print(x)"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PUE_n529K-Gp"
      },
      "source": [
        "<br><br>\n",
        "\n",
        "## **5. Multiple Assignment Operator:**\n",
        "\n",
        "Suppose you are making a program where in you enter the dimensions of the tank and it will give the volume of the tank as the output. So you can write code as:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gZHy4uODKsQX"
      },
      "source": [
        "height = 3\n",
        "length = 6\n",
        "width = 2\n",
        "volume = height * length * width\n",
        "print(volume)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PdSLF0z5N0Bq"
      },
      "source": [
        "Now python has a very useful way to assign multiple variables together in a single line using multiple assignment like this:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cGr5tmszNwUe"
      },
      "source": [
        "# this will now assign 3 to height, 6 to length and 2 to width just as before.\n",
        "height , length , width = 3 , 6 , 2\n",
        "volume = height * length * width\n",
        "print(volume)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WbLxkJozSF5g"
      },
      "source": [
        "<br><br>\n",
        "\n",
        "## **6. Variable Naming Conventions:**\n",
        "\n",
        "There are some rules we need to follow while giving a name for a Python variable.\n",
        "\n",
        "- **Rule-1**: You should start variable name with an alphabet or **underscore(_)** character.\n",
        "- **Rule-2:** A variable name can only contain **A-Z,a-z,0-9** and **underscore(_)**.\n",
        "- **Rule-3:** You cannot start the variable name with a **number**.\n",
        "- **Rule-4:** You cannot use special characters with the variable name such as such as **$,%,#,&,@.-,^** etc.\n",
        "- **Rule-5**: Variable names are **case sensitive**. For example str and Str are two different variables.\n",
        "- **Rule-6:** Do not use reserve keyword as a variable name for example keywords like **class, for, def, del, is, else,** **try, from,** etc. more examples are given below and as we go through the course we will come across many more. Creating names that are descriptive of the values often will help you avoid using any of these words."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KtIoAjAKQ0Jh"
      },
      "source": [
        "#Allowed variable names\n",
        "\n",
        "x=2\n",
        "y=\"Hello\"\n",
        "mypython=\"PythonGuides\"\n",
        "my_python=\"PythonGuides\"\n",
        "_my_python=\"PythonGuides\"\n",
        "_mypython=\"PythonGuides\"\n",
        "MYPYTHON=\"PythonGuides\"\n",
        "myPython=\"PythonGuides\"\n",
        "myPython7=\"PythonGuides\""
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HswApcdn-GTJ"
      },
      "source": [
        "#Variable name not Allowed\n",
        "\n",
        "7mypython=\"PythonGuides\"\n",
        "-mypython=\"PythonGuides\"\n",
        "myPy@thon=\"PythonGuides\"\n",
        "my Python=\"PythonGuides\"\n",
        "for=\"PythonGuides\"\n",
        "\n",
        "#It shows invalid syntax. \n",
        "#It will execute one by one and will show the error."
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zoaFd7Jw-gVJ"
      },
      "source": [
        "Also there are some naming convention that needs to be followed like:\n",
        "\n",
        "* try to keep the name of the variables descriptive short but descriptive.    **for example:** when taking inputs for the height of a tree of a box the appropriate  variable name will be just *height* not *x* not *h* not *height_of_the_tree*.\n",
        "\n",
        "* Also the pythonic way to name variables is to use all lowercase letters and underscores to separate words."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "R_5NxrWx-L2E"
      },
      "source": [
        "# pythonic way\n",
        "\n",
        "my_height = 58\n",
        "my_lat = 40\n",
        "my_long = 105"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bufefdio-5N5"
      },
      "source": [
        "# not pythonic way\n",
        "my height = 58 # wont work\n",
        "MYLONG = 40    # will work still avoid using it\n",
        "MyLat = 105    # will work still avoid using it"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0vk0r_8m_dWl"
      },
      "source": [
        "Though the last two of these would work in python, they are not pythonic ways to name variables. The way we name variables is called snake case, because we tend to connect the words with underscores."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DAoihPxbFI_d"
      },
      "source": [
        "\n",
        "\n",
        "What if we want to change or update the value of a variable for example take the example of rent = 1700, suppose the rent has hiked and the new rent is 2000 we can just assign the variable its new value as:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "81F5psRj_kUP"
      },
      "source": [
        "rent = 1700\n",
        "rent = 2000\n",
        "print(rent)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MavVAvfNGFOi"
      },
      "source": [
        "This is called overwriting the variable , i.e, When a new value is assigned to a variable, the old one is forgotten.\n",
        "\n",
        "If we had then caused some damages to the property during our crazy house party and we have to pay for them then we can just apply these changes directly to this variable."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rkEh72gQFaK2"
      },
      "source": [
        "rent = 1700\n",
        "rent = 2000\n",
        "rent =rent + 700\n",
        "print(rent)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vqwJs-3bHU7S"
      },
      "source": [
        "in the line 3 the variable *rent* is being assigned to itself plus 700 which results to 2700. \n",
        "\n",
        "Because such increment and assignment operations are very common python has a very special assignment operator for this. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gUkRhTKnH9mv"
      },
      "source": [
        "rent = 1700\n",
        "rent = 2000\n",
        "rent += 700\n",
        "print(rent)"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6N1_qkohIEb2"
      },
      "source": [
        "we can actually use this **+=** operator to tell python that we are incrementing the value on the left by the value on the right. **+=** is a example of assignment operator **-= *= /=** are some more examples of assignment operators. All of these operators just apply arithmetic operation to the variable on the left with the value on the right which makes your code more concise and easier to read and understand."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "G3q5YcesJ8MV"
      },
      "source": [
        "<br><br>\n",
        "\n",
        "## **7. Integers and Floats:**\n",
        "So far the numbers that we have dealt with were mostly whole numbers or integers, but as you may have notices that other types of numbers also do exist. For example dividing one integer by another gives us a number that isn't an integer, in python we represent such a number as a float, which is short for floating point number. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fqai63lgI8v8"
      },
      "source": [
        "print(3/2)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "25ijafCzMh4j"
      },
      "source": [
        "Numbers with a decimal point, such as 3.14, are called floating-point numbers (or floats). Note that even though the value 42 is an integer, the value 42.0 would be a floating-point number. And if 2 integers are divided then also we get float as an answer.\n",
        "\n",
        "You can check the datatype of any value by using the builtin function of type, that returns the type of an object. Here as you can see they type of a number without a decimal and the type of a number with a decimal."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "L6ZPHtSyKogM"
      },
      "source": [
        "a = 3\n",
        "b = 2.5\n",
        "\n",
        "print(type(a))\n",
        "print(type(b))"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4zrtRdZtDnj6"
      },
      "source": [
        "An operation involving an int and a float will always give float as its output. We can also covert one datatype to another by constructing new objects of those types with int and float. \n",
        "\n",
        "When we convert a float to an int the part after the decimal point is dropped and hence there is no rounding. eg 28.9 will be cut to 28. \n",
        "\n",
        "Similarly converting int to float just adds a decimal at the end of the number and a 0 after that. example 3 will become 3.0"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_17RKbnXMvSZ"
      },
      "source": [
        "a = float(3)\n",
        "b = int(28.9)\n",
        "print(a)\n",
        "print(b)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qlcwxnN0EYgx"
      },
      "source": [
        "\n",
        "\n",
        "> Another point that you need to keep in mind is float are an approximation to the number they represent. As float can represent very large range of numbers python must use approximation to represent these numbers. For example this floating point number 0.23 is in reality slightly more than 0.23. such that if we add up 0.23 to itself a few times and check its equality to the expected resultant it will be different. Although the difference is very small but it exists never the less and you should know about it.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ecx9e1p8DuVJ"
      },
      "source": [
        "print(0.23 + 0.23 + 0.23 + 0.23 + 0.23 + 0.23\n",
        "       + 0.23 + 0.23 + 0.23 + 0.23 + 0.23 + 0.23\n",
        "       + 0.23 + 0.23 + 0.23 + 0.23 + 0.23 + 0.23\n",
        "       + 0.23 + 0.23 + 0.23 + 0.23 + 0.23 + 0.23\n",
        "       + 0.23 + 0.23 + 0.23 + 0.23+ 0.23 + 0.23 == 6.9)"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cs768gAfFM2S"
      },
      "source": [
        "<br><br>\n",
        "\n",
        "##**9. Boolean Datatype, Comparison and Logical Operators:**\n",
        "\n",
        "Bool is another datatype that is commonly used in Python. Bool is short for Boolean which can have a value of either True or False. Boolean algebra is the branch of algebra in which the values of the variables are the truth values true or false. Boolean algebra us the framework on which all electronic devices and built and exists fundamentally in every line of code inside a computer. In python we can easily assign boolean values like this:\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JW5nXrxsEnin"
      },
      "source": [
        "python_awsome = True\n",
        "doumentation_bad = False"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "a-JN4xZlHmzD"
      },
      "source": [
        "We can use comparison operators to compare 2 values and produce boolean results like:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mVRNbJecHjgH"
      },
      "source": [
        "a = 3 > 1\n",
        "print(a)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QK7KL0o3Jqo3"
      },
      "source": [
        "Here 3 is greater than 1 so printing out the output gives us a boolean value to true. There are many comparison operators in python, as you can see here are all of them.\n",
        "\n",
        "As you will see the function of all these comparison operators are evident from their names itself these are **less than,  greater than , less than or equal to, greater than or equal to, not equal to**.\n",
        "\n",
        "Working with boolean has its own set of operators called as logical operators. These operators very useful when working with boolean, and evaluates if both the sides are true, **OR** evaluates if atleast one side is true and **not** evaluates the inverse of the input boolean.\n",
        "\n",
        "Lets understand if via an example:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eN24eeGyHl6k"
      },
      "source": [
        "rent = 1200\n",
        "is_affordable = rent > 1000 and rent < 2000\n",
        "\n",
        "print(is_affordable)"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XgntpdwgLpzT"
      },
      "source": [
        "Here we check if the *rent* of a house is affordable or not, here in the second line we evaluate both the sides ie *rent > 1000*, yes, so it is **true** while the second condition is *rent < 200*, that too is **true**. as both the condition on the left and right side of and is **true** hence the boolean value of **true** will be assigned to the *is_affordable variable*. In other words if the *rent* is greater than 1000 and less than 2000 then only it is affordable.\n",
        "\n",
        "And here you can see how not works:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8c9_zsNvKR0v"
      },
      "source": [
        "rent = 1200\n",
        "is_affordable = not(rent > 1000 and rent < 2000) #\"not\" just inverts bool value\n",
        "\n",
        "print(is_affordable)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oeq2QDdEMSK8"
      },
      "source": [
        "<br><br>\n",
        "\n",
        "## **10. Strings:**\n",
        "\n",
        "Python has another datatype in its toolkit called as Strings, as the name suggest this datatype deals with characters words and text. String is a immutable order of sequences of characters (eg, Letters, numbers, spaces and symbols. We will be explaining what does immutable order means later on.\n",
        "\n",
        "You can create a string by using quotes as seen here, you can use either single / double quotes they both work equally well but there are some cases where you might prefer one over the other which we will be discussing below."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Q84mRQ2_MFGW"
      },
      "source": [
        "# using Double Quotes\n",
        "print(\"ShapeAI\")\n",
        "# using Single Quotes\n",
        "print('ShapeAI')"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "odFoazduN4rR"
      },
      "source": [
        "In this example we printed the word *ShapeAI* using single and double quotes and got the same output *ShapeAI*.\n",
        "\n",
        "We can also assign a string to a variable just like float and int."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Krfhjf9NN0-D"
      },
      "source": [
        "motto = \"Learn | Code | Compete | Intern\" \n",
        "print(motto)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YHgDcRm6R0FI"
      },
      "source": [
        "Strings in Python are shown as the variable type str."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YkyDHgq3RW6K"
      },
      "source": [
        "type(motto)"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SjqlkfgzR-gR"
      },
      "source": [
        "> *String can contain any character number symbol space within the quotes.\n",
        "However if we want to have quotes inside the string we get an error.*"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "788JWDKUR4BD"
      },
      "source": [
        "dialogue = \"shiva said, \"you learn as you grow\"\""
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WjG9dsH5SOFT"
      },
      "source": [
        "Python provides 2 easy ways to handle such problem:\n",
        "\n",
        "1. Place the string in single quotes rather than double quotes. This will solve your problem for having double quotes within the string. But sometimes you will want to have both double and single quotes in your string in that case this will prove to be a problem."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_lPyEIYmSIes"
      },
      "source": [
        "dialogue = 'shiva said, \"you learn as you grow\"'\n",
        "print(dialogue)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EMqd6v3xSMno"
      },
      "source": [
        "2. In that case we can use a backslash to skip quotes as you can see in this example. The backslash helps python to know that the the single quote should be interpreted as part of the string rather than the quote that ends the string."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "otSfYmAoS2TM"
      },
      "source": [
        "dialogue = '\"shiva you\\'re bag is red\"'\n",
        "print(dialogue)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RA3hh1VhTFUF"
      },
      "source": [
        "There are a few operators that we use on floats and ints that can also be used on strings. For example we can use the **'+'** to combine / concatenate 2 strings together and we can use **'*'** to repeat the string let us look at an example for each."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bIBYEJ6uS7ko"
      },
      "source": [
        "print(\"hello\" + \"world\")\n",
        "\n",
        "print(\"hello\" + \" \" + \"world\")"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iurj3HxXTkx2"
      },
      "source": [
        "> *here in this example we can see that using the plus arithmetic operator we get *helloworld* written together but this word that is printed out has no meaning, we need to have a space between both the words to have a meaning. We can add another string containing just a space in between the words to do so.*"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jYVDqes0TeCz"
      },
      "source": [
        "word = \"hello\"\n",
        "print(word * 5)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "78vTvfYSTwap"
      },
      "source": [
        "Now in the second example we can see that using the multiplication operator on a string we get repetition of the same word as many time as the number we multiplied the string by in the output."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fIFnUmZcT3_I"
      },
      "source": [
        "However unlike multiplication and addition operators the other arithmetic operators like division and subtraction cannot be used on strings any attempt to do so would result in an error that string is an unsupported datatype for the division/subtraction operator."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "h2nM7OBxT3he"
      },
      "source": [
        "word_1 = \"hello\"\n",
        "word_2 = \"world\"\n",
        "print(word_1 / word_2)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9gumg_-mUBfA"
      },
      "source": [
        "A useful builtin function for string datatypes is *len()* which stands for length. As the name suggests (it returns the length of an object ie., it returns the no of characters in a string.\n",
        "\n",
        "It takes in values in a parenthesis and returns the length of the string. *len()* is a little different from *print()* as the value returned from length can be stored in a variable as seen in the example here. The *len()* function outputs a value 7 that is then stored in a variable called as *word_length* which is then printed out."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oQNIXXfNTtzl"
      },
      "source": [
        "word_length = len(\"ShapeAI\")\n",
        "print(word_length)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EEfczWGFzu6Y"
      },
      "source": [
        "### **Question:**\n",
        "\n",
        "The line of code in the following code block will cause a *SyntaxError*, thanks to the misuse of quotation marks. First run it with Test Run to view the error message. Then resolve the problem so that the quote (from Mahatama Gandhi) is correctly assigned to the variable *gandhi_quote*."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MnmykPZy0F-w"
      },
      "source": [
        "# TODO: Fix this string!\n",
        "gandhi_quote = 'If you don't ask, you don't get it'"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GDbOH8th0g7c"
      },
      "source": [
        "### **Question:**\n",
        "\n",
        "In this question you have to print the accuracy logs of a model in training."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tlAI_jTK0ywg"
      },
      "source": [
        "model = \"VGG16\"\n",
        "iteration = \"150\"\n",
        "accuracy = \"67.98\"\n",
        "\n",
        "# TODO: print a log message using the variables above\n",
        "# This message should have the same format as this one:\n",
        "# \"the accuracy of ResNET50 model in 100th iteration is: 42.16%\""
      ],
      "execution_count":  None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WiPTD1y81uXZ"
      },
      "source": [
        "### **Question:**\n",
        "\n",
        "Use string concatination and *len()* function to fing the length of a persons complete name and store it in the variable *name_length*.\n",
        "\n",
        "As a business card designer find if the name can fit into a business card. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9Hzh7_vB1tpb"
      },
      "source": [
        "given_name = \"Rahul\"\n",
        "middle_names = \"Shastri\"\n",
        "family_name = \"Mishra\"\n",
        "\n",
        "name_length = #todo: calculate how long this name is\n",
        "\n",
        "# Now we check to make sure that the name fits within the driving license character limit\n",
        "# Nothing you need to do here\n",
        "driving_license_character_limit = 28\n",
        "print(name_length <= driving_license_character_limit)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Juq_M-ENy6-_"
      },
      "source": [
        "<br><br>\n",
        "\n",
        "## **11. Type and Type Conversion Revision:**\n",
        "\n",
        "Till now we have covered 4 different datatypes int, float, bool and string. As you can recall from the previous classes python has a builtin function called as type that returns the type of an object."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wsr3y0KgyuWW"
      },
      "source": [
        "print(type(75))\n",
        "print(type(75.0))\n",
        "print(type(\"75\"))\n",
        "print(type(True))"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iGgkIXg5zgwN"
      },
      "source": [
        "Look at the code example we can see that even though the first 3 values appear to be same they can be encoded into different datatypes each with their own set of functions operations and uses.\n",
        "\n",
        "This is to note that here we have called the function print on another function type to output the return value of the function type. In such a case always the function inside the parenthesis is  run first ie. here it will be type.\n",
        "\n",
        "Different types have different properties with their own set of functions operations and uses and hence while choosing a variable you need to choose the correct set of datatype for it depending upon how you care going to use it this is very important.\n",
        "\n",
        "There might be sometimes when you don't have the control over the type of the data being provided to you like one that has been received from a user as in input. But the good news is that python allows you to create new objects from old and change the datatypes for these new objects. As we had previously seen in the integers and floats video."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bBZGIBLe6kKT"
      },
      "source": [
        "> For example here we created a float ie 3.0 from an int 3 and assigned it to a new variable called decimal"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yUceqN1QzIJ0"
      },
      "source": [
        "decimal = float(3)\n",
        "print(decimal)\n",
        "print(type(decimal))"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OHQFOeZi6o6c"
      },
      "source": [
        "> In this next example we created a string from the integer variable *marks* and used that to create a larger string."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xZwhCiLZ6jky"
      },
      "source": [
        "marks = 15\n",
        "subject = \"coding\"\n",
        "semester = \"first\"\n",
        "\n",
        "result = \"I scored \" + str(marks) + \" in \" + subject + \" during my \" + semester + \" semester.\"\n",
        "print(result)"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IqgSdyf067yQ"
      },
      "source": [
        "> we can also create an float from string"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Kqsda09k6d4x"
      },
      "source": [
        "marks = \"15\"\n",
        "print(type(marks))\n",
        "\n",
        "marks = float(marks)\n",
        "print(type(marks))"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pzFSq-6W7oZi"
      },
      "source": [
        "### **Question:**\n",
        "\n",
        "In this quiz, you’ll need to change the types of the input and output data in order to get the result you want.\n",
        "\n",
        "Calculate and print the total sales for the week from the data provided. Print out a string of the form \"This week's total sales: xxx\", where xxx will be the actual total of all the numbers. You’ll need to change the type of the input data in order to calculate that total."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hu24eSfU7Q3F"
      },
      "source": [
        "mon_sales = \"121\"\n",
        "tues_sales = \"105\"\n",
        "wed_sales = \"110\"\n",
        "thurs_sales = \"98\"\n",
        "fri_sales = \"95\"\n",
        "\n",
        "#TODO: Print a string with this format: This week's total sales: xxx\n",
        "# You will probably need to write some lines of code before the print statement.\n",
        "total_sales = (float(mon_sales) + float(tues_sales) + float(wed_sales) \n",
        "                + float(thurs_sales) + float(fri_sales))\n",
        "print(\"This week\\'s total sales: \" + str(total_sales))"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4M_Qt7mSWGuD"
      },
      "source": [
        "### **12.a. One important string method: format()**\n",
        "\n",
        "We will be using the *format()* string method a good bit in our future work in Python, and you will find it very valuable in your coding, especially with your print statements.\n",
        "\n",
        "We can best illustrate how to use *format()* by looking at some examples:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "utXx78crUTO0"
      },
      "source": [
        "# Example 1\n",
        "print(\"EG:1\")\n",
        "print(\"Mohammed has {} balloons\".format(27))\n",
        "\n",
        "# Example 2\n",
        "print(\"EG:2\")\n",
        "animal = \"dog\"\n",
        "action = \"bite\"\n",
        "print(\"Does your {} {}?\".format(animal, action))\n",
        "\n",
        "# Example 3\n",
        "print(\"EG:3\")\n",
        "maria_string = \"Maria loves {} and {}\"\n",
        "print(maria_string.format(\"math\",\"statistics\"))"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "G9ybjouxWyQe"
      },
      "source": [
        "Notice how in each example, the number of pairs of curly braces {} you use inside the string is the same as the number of replacements you want to make using the values inside *format()*.\n",
        "\n",
        "More advanced students can learn more about the formal syntax for using the *format()* string method [here](https://docs.python.org/3.6/library/string.html#format-string-syntax)."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PqKTCtYOTMQ8"
      },
      "source": [
        "<br><br>\n",
        "\n",
        "## **13. Lists and Membership Operators:**\n",
        "\n",
        "**Data structures** are containers that organize and group data types together in different ways. A **list** is one of the most common and basic data structures in Python. It is a mutable ordered sequence of elements.\n",
        "\n",
        "The code below defines a variable *students* which contains a list of strings. Each element in the list is a string that signifies the name of a student.\n",
        "\n",
        "> The data inside a list can be a mixture of any number and combination of diffrent data types."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zRS5zyHbWqaP"
      },
      "source": [
        "students = ['sam', 'pam', 'rocky', 'austin', 'steve', 'banner']"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fl7PSRXXdhrO"
      },
      "source": [
        "List are ordered, we can look up individual elements by their index, we can look elements from a list just like we have done below."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uERsCZXNeBbY"
      },
      "source": [
        "print(students[0])\n",
        "print(students[1])\n",
        "print(students[2])"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cGgwxP3_eWir"
      },
      "source": [
        "Notice that the first element in the list is accessed by the index 0, many programming language follow this convection called as zero based indexing.\n",
        "\n",
        "We can also access the elements from the end of the list using negative index as seen in the examples below."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CiGVaf_beRAC"
      },
      "source": [
        "print(students[-1])\n",
        "print(students[-2])\n",
        "print(students[-3])"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KqJU4qOYgE6A"
      },
      "source": [
        "If you try to access an index in a list that doesn't exist then you will get an Error as seen below."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C5DSaY0Wf2wT"
      },
      "source": [
        "print(students[20])"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nKJIgDrZh0Cn"
      },
      "source": [
        "### **Question:**\n",
        "\n",
        "Try to use *len()* to pull the last element from the above list"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NOiBUWAwgV87"
      },
      "source": [
        "# TODO: write your code here\n",
        "students[len(students)-1]"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WZU02jRcFFPN"
      },
      "source": [
        "## **13.a. Membership Operators:[Lists]**\n",
        "\n",
        "In addition to accessing individual elements froma a list, we can use pythons sliceing notation to access a subsequence of a list.\n",
        "\n",
        "Slicing means using indicies to slice off parts of an object like list/string. Look at an example "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dLyKcmXNiLwU"
      },
      "source": [
        "students = ['sam', 'pam', 'rocky', 'austin', 'steve', 'banner', 'tony', 'bruce', \n",
        "            'henry', 'clark', 'diana']\n",
        "student = \"Barry\"\n",
        "\n",
        "# slice a particular range\n",
        "marvel = students[4:7]\n",
        "flash = student[1:3]\n",
        "\n",
        "print(marvel)\n",
        "print(flash)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hzDrsBVELAsr"
      },
      "source": [
        "# slice from the end\n",
        "dc = students[7:]\n",
        "flash = student[1:]\n",
        "\n",
        "print(dc)\n",
        "print(flash)"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NYSNXq7wLtR9"
      },
      "source": [
        "# slice from the begining\n",
        "normal = students[:4]\n",
        "flash = student[:3]\n",
        "\n",
        "print(normal)\n",
        "print(flash)"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uXeNb-9qNdkL"
      },
      "source": [
        "# length of the list and the string\n",
        "print(len(students))\n",
        "print(len(student))"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FPqHnXKXMLku"
      },
      "source": [
        "Of the types we have seen lists are most familier to strings, both supports the *len()* function, indexing and slicing.\n",
        "\n",
        "> Here above you have seen that the length of a string is the no of characters in the string, while the length of a list is the no of elements in the list.\n",
        "\n",
        "Another thing that they both supports aare membership operators:\n",
        "\n",
        "* **in:** evaluates if an object on the left side is included in the object on the right side.\n",
        "* **not in:** evaluates if object on left side is not included in object on right side."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3WSj6PZYL3Eg"
      },
      "source": [
        "greeting = \"Hello there\"\n",
        "print('her' in greeting, 'her' not in greeting)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sQIsQ-_PRZQm"
      },
      "source": [
        "print('ShapeAI' in students, 'ShapeAI' not in students)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ykKZQtwXfWRd"
      },
      "source": [
        "### **13.b. Mutability and Order:**\n",
        "\n",
        "So how are Lists diffrent from Strings, both supporst slicing, indexing, in and not in operators.\n",
        "\n",
        "The most obvious diffrence between them is that string is a sequence of characters while list's elements can be any type of bojects string, integers, floats orr bools.\n",
        "\n",
        "A more important diference is that lists can be modified but string can't. Look at the example below to understand more."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uEYr9AS0Rlxe"
      },
      "source": [
        "students = ['sam', 'pam', 'rocky', 'austin', 'steve', 'banner', 'tony', 'bruce', \n",
        "            'henry', 'clark', 'diana']\n",
        "\n",
        "students[2] = 'ben'\n",
        "print(students)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FHuFUelijkOp"
      },
      "source": [
        "student = \"Barry\"\n",
        "student[1] = \"e\"\n",
        "print(student)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xMiN9z9pkAWm"
      },
      "source": [
        "**Mutability** is about whether or not we can change an object once it has been created. If an object (like a list or string) can be changed (like a list can), then it is called **mutable**. However, if an object cannot be changed without creating a completely new object (like strings), then the object is considered immutable."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xm5EHFuykdpP"
      },
      "source": [
        "**Order** is about whether the position of an element in the object can be used to access the element. **Both strings and lists are ordered.** We can use the order to access parts of a list and string.\n",
        "\n",
        "> However, you will see some data types in the next sections that will be unordered. For each of the upcoming data structures you see, it is useful to understand how you index, are they mutable, and are they ordered. Knowing this about the data structure is really useful!\n",
        "\n",
        "Additionally, you will see how these each have different methods, so why you would use one data structure vs. another is largely dependent on these properties, and what you can easily do with it!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nQ22-QIIRXsG"
      },
      "source": [
        "Previously when we created a variable that heald an immutable object like string, the value of the immutable object was saved in memory. Like as you can see below"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-JjIXgKuPjlO"
      },
      "source": [
        "student = \"pam\"\n",
        "character = student\n",
        "print(character)\n",
        "character = \"peter\"\n",
        "print(character)\n",
        "print(student)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "T4SpeeBCZAVB"
      },
      "source": [
        "Lists are diffrent from strings as they are mutable as can be seen from the example below"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fDu_EQW3j5yw"
      },
      "source": [
        "students = ['sam', 'pam', 'rocky', 'austin', 'steve', 'banner', 'tony', 'bruce', \n",
        "            'henry', 'clark', 'diana']\n",
        "characters = students\n",
        "print(characters)\n",
        "characters[1]= \"peter\"\n",
        "print(characters)\n",
        "print(students)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VC6ZnlQfZjsF"
      },
      "source": [
        "There are some useful functions for lists that you should get familier with.\n",
        "\n",
        "1. ***len():*** returns how many elements does the list has.\n",
        "2. ***max():*** returns the greatest element of a list.\n",
        "3. ***min():*** returns the smallest element of a list.\n",
        "4. ***sorted():*** returns a copy of the list, in order from smallest to the largest. leaving the orignal list unchanged\n",
        "\n",
        "> max element in a list of integers is the largest integer, while in the case of string is the string that will come last if the list was sorted alphabetically."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bk55uR0VPzqr"
      },
      "source": [
        "students = ['sam', 'pam', 'rocky', 'austin', 'steve', 'banner', 'tony', 'bruce', \n",
        "            'henry', 'clark', 'diana']\n",
        "\n",
        "student = \"barry\"\n",
        "\n",
        "print(max(students))\n",
        "print(max(student))"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hL-h6v8Nev9j"
      },
      "source": [
        "> a point to note is that even though you can have a list cntaining int and string a max function will be undefined upon such a list."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qofTAIxvccsm"
      },
      "source": [
        "max([2, 'two'])"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DmQ7YXTse_Le"
      },
      "source": [
        "characters = sorted(students)\n",
        "print(characters)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SZiwJj5ua7qs"
      },
      "source": [
        "***Join()*** is an other useful function for lists(string lists), Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string. Look at the example below to understand.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tUxIAmUiZgOv"
      },
      "source": [
        "sep_str = \"\\n\".join([\"Jack\", \"O\", \"Lantern\"])\n",
        "print(sep_str)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mKrXZopBesma"
      },
      "source": [
        "In this example we use the string **\"\\n\"** as the separator so that there is a newline between each element.\n",
        "We can also use other strings as separators with .join. Here we use a hyphen."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GPH5EfbYepKQ"
      },
      "source": [
        "name = \"-\".join([\"Jack\", \"O\", \"Lantern\"])\n",
        "print(name)"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "z4Qml70wfYt5"
      },
      "source": [
        "> It is important to remember to separate each of the items in the list you are joining with a comma (,). Forgetting to do so will not trigger an error, but will also give you unexpected results."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NaEnB22pfci9"
      },
      "source": [
        "***append()*** is an other useful method that adds an element to the end of a list."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XcY1vqKLe1FK"
      },
      "source": [
        "letters = ['a', 'b', 'c', 'd']\n",
        "letters.append('e')\n",
        "print(letters)"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HFY2Ty8_hUdo"
      },
      "source": [
        "<br><br>\n",
        "\n",
        "## **14. Tuples:**\n",
        "\n",
        "A tuple is another useful container. It's a data type for immutable ordered sequences of elements. They are often used to store related pieces of information. Consider this example involving (x, y, z) coordinates:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_Q0uioLufvgc"
      },
      "source": [
        "vector = (4, 5, 9)\n",
        "print(\"x-coordinate:\", vector[0])\n",
        "print(\"y-coordinate:\", vector[1])\n",
        "print(\"z-coordinate:\", vector[2])"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_JtjMmZ2rz1t"
      },
      "source": [
        "Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indices. Unlike lists, however, tuples are immutable - you can't add and remove items from tuples, or sort them in place.\n",
        "\n",
        "> Tuples can also be used to assign multiple variables in a compact way.\n",
        "\n",
        "> The parentheses are optional when defining tuples, and programmers frequently omit them if parentheses don't clarify the code."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-a_ISfUIrx65"
      },
      "source": [
        "location = 108.7774, 92.5556\n",
        "latitude, longtitude = location\n",
        "print(\"The coordinates are {} x {}\".format(latitude, longtitude))"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "W5LSu94ItjfD"
      },
      "source": [
        "In the second line, two variables are assigned from the content of the tuple location. This is called tuple unpacking. You can use tuple unpacking to assign the information from a tuple into multiple variables without having to access them one by one and make multiple assignment statements.\n",
        "\n",
        "If we won't need to use location directly, we could shorten those two lines of code into a single line that assigns three variables in one go!"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0d7u9CZ1tgo-"
      },
      "source": [
        "location = 108.7774, 92.5556\n",
        "\n",
        "print(\"The coordinates are {} x {}\".format(latitude, longtitude))"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DORS4RJ_0W0Z"
      },
      "source": [
        "<br><br>\n",
        "\n",
        "## **16. Dictionaries and Identity Operators:**\n",
        "\n",
        "A dictionary is a mutable data type that stores mappings of unique keys to values. Here's a dictionary that stores elements and their atomic numbers."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ApfpAVUvzqDe"
      },
      "source": [
        "elements = {\"hydrogen\": 1, \"helium\": 2, \"carbon\": 6}"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xTlhGP84yajj"
      },
      "source": [
        "Dictionaries can have keys of any immutable type, like integers or tuples, not just strings. It's not even necessary for every key to have the same type! We can look up values or insert new values in the dictionary using square brackets that enclose the key."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pAtBqAtPyZzq"
      },
      "source": [
        "print(elements[\"helium\"])  # print the value mapped to \"helium\"\n",
        "elements[\"lithium\"] = 3  # insert \"lithium\" with a value of 3 into the dictionary\n"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8ygwwby4y6Ia"
      },
      "source": [
        "We can check whether a value is in a dictionary the same way we check whether a value is in a list or set with the in keyword. Dicts have a related method that's also useful, *get()*. *get()* looks up values in a dictionary, but unlike square brackets, get returns **None** (or a default value of your choice) if the key isn't found."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CyBTsiY6yrRA"
      },
      "source": [
        "print(\"carbon\" in elements)\n",
        "print(elements.get(\"dilithium\"))"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "d84ZmGfRzy7r"
      },
      "source": [
        "Carbon is in the dictionary, so ***True*** is printed. Dilithium isn’t in our dictionary so ***None*** is returned by get and then printed. If you expect lookups to sometimes fail, get might be a better tool than normal square bracket lookups because errors can crash your program."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vYKbWMN40Hbj"
      },
      "source": [
        "### **16.a. Keyword Operators:**\n",
        "\n",
        "* ***is:***\tevaluates if both sides have the same identity\n",
        "* ***is not***\tevaluates if both sides have different identities\n",
        "\n",
        "You can check if a key returned ***None*** with the ***is*** operator. You can check for the opposite using ***is not.***"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-3Z4D-Przuu2"
      },
      "source": [
        "n = elements.get(\"dilithium\")\n",
        "print(n is None)\n",
        "print(n is not None)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WY58GiSVSQAU"
      },
      "source": [
        "### Task:\n",
        "Define a dictionary named population that contains this data:\n",
        "\n",
        "**Keys** ->\t    **Values**\n",
        "\n",
        "New York ->\t\t17.8\n",
        "\n",
        "Spain\t  ->\t   13.3\n",
        "\n",
        "Dhaka\t  ->\t   13.0\n",
        "\n",
        "Mumbai\t  ->\t 12.5"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PEGkVp3S0pzm"
      },
      "source": [
        "population = {\"New York\":17.8, \"Spain\":13.3, \"Dhaka\":13.0, \"Mumbai\":12.5}\n",
        "print(population)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "esVtoMWGTESQ"
      },
      "source": [
        "## 16.b. ***Get()* with a Default Value:**\n",
        "\n",
        "Dictionaries have a related method that's also useful, *get()*. *get()* looks up values in a dictionary, but unlike looking up values with square brackets, *get()* returns **None** (or a default value of your choice) if the key isn't found. If you expect lookups to sometimes fail, *get()* might be a better tool than normal square bracket lookups."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lpgpXnvLS_BO"
      },
      "source": [
        "print(population.get('London'))"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lwUfwma8TvA9"
      },
      "source": [
        "population['London']"
      ],
      "execution_count":None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "l50bnIi5T1Wl"
      },
      "source": [
        "population.get('London', 'There\\'s no such place!')"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6mBdBxyQULNO"
      },
      "source": [
        "> *In the last example we specified a default value (the string 'There's no such element!') to be returned instead of None when the key is not found.*\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Yl7JfrMAn3kJ"
      },
      "source": [
        "## **16.c. Compound Data Structures:**\n",
        "\n",
        "Previously we have seen a dictonary called *elements* in which the element names are maped to their atomic numbers which are integers. But what if we want to store more information about each element like their atomic weight and symbol. We can do that by adjusting this dictionary so that it maps the element names to an other dictionary, that stores that collection of data. \n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UUfWjEUIUIKS"
      },
      "source": [
        "elements = {\"hydrogen\": {\"number\": 1,\n",
        "                         \"weight\": 1.00794,\n",
        "                         \"symbol\": \"H\"},\n",
        "              \"helium\": {\"number\": 2,\n",
        "                         \"weight\": 4.002602,\n",
        "                         \"symbol\": \"He\"}}"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pHEaNsQMplHp"
      },
      "source": [
        "\n",
        "We can look up information about an element using this nested dictionary, using square brackets or the *get()* method."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N3Icsgotpv_P"
      },
      "source": [
        "helium = elements[\"helium\"]  # get the helium dictionary\n",
        "hydrogen_weight = elements[\"hydrogen\"][\"weight\"]  # get hydrogen's weight\n",
        "\n",
        "print(helium)\n",
        "print(hydrogen_weight)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "L8id3asCp8Q5"
      },
      "source": [
        "> You can also add a new key to the element dictionary."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "krGwpkyqpyM7"
      },
      "source": [
        "oxygen = {\"number\":8,\"weight\":15.999,\"symbol\":\"O\"}  # create a new oxygen dictionary \n",
        "elements[\"oxygen\"] = oxygen  # assign 'oxygen' as a key to the elements dictionary\n",
        "\n",
        "print('elements = ', elements)"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GBpaX13TrJ0s"
      },
      "source": [
        "### **Question:**\n",
        "\n",
        "Try your hand at working with nested dictionaries. Add another entry, *'is_noble_gas,'* to each dictionary in the *elements* dictionary. After inserting the new entries you should be able to perform these lookups:\n",
        "\n",
        "\n",
        "\n",
        "---\n",
        "\n",
        "> print(elements['hydrogen']['is_noble_gas'])<br>\n",
        "False\n",
        "\n",
        "> print(elements['helium']['is_noble_gas'])<br>\n",
        "True"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V8Ynb9OpqGCY"
      },
      "source": [
        "elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},\n",
        "            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}\n",
        "\n",
        "# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries\n",
        "# hint: helium is a noble gas, hydrogen isn't\n",
        "elements['helium']['is_noble_gas'] = True\n",
        "elements['hydrogen']['is_noble_gas'] = False"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZJmnZKwJr3Nw"
      },
      "source": [
        "elements"
      ],
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "42016zIdsXQL"
      },
      "source": [
        ""
      ],
      "execution_count":None,
      "outputs": []
    }
  ]
}