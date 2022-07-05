import pandas as pd

df=pd.read_csv("./CSV/IPL_2021.csv")


#player
class runs_info:
    def __init__(self,player):
        self.name=player
        
    def dot(self):
        name=self.name
        dot=df[df['striker']==name]
        val=dot['dot'].sum()
        return val
    
    def once(self):
        name=self.name
        once=df[df['striker']==name]
        val=once['one'].sum()
        return val
    
    def two(self):
        name=self.name
        two=df[df['striker']==name]
        val=two['two'].sum()
        return val
    
    def three(self):
        name=self.name
        three=df[df['striker']==name]
        val=three['three'].sum()
        return val
        
        
    def four(self):
        name=self.name
        four=df[df['striker']==name]
        val=four['four'].sum()
        return val
    
    
    def five(self):
        name=self.name
        five=df[df['striker']==name]
        val=five['five'].sum()
        return val
    
    
    def six(self):
        name=self.name
        six=df[df['striker']==name]
        val=six['six'].sum()
        return val

#Ball
# class ball(runs_info):
        
    def ball_faced(self):
        tmp=df[df['striker']==self.name]
        ttl=len(tmp)
        wd=tmp['w'].sum()
        return ttl-wd
    
    
    
# class runs(ball):
    
    def single_runs(self):
        val=runs_info.once(self)
        return val
    
    def two_runs(self):
        val=runs_info.two(self)*2
        return val
    
    def three_runs(self):
        val=runs_info.three(self)*3
        return val
    
    def four_runs(self):
        val=runs_info.four(self)*4
        return val
    
    def five_runs(self):
        val=runs_info.five(self)*5
        return val
    
    
    def six_runs(self):
        val=runs_info.six(self)*6
        return val
    
    
    def total_runs(self):
        runs_df=df[df['striker']==self.name]
        val=runs_df['runs_off_bat'].sum()
        return val