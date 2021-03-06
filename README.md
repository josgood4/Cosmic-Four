# Cosmic Four

## Prerequisites 
- Python 3  
- `pip install inflect`  
- `pip install csv`  

## Why Is 4 "Cosmic"?
Interestingly, if you perform the following procedure, you will always arrive at the number 4 (at least in the English language):
1. Begin with an arbitrary integer
2. Spell out the integer in words
3. Count the number of letters in the word-form of the number
4. Return to step (2) with the result from step (3) and continue until you reach 4

For example, beginning with the number 10:  
  - 10 spelled out is "ten,"   which has 3 letters  
  - 3  spelled out is "three," which has 5 letters  
  - 5  spelled out is "five,"  which has 4 letters  
  - 4  spelled out is "four,"  which has 4 letters  
...

If you continue repeating this process, you will always arrive at the number 4.

4 is "cosmic" because it is the only number which has the same number of letters as its numerical value.

## Main Proof
First, to show this works with all positive numbers:
### Base Case: `1<=n<=4`
Each of these numbers leads back to 4:  
 - 1 -> 3 -> 5 -> 4
 - 2 -> 3 -> 5 -> 4
 - 3 -> 5 -> 4
 - 4 -> 4 -> ...  
### Inductive Step:  
Assume that `n>4` and for all `0<i<n`, `i` will lead back to 4. Consider `n+1`.  
For all `n>4`, the number of letters in the word-form of that number is less than the numerical value of the number.<sup>[by the lemma below]</sup> `n+1` will thus lead to a smaller (positive) number, and, by induction, one that also leads back to 4.  
QED  
  
To put it in simpler terms, each iteration gets closer and closer to the number 4 (by shrinking the number that iteration started with). A number can't have a negative number of letters (nor zero letters), so this means that the process produces smaller and smaller positive integers until it eventually produces either a 1, 2, 3, or 4, all of which lead back to 4, as shown above.  
  
As for other special cases:
 - 0 -> 4
 - negative numbers -> some positive number -> ... (as shown above) -> 4
 
## Lemma: Letter-Count < Numerical Value 
(for n > 4)  
### Letter-count vs. Numerical Value
[![Chart 1a](chart1a.png)](https://docs.google.com/spreadsheets/d/e/2PACX-1vQUwPpcpuZXmU4O2UB8aWidqYp2kwAxdC1AEnqzMDTWGGSGKwOAHZdHX4D-G8Wc8wd7iEhYemALRpAP/pubchart?oid=722479629&format=interactive)  
The letter-count increases significantly every time a new decimal place is reach, since an additional "hundred", "thousand", etc. must be added to the number's word form. This increase is no more than twenty letters for every power of 10 which is reached. Thus, the letter-count increases roughly logarithmically with respect to the numerical value of the numbers, and thus is always less than its numerical value.

## Results
The following charts show the result of performing the above process once per number from 0 to 100 and from 0 to 10000, respectively. As you can see, as numbers grow larger, the number of letters in their spelled-out versions increases very slowly, lending more confidence to the idea that every number will eventually get back to four (as explained above).  
_(click charts below for interactive versions)_
### Numbers from 0 to 100 
[![Chart 1](chart1.png)](https://docs.google.com/spreadsheets/d/e/2PACX-1vQUwPpcpuZXmU4O2UB8aWidqYp2kwAxdC1AEnqzMDTWGGSGKwOAHZdHX4D-G8Wc8wd7iEhYemALRpAP/pubchart?oid=277922962&format=interactive)

### Numbers from 0 to 10000
[![Chart 2](chart3.png)](https://docs.google.com/spreadsheets/d/e/2PACX-1vQUwPpcpuZXmU4O2UB8aWidqYp2kwAxdC1AEnqzMDTWGGSGKwOAHZdHX4D-G8Wc8wd7iEhYemALRpAP/pubchart?oid=1275451316&format=interactive)

