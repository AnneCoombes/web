This is just a test to start examining web.py

Download the code.  
Open it up using VS Code.  
Run the code.  
In a browser try the following URLs:

1. http://localhost:8080/
   > This will display:  
   > Hello world!
2. localhost:8080/health
   > This will display:  
   >  I am running
3. http://localhost:8080/Andrew
   > This will display:  
   > I just wanted to say Hello to Andrew.
4. http://localhost:8080/count
   > This will display:  
   > 1 => 1  
   > 2 => 3  
   > 3 => 6  
   > 4 => 10  
   > 5 => 15  
   > 6 => 21  
   > 7 => 28  
   > 8 => 36  
   > 9 => 45
5. http://localhost:8080/count?start=5
   > This will display:  
   >  5 => 5  
   > 6 => 11  
   > 7 => 18  
   > 8 => 26  
   > 9 => 35
6. http://localhost:8080/count?start=5&num=8
   > This will display:  
   >  5 => 5  
   > 6 => 11  
   > 7 => 18
