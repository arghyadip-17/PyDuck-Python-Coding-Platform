# problems.py

problems = {
    "sum": {
        "id": "sum",
        "title": "Sum of Two Numbers",
        "description": "Take two integers as input and print their sum || Sample Input: 2 3 ||  Sample Output: 5",

        "tests": [
            ("2 3", "5"),
            ("10 20", "30"),
            ("-5 5", "0")
        ]
    },

    "square": {
        "id": "square",
        "title": "Square of a Number",
        "description": "Take an integer as input and print its square || Sample Input: 4 ||  Sample Output: 16",
        "tests": [
            ("4", "16"),
            ("-3", "9"),
            ("10", "100")
        ]
    },

    "multiply": {
        "id": "multiply",
        "title": "Multiplication of Two Numbers",
        "description": "Take two integers as input and print their multiplication || Sample Input: 2 3 ||  Sample Output: 6",
        "tests": [
            ("2 3", "6"),
            ("5 0", "0"),
            ("-2 4", "-8")
        ]
    },
    "evenodd": {
        "id": "evenodd",
        "title": "Even Odd Test",
        "description": "Take an integer as input and print whether it is Even or Odd ||  Sample Input: 2 ||  Sample Output: EVEN",
        "tests": [
            ("2", "EVEN"),
            ("5", "ODD"),
            ("6", "EVEN")
        ]
    },
    "ludo": {
        "id": "ludo",
        "title": "Playing Ludo",
        "description": "A is playing Ludo. According to the rules of Ludo, a player can enter a new token into the play only when he rolls a 6 on the die. In the current turn, A rolled the number X on the die. Determine if A can enter a new token into the play in the current turn or not ||  Sample Input: 4  || Sample Output: NO",
        "tests": [
            ("2", "NO"),
            ("5", "NO"),
            ("6", "YES")
        ]
    },
    "calculator": {
        "id": "calculator",
        "title": "Defect Calculator",
        "description": "You just bought a new calculator, but it seems to have a small problem: all its results have an extra 1 appended to the end. For example, if you ask it for 3 + 5, it'll print 81. Given A and B, can you predict what the calculator will print when you ask it for A+B? || Sample Input: 4 12 || Sample Output: 161",
        "tests": [
            ("2 5", "71"),
            ("5 3", "81"),
            ("6 4", "101")
        ]
    },
    "blood": {
        "id": "blood",
        "title": "Blood Donation",
        "description": "A blood drive aims to collect N number of blood donations. The drive has collected X donations so far. Find the remaining number of donations needed to reach the target || Sample Input: 7 5 || Sample Output: 2",
        "tests": [
            ("7 5", "2"),
            ("5 5", "0"),
            ("6 2", "4")
        ]
    },
    "ipl": {
        "id": "ipl",
        "title": "IPL Ticket Rush",
        "description": "GCETTS college students want to attend an IPL match. A total of N students from the college want to go while only M tickets are available for the match. Determine how many students won't be able to book tickets ||  Sample Input: 4 1 || Sample Output: 3",
        "tests": [
            ("4 1", "3"),
            ("5 7", "0"),
            ("6 4", "2")
        ]
    },
    "range": {
        "id": "range",
        "title": "Audible Range",
        "description": "Dev's cat binary hears frequencies starting from 67 Hertz to 45000 Hertz (both inclusive). If Dev's commands have a frequency of X Hertz, find whether binary can hear them or not. ||  Sample Input: 39  || Sample Output: NO",
        "tests": [
            ("39", "NO"),
            ("45550", "NO"),
            ("600", "YES")
        ]
    },
    "tall": {
        "id": "tall",
        "title": "Who Is Taller?",
        "description": "Alen and Bobo were having an argument about which of them is taller than the other. Chan got irritated by the argument, and decided to settle the matter once and for all. Chan measured the heights of Alen and Bobo, and got to know that Alen's height is X centimeters and Bobo's height is Y centimeters. Help Chan decide who is taller. It is guaranteed that X ≠ Y ||  Sample Input: 170 160 || Sample Output: A",
        "tests": [
            ("170 160", "A"),
            ("160 165", "B"),
            ("160 150", "A")
        ]
    },
    
    "target": {
        "id": "target",
        "title": "Reach The Target",
        "description": "There is a cricket match going on between two teams A and B.Team B is batting second and got a target of X runs. Currently, team B has scored Y runs. Determine how many more runs Team B should score to win the match. Note: The target score in cricket matches is one more than the number of runs scored by the team that batted first ||  Sample Input: 200 160 || Sample Output: 40",
        "tests": [
            ("200 160", "40"),
            ("160 105", "55"),
            ("160 100", "60")
        ]
    },
     "candy": {
        "id": "candy",
        "title": "Candy Division",
        "description": "There are three friends and a total of N candies. There will be a fight amongst the friends if all of them do not get the same number of candies. Duck wants to divide all the candies such that there is no fight. Find whether such distribution is possible ||  Sample Input: 3  || Sample Output: YES",
        "tests": [
            ("3", "YES"),
            ("4", "NO"),
            ("6", "YES")
        ]
    },
     "money": {
        "id": "money",
        "title": "Prize Money",
        "description": "In a coding contest, there are prizes for the top rankers. The prize scheme is as follows: Top 10 participants receive rupees X each. Participants with rank 11 to 100 (both inclusive) receive rupees Y each. Find the total prize money over all the contestants ||  Sample Input: 400  30  || Sample Output: 6700",
        "tests": [
            ("400 30", "6700"),
            ("1000 100", "19000"),
            ("80 1", "890")
        ]
    },
    "max": {
        "id": "max",
        "title": "Second MAX of Three",
        "description": "Write a program that accepts sets of three numbers, and prints the second-maximum number among the three ||  Sample Input: 1  2  3  || Sample Output: 2",
        "tests": [
            ("1 2 3", "2"),
            ("10 100 50", "50"),
            ("80 10 17", "17")
        ]
    },
    "messi": {
        "id": "messi",
        "title": "Messi vs Ronaldo",
        "description": "In Duckland, a football player gets 2 points for each goal and 1 point for each assist. Messi has A goals and B assists this season, whereas Ronaldo has X goals and Y assists. Find out the player with more points this season ||  Sample Input: 91  22  60  30  || Sample Output: Messi",
        "tests": [
            ("91 22 60 30", "Messi"),
            ("40 30 50 10", "Equal"),
            ("60 30 80 20", "Ronaldo")
        ]
    },
     "rain": {
        "id": "rain",
        "title": "Rain In Duckland ",
        "description": "In Duckland, precipitation is measured using a rain gauge in millimetre per hour. Duck categorises rainfall as: LIGHT, if rainfall is less than 3 millimetre per hour. MODERATE, if rainfall is greater than equal to 3 millimetre per hour and less than 7 millimetre per hour. HEAVY if rainfall is greater than equal to 7 millimetre per hour. Given that it rains at X millimetre per hour on a day, find whether the rain is LIGHT, MODERATE, or HEAVY ||  Sample Input: 2  || Sample Output: LIGHT",
        "tests": [
            ("2", "LIGHT"),
            ("20", "HEAVY"),
            ("4", "MODERATE")
        ]
    },
    "chess": {
        "id": "chess",
        "title": "Chess Time",
        "description": "Duck has recently started playing chess, and wants to play as many games as possible. He calculated that playing one game of chess takes at least 20 minutes of his time. Duck has N hours of free time. What is the maximum number of complete chess games he can play in that time? ||  Sample Input: 10  || Sample Output: 30",
        "tests": [
            ("10", "30"),
            ("7", "21"),
            ("3", "9")
        ]
    },
    "math": {
        "id": "math",
        "title": "Math Enrollment",
        "description": "For the upcoming semester, the admins of your university decided to keep a total of X seats for the MATH course. A student interest survey was conducted by the admins and it was found that Y students were interested in taking up the MATH course. Find the minimum number of extra seats that the admins need to add into the MATH course to make sure that every student who is interested in taking the course would be able to do so ||  Sample Input: 1 1  || Sample Output: 0",
        "tests": [
            ("1 1", "0"),
            ("12 34", "22"),
            ("50 49", "0")
        ]
    },
    "design": {
        "id": "design",
        "title": "Interior Design",
        "description": "Duck decided to redecorate his house, and now needs to decide between two different styles of interior design. For the first style, tiling the floor will cost X1 rupees and painting the walls will cost Y1 rupees. For the second style, tiling the floor will cost X2 rupees and painting the walls will cost Y2 rupees. Duck will choose whichever style has the lower total cost. How much will Chef pay for his interior design? ||  Sample Input: 10 20 9 25  || Sample Output: 30",
        "tests": [
            ("10 20 9 25", "30"),
            ("10 20 9 20", "29"),
            ("10 20 20 10", "30")
        ]
    },
    "atm": {
        "id": "atm",
        "title": "ATM Balance",
        "description": "Dev would like to withdraw X US Dollar from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Dev's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 US Dollar. Calculate Dev's account balance after an attempted transaction ||  Sample Input: 30 120.0  || Sample Output: 89.5",
        "tests": [
            ("30 120.0", "89.5"),
            ("42 120.0", "120.0"),
            ("300 120.0", "120.0")
        ]
    },
    "stick": {
        "id": "stick",
        "title": "Break The Stick",
        "description": "Duck has a stick of length N. He can break the stick into 2 or more parts such that the parity of length of each part is same. For example, a stick of length 11 can be broken into three sticks of lengths {3,3,5} since each part is odd, but it cannot be broken into two sticks of lengths {5,6} since one is even and the other is odd. Duck can then continue applying this operation on the smaller sticks he obtains, as many times as he likes. Can Duck obtain a stick of length exactly X by doing this? ||  Sample Input: 6  1  || Sample Output: YES",
        "tests": [
            ("6 1", "YES"),
            ("3 2", "NO"),
            ("4 3", "YES")
        ]
    },
    "exam": {
        "id": "exam",
        "title": "Passed In Exam",
        "description": "In Duckland, there are X schools, and each school has Y students. The year end results are in and a total of Z students passed the exams. Assuming that all students appeared for the exams, find whether the number of students who passed in Duckland was strictly greater than 50% ||  Sample Input: 2  10  12  || Sample Output: YES",
        "tests": [
            ("2 10 12", "YES"),
            ("2 10 3", "NO"),
            ("1 5 3", "YES")
        ]
    },
    "ac": {
        "id": "ac",
        "title": "AC Temperature",
        "description": "There are three people sitting in a room - Alen, Bobo, and Chan. They need to decide on the temperature to set on the air conditioner. Everyone has a demand each: Alen wants the temperature to be at least A degrees. Bobo wants the temperature to be at most B degrees. Chan wants the temperature to be at least C degrees. Can they all agree on some temperature, or not? ||  Sample Input: 30 35 25  || Sample Output: YES",
        "tests": [
            ("30 35 25", "YES"),
            ("30 35 40", "NO"),
            ("30 35 35", "YES")
        ]
    },
    "exit": {
        "id": "exit",
        "title": "Nearest Exit",
        "description": "There are two exits in a bus with 100 seats: First exit is located beside seat number 1. Second exit is located beside seat number 100. Seats are arranged in a straight line from 1 to 100 with equal spacing between any 2 adjacent seats. A passenger prefers to choose the nearest exit while leaving the bus. Determine the exit taken by passenger sitting on seat X. ||  Sample Input: 50  || Sample Output: LEFT",
        "tests": [
            ("50", "LEFT"),
            ("100", "RIGHT"),
            ("30", "LEFT")
        ]
    },
    "reverse": {
        "id": "reverse",
        "title": "Reverse A Number",
        "description": "Given an Integer N, write a program to reverse it ||  Sample Input: 12345  || Sample Output: 54321",
        "tests": [
            ("12345", "54321"),
            ("102", "201"),
            ("30547", "74503")
        ]
    },
}
