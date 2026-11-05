# Grade Processor Srquence Diagram



```
mermaid
sequenceDiagram
	actor Instructor
    participent Program
    Instructor->>Program: Start grade processing
    Program->>Instructor: Request grade
    Program->>Instructor: How many grades?
    Intsructor->>Program: Enter 3
    loop for each student
    	Program->>Instructor: Request Grade
        Instrucror->>Program: Enter grade
        Program->>Program: Update total
        Program->>Program: Update pass/fail count
    end
    Program->>Program: Calculater average
    Program-->>Instructor: Display summary
```
