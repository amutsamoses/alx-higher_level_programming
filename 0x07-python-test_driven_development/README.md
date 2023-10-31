0x07. Python - Test-driven development

The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.


Purpose:	Write automated tests as part of the documentation for a module.
doctest tests source code by running examples embedded in the documentation and verifying that they produce the expected results. It works by parsing the help text to find examples, running them, then comparing the output text against the expected value. Many developers find doctest easier to use than unittest because, in its simplest form, there is no API to learn before using it. However, as the examples become more complex the lack of fixture management can make writing doctest tests more cumbersome than using unittest.

What is Doctest?
Doctest is an inbuilt test framework that comes bundled with Python by default. The doctest module searches for code fragments that resemble interactive Python sessions and runs those sessions to confirm they operate as shown.

Developers commonly use doctest to test documentation. The doctest module looks for sequences of prompts in a docstring, re-executes the extracted command, and compares the output with the command’s input given in the docstrings test example.

The default action when running doctests is not to show the output when a test passes. However, we can change this in the doctest runner options. In addition, doctest’s integration with the Python unittest module enables us to run doctests as standard unittest test cases.

What is Unittest?
Unittest test case runners allow more options when running tests, like reporting test statistics such as tests that passed and failed.

Unittest uses methods created in classes to manage tests. It has support for automation, setup, and shutdown code when testing. Unittest has several rich, in-built features that are unavailable in doctest, including generators and group fixture managers like setUp and tearDown. 

Since unittest follows the object-oriented method, it’s more suitable for testing class-based methods in a non-production environment. Continuous delivery tools such as Jenkins or Travis CI work better for production environments.
We’ll create a real-world example in the following sections, some code with customer information and discounts, and test it using doctest and unittest. Then we’ll analyze the tests and recommend the best ways to make further improvements.  

Using Unittest 
Let’s implement a Customer class and explore how we can test its methods using unittest.  

At the terminal command prompt, create a tests directory, then create a subdirectory named unittest. We’ll later create our Python testing scripts in the unittest directory. 

Use these commands to create the directory and subdirectory:

mkdir tests
cd tests 
mkdir unittest && cd unittest
Inside the unittest directory, create a Python script named unittest/customer.py. 
