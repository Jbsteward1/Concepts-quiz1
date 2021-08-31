
PART I
Navigating the File System
1.  How do you move back and forth between directories? To move back and forth through a directory you (pwd) print working drectory to list what already on computer then (cd) change directory based on what you have stored.

2.  How do you create and delete files? to create a file you can (touch then add file name.(something)), to delete a file you (rm then add the file name.)

3.  How do you create and delete directories? to create a directory you first (cd ..) to the desktop then type (mkdir) add new directory(folder) name,  to delete a directory you would (rmdir) along with the directory name.

4.  How can I see exactly where I am within the filesystem? To find where you are you could (pwd) print working directory. 

5.  How can I see the files and directories within the current directory that I am in? The (ls) to list the current directories.



Git
1.  How do you let git know you want to track changes made in a directory? You would a initiliaze a git repo by typing (git init).

2.  How do you tell git that you like the work you’ve done and want it to be a part of a chunk of work to be saved? To let git know i like my work i would use the (get add) option along with the file name.

3.  How do you tell git you want to save a chunk of work? To actually save that piece of work i would then use a (git commit -m) alone with a descriptive message put into qotations. 

4.  How do you tell git where to push your local changes up to a online repository? You would use the (git push) code and it will then give you a direction of where to send the push upstream.

5.  How can you safely work on a different version of your current project? To work on a different version of the current project you make a new branch using (git branch) and add a name behind it.

6.  How can you make that different version become a part of your main version? To make a different version a part of the main branch you would merge the branch using (git merge) and since you mightve been on the new branch you would add it to main.

7.  How do I move between versions of my project? To move between versions you would use (git checkout) along wit the name you want to switch to.

8.  How can I go back to previous chunks of work that I’ve created and work from that point in time? To go back you could go itnot the git repo and edit or from the terminal you could (git revert) to the point you would wanna edit, it keeps the histoty but removes the contents.

9.  Let’s say I wrote a bad message for a commit. How could I change it? To change a bad message for a commit i would use (git commit -- amend) then the new message.

PART II
Python
1.  How do I run my code from the terminal?to run the code from the terminal you type python the the file name .python

2.  What can I use to reference a value later in my code? To reference a value you would make something a variable meaning ( my_name = Jeremy)

3.  How can I make my program display text or some value in my terminal? To display what youve now put into the text editor you woud type (print(whatever variable or txt or data type you are lookig to print))

4.  How can I make my code make decisions on which code to execute? If else statements would work in this specific scenario,(If child number 1? print(i love him/her)) elif child 2 print(i dont love him/her).

5.  How can I repeat blocks of code based on conditions? repeating conditions come by using loops like a while loop for example.

6.  Why is it critical to ensure that our conditions eventually become false when repeating blocks of code? If the conditions dont become fale the program will run infinitely.

7.  What are sequences and what are the differences between them? a sequence is a set or like a list or a tuple for example, they are seperated by commas and how the values can be changed or not changed depending on how the way the list is setup. 

8.  How do I access a value within the various types of sequences? to acces a certain value you would have to call the specific zero based number in the list ie: For_later_use[2] that will acces value to from the list index.
9.  What is an index when talking about sequences? An index is basically the position of the items listed. ie: (food[0], car[1], house[3]).

10. What is the index of the first value within a sequence? The index of the first value is always 0 unless counting backwards then it would be -1

11. How can I add or remove a value from a sequence? To add or remove a value hae to assing the zero based number then add pop.ie pizza_toppings.pop()

12. What is the index of the last value within a sequence? The index of the last value would be -1 again if counting backwards.

13. How can I get the length of a sequence? To get the length of a sequence you would use a while len loop.ie: while index < len(self.items):

14. What can I use to reference and use a block of code later in my code? By adding a comment? using  pound sign #

15. What is DRY? D.R.Y = dont repeat yourself meanig tehre are differnt ways to repeat the same code without using the exact code.

16. What is Scope? Provide an example. Scope is fdefining a variable to a function ie: def __function_name ()

17. What is the difference between parameters and arguments? A parameter are the names listed in the functions definition, and the argument are the actual value passed to the function.

18. What is recursion? A recursion is the process of the function calling itself directly: def __find_your_way_home("if home cleanup")

19. How can you return a value from a function? ie def add(x, y):
   print(x+y)
    add(6,9)


20. Describe a dictionary. How and why would it be useful? A dictionary is a data type and its useful because it is used for indexinfg meaning store an order of key values:ie practice ={"first_name": "jeremy", "favorite_food",: "salmon"}

21. How can you remove a value from a dictionary? To remove a value you use the del command ie:del test_dict['Mani'] 

22. How can you access and change values within a dictionary? To acces & change a value is basically the same call the number you want to use and then add a bracket behind it wit the zero based number ie: practice[1]="walk the dog"

23. What data types can a sequence hold? A sequence can hold strings, lists, tuples

24. What data types can a dictionary hold? A dictionary can hold integers floats strings booleans and lists.

25. How can you iterate through a dictionary? You can iterate through a dictionary by using a key and value and changing them.ie: print(key, value)

26. What is object oriented programming? It is a way to create classes
27. Describe a class? Why are they useful? A class is a representation of common elements you can build on. Its useful because it makes the code formula easier.

28. What are class properties? How would I give a class an initial set of properties? A class proprety is either an instance or the attribute meaning its name place.

29. What are class methods?A method is a function that belongs to an object. ie: def __school__ (self, gym, art,) self.gym

30. What is inheritence? An inheritance  us to define a class that inherits all the methods and properties from another class

31.  What are the various data types? (edited) The various data types are, Numbers, Lists, Strings, Tuple, and a Dictionary.