In this task the problem statement is “Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption” 

What is Caesar Cipher?
Imagine you're a kid passing secret notes in class. You don't want anyone else to read them, so you create a simple code:
•	Replace A with D

•	Replace B with E\

•	Replace C with F

•	And so on...

This is exactly what Caesar Cipher does! It shifts every letter in your message by a certain number of positions in the alphabet.

Real Example:
•	Original message: "HELLO"
•	Shift: 3 (move each letter 3 positions forward)
•	Encrypted message: "KHOOR"

Why?
•	H → K (H is 8th letter, K is 11th letter)
•	E → H (E is 5th letter, H is 8th letter)
•	L → O (L is 12th letter, O is 15th letter)
•	L → O
•	O → R (O is 15th letter, R is 18th letter)

What We Need to Build:

A program that:
1.	Takes a message from the user (like "HELLO")
2.	Takes a shift number (like 3)
3.	Can encrypt (scramble) the message
4.	Can decrypt (unscramble) the message back

Step 2: Break the Problem into Small Sub-Tasks
Let's think about what we need to do, piece by piece:

Sub-Task 1: Get Input from User
• Ask for a message (text to encrypt/decrypt)
•	Ask for a shift value (how many positions to move)
•	Ask if they want to encrypt or decrypt

Sub-Task 2: Process Each Character
For encryption:
•	Look at each letter in the message one by one
•	If it's a letter (A-Z), shift it forward
•	If it's not a letter (space, comma, etc.), keep it the same

Sub-Task 3: Handle the "Wrap Around" Problem
•	What happens when we shift 'Z' by 3?
•	It should become 'C' (Z → A → B → C)
•	We need to wrap back to the beginning of the alphabet

Sub-Task 4: Create Encryption Function
•	Take the message and shift value
•	Return the encrypted message

Sub-Task 5: Create Decryption Function
•	Same as encryption, but shift backwards
•	If we encrypted with +3, decrypt with -3

Sub-Task 6: Display Results
•	Show the user their encrypted or decrypted message    

Step 3: Writing the actual code

In the Caesar_cipher.py file


Step 4: Explain What the Output Means and Why It Is Correct

Understanding the Output:

When we run the program with:
•	Input: "HELLO"
•	Shift: 3
•	Action: Encrypt
Output: Encrypted message: KHOOR

Why Is This Correct?
Let's verify letter by letter:
Original Alphabet: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Shifted by 3:      D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

H → K ✓ (Count 3 forward from H: H-I-J-K)
E → H ✓ (Count 3 forward from E: E-F-G-H)
L → O ✓ (Count 3 forward from L: L-M-N-O)
L → O ✓
O → R ✓ (Count 3 forward from O: O-P-Q-R)
Testing Decryption:
If we now decrypt "KHOOR" with shift 3:
K → H (Count 3 backward from K: K-J-I-H)
H → E (Count 3 backward from H: H-G-F-E)
O → L (Count 3 backward from O: O-N-M-L)
O → L
R → O (Count 3 backward from R: R-Q-P-O)

Result: "HELLO" ✓ (We got our original message back!)

Why the Code Works:
1.	ord() and chr():
•	These functions convert between letters and numbers
•	Computers store letters as numbers (ASCII codes)
•	This lets us do math on letters!
3.	Modulo (%) Operation:
•	Ensures we stay within 0-25 range
•	Automatically wraps around the alphabet
•	Example: 28 % 26 = 2 (goes back to beginning)
4.	Negative Shift for Decryption:
•	Shifting forward by 3 is encryption
•	Shifting backward by 3 (or forward by -3) is decryption
•	They're opposite operations that cancel each other

Complete Example Session:
========================================
   CAESAR CIPHER - ENCRYPTION TOOL
========================================

Enter your message: Hello World
Enter shift value (number): 5
Do you want to (E)ncrypt or (D)ecrypt? E

Encrypted message: MJQQT BTWQI
Verification:
•	H (+5) → M
•	e (+5) → J (converted to uppercase first)
•	l (+5) → Q
•	l (+5) → Q
•	o (+5) → T
•	(space stays as space)
•	W (+5) → B
•	o (+5) → T
•	r (+5) → W
•	l (+5) → Q
•	d (+5) → I

