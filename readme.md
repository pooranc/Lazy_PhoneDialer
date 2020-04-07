**Phone Dialer -**

Laziest Way to dial a n-digit number on a standard push button telephone.

List of requirements :
- Standard Telephone button layout, so Assumptions digit “1” at a position (0,0) likewise; 

* *
"""
  1(0,0)  2(0,1)  3(0,2)
  4(1,0)  5(1,1)  6(1,2)
  7(2,0)  8(2,1)  9(2,2)
  *(3,0)  0(3,1)  #(3,2)
"""
* *

- Starting finger position is at * and #
- Need a Euclidian distance method to calculate the distance between the current digit input position and the digit’s position on the     left and right fingers. Note: “SciPy.Spatial” library is used to calculate the Euclidean distance between 2 points.
- Based on the Euclidian distance move the finger which has less distance.
- The smallest amount of Euclidian distance both fingers combined to dial phone number. 
 

**Implementation link: **

https://github.com/pooranc/Lazy_PhoneDialer 

**Idea: **

1. Each digit in the telephone number is passed to dial() in dialer.py class
2. The first position of the fingers is assumed to be at * and #, so this will be the current position of fingers. 
3. Euclidian distance is calculated with respect to (w.r.t) Left and right fingers,
4. The combined distance of both fingers is stored.
5. Movement of the fingers is decided based on the distance values
    a.	If the distance is equal w.r.t both the fingers, the left finger is given the priority to move position.
    b.	Distance wr.t right finger is less than w.r.t left finger, the right finger is moved to a new position
    c.	Vice versa w.r.t left finger

**Complexity: **

The time complexity is O(n), n being the number of digits in the telephone number. As each digit is passed to the algorithm in a for loop.

The space complexity is O(1), a constant k, k being the number of keys.


