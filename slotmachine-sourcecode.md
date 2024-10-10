ClrHome
100→B
Disp "WELCOME TO"
Disp "SLOT MACHINE"
Pause 

Lbl S
ClrHome
Disp "BALANCE ",B
Input "BET AMOUNT? ",A
If A>B or A=0
Then
Disp "INVALID BET!"
Pause 
Goto S
End

B-A→B

randInt(1,5)→R
randInt(1,5)→T
randInt(1,5)→U

ClrHome
Disp "SPINNING..."
Pause 

Output(2,4,R) 
Output(2,6,T)
Output(2,8,U)
Pause 

0→P
If R=T and T=U      
Then
A*5→P
Else
If R=T or T=U or R=U  
Then
A*0.5→P
End
End

If P>0
Then
Disp "YOU WON!",P
B+P→B
Else
Disp "YOU LOST!"
End

Pause 

If B>0
Goto S

Disp "OUT OF MONEY!"
End