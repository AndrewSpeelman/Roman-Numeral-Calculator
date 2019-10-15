# Roman-Numeral-Calculator

This calculator will calculate roman numeral expressions that use the addition (+) and subtraction (-) operators. The program
does not use any conversion to arabic numbers (integers) and will use the algorithms that the Roman's likely followed below.  
The algorithm used is as follows: 

Addition:
1. Substitute for any subtractives in both values; that is; "uncompact" the Roman values.
2. Put the two values together—catenate them.
3. Sort the symbols in order from left-to-right with the "largest" symbols on the left.
4. Starting with the right end, combine groups of the same symbols that can make a "larger" one and substitute the single larger one.
5. Compact the result by substituting subtractives where possible.

Subtraction:
1. Substitute for any subtractives in both values.
2. Any symbols occurring in the second value are "crossed out" in the first.
  1. If the symbol appears in the first, simply cross it out.
  2. If not, then convert a "larger" symbol into appropriate multiples of the needed one, then cross out.
3. Rewrite without the crossed out symbols.
4. Check for any groupings of the same symbol that needs to be replaced with a "larger" one.
5. Compact the result by substituting subtractives where possible.

Inside 'main.py' you will find a few input examples given in main.
