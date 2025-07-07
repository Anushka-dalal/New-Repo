# IPL Management System Project

class Player:
    def __init__(self,jn,nm,r,w,tn):
        self.jersy_no = jn
        self.name = nm
        self.runs = r
        self.wickets = w
        self.team_name = tn
        self.details = [jn,nm,r,w,tn]

    def get_runs(self):
        return self.runs

    def getName(self):
        return self.name
    
    def get_wickets(self):
        return self.wickets
    
    def get_jearsy_no(self):
        return self.jearsy_no
    
    def get_team_name(self):
        return self.team_name
    
    def set_jearsy_no(self,jn):
        self.jearsy_no = jn

    def set_name(self,n):
        self.name = n

    def set_runs(self,r):
        self.runs = r
    
    def set_wickets(self,w):
        self.wickets = w

    def set_team_name(self,tn):
        self.team_name = tn
    

p1 = Player(45, "Rohit Sharma", 6500, 1, "Mumbai Indians")
p2 = Player(33, "Hardik Pandya", 2000, 50, "Mumbai Indians")
p3 = Player(63, "Ishan Kishan", 2100, 0, "Mumbai Indians")
p4 = Player(77, "Suryakumar Yadav", 3000, 0, "Mumbai Indians")
p5 = Player(93, "Jasprit Bumrah", 60, 160, "Mumbai Indians")
p6 = Player(17, "Tilak Varma", 900, 0, "Mumbai Indians")
p7 = Player(99, "Piyush Chawla", 250, 180, "Mumbai Indians")
p8 = Player(22, "Tim David", 700, 0, "Mumbai Indians")
p9 = Player(66, "Akash Madhwal", 100, 25, "Mumbai Indians")
p10 = Player(6, "Nehal Wadhera", 500, 0, "Mumbai Indians")
p11 = Player(5, "Gerald Coetzee", 50, 20, "Mumbai Indians")

miteam = []

miteam.append(p1)
miteam.append(p2)
miteam.append(p3)
miteam.append(p4)
miteam.append(p5)
miteam.append(p6)
miteam.append(p7)
miteam.append(p8)
miteam.append(p9)
miteam.append(p10)
miteam.append(p11)

rcb = []

rcb.append(Player(18, "Virat Kohli", 7500, 4, "Royal Challengers Bengaluru"))
rcb.append(Player(97, "Faf du Plessis", 4300, 0, "Royal Challengers Bengaluru"))
rcb.append(Player(33, "Glenn Maxwell", 2700, 35, "Royal Challengers Bengaluru"))
rcb.append(Player(5, "Dinesh Karthik", 4400, 0, "Royal Challengers Bengaluru"))
rcb.append(Player(7, "Anuj Rawat", 300, 0, "Royal Challengers Bengaluru"))
rcb.append(Player(19, "Mahipal Lomror", 400, 0, "Royal Challengers Bengaluru"))
rcb.append(Player(6, "Cameron Green", 500, 20, "Royal Challengers Bengaluru"))
rcb.append(Player(11, "Mohammed Siraj", 60, 90, "Royal Challengers Bengaluru"))
rcb.append(Player(27, "Karn Sharma", 150, 70, "Royal Challengers Bengaluru"))
rcb.append(Player(21, "Reece Topley", 40, 25, "Royal Challengers Bengaluru"))
rcb.append(Player(23, "Yash Dayal", 20, 15, "Royal Challengers Bengaluru"))


print("Batsman in MI :")
mi_batsmen = filter(lambda p: p.get_runs() > 1000, miteam)
for i in mi_batsmen :
    print(i.getName())

print("\nBowlers in MI :")
mi_bowlers = filter(lambda p: p.get_wickets() > 20, miteam)
for i in mi_bowlers:
    print(i.getName())

print("\nBatsman of RCB :")
rcb_batsmen = filter(lambda p: p.get_runs() > 1000, rcb)
for i in rcb_batsmen :
    print(i.getName())

print("\nBowlers of RCB :")
rcb_bowlers = filter(lambda p: p.get_wickets() > 20, rcb)
for i in rcb_bowlers:
    print(i.getName())



