The Cocke–Younger–Kasami algorithm (alternatively called CYK, or CKY) is a parsing algorithm for context-free grammars, named after its inventors, John Cocke, Daniel Younger and Tadao Kasami.
The standard version of CYK operates only on context-free grammars given in Chomsky normal form (CNF).
The importance of the CYK algorithm stems from its high efficiency in certain situations. Using Big O notation, the worst case running time of CYK is O ( n^3 ⋅ |G| ), where n is the length of the parsed string and | G | is the size of the CNF grammar G.


Pseudocode:

    Begin
          for ( i = 1 to n do )
          Vi1 { A | A → a is a production where ith symbol of x is a }
          for ( j = 2 to n do )
               for ( i = 1 to n - j + 1 do )
               Begin
                     Vij = ϕ
                     For k = 1 to j - 1 do
                     Vij = Vij ∪ { A | A → BC is a production where B is in Vik and C is in V(i + k)(j - k) }
               End
    End




use this command to run code:
python3 cyk.py

input.txt contains the given input.
Grammer.txt contains a free-context grammer.
The code is sensitive to 'S' as the starting symbol.  
Use uppercase characters as varaiables and lowercases as terminals.
Seperate each production rule with '|' or a new line.
