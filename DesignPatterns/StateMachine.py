from abc import ABC, abstractmethod


class State(ABC):
    
    def __init__(self, s_m, element, state, bp, mp):
        self.state_machine = s_m
        self.element = element
        self.state = state
        self.boil_point = bp
        self.melt_point = mp
        print("State Interface Constructed")
        
    @abstractmethod
    def boil(self, tmp):
        pass
    
    @abstractmethod
    def melt(self, tmp):
        pass
    
    
class SolidState(State):
    
    def __init__(self, s_m, element, bp, mp):
        super().__init__(s_m, element, "Solid", bp, mp)

    def boil(self, tmp):
        if tmp >= self.boil_point:
            print("Coverting Solid to Gas!")
            self.state_machine.state = GasState(self.state_machine, self.element, self.boil_point, self.melt_point)
        else:
            print("Temp too low!")
            
    def melt(self, tmp):
        if tmp >= self.melt_point:
            print("Coverting Solid to Liquid!")
            self.state_machine.state = LiquidState(self.state_machine, self.element, self.boil_point, self.melt_point)
        else:
            print("Temp too low!")


class LiquidState(State):
    
    def __init__(self, s_m, element, bp, mp):
        super().__init__(s_m, element, "Liquid", bp, mp)

    def boil(self, tmp):
        if tmp >= self.boil_point:
            print("Coverting Liquid to Gas!")
            self.state_machine.state = GasState(self.state_machine, self.element, self.boil_point, self.melt_point)
        else:
            print("Temp too low!")           

    def melt(self, tmp):
        print("Already a Liquid!")


class GasState(State):
    
    def __init__(self, s_m, element, bp, mp):
        super().__init__(s_m, element, "Gas", bp, mp)

    def boil(self, tmp):
            print("Cant Convert, Already a gas!")

    def melt(self, tmp):
        print("Already a Gas!")


class StateMachine:
    
    def __init__(self, element, bp, mp):
        self.state = SolidState(self, element, bp, mp)
        
    def reset_state(self):
        self.state = SolidState(self, self.state.element, self.state.boil_point, self.state.melt_point)
        
    def boil(self, tmp):
        self.state.boil(tmp)
    
    def melt(self, tmp):
        self.state.melt(tmp)
    
            

def test_sm():
    
    water = StateMachine("Water", 100, 0)
    
    water.melt(25)
    water.boil(200)
    water.boil(150)
    
    water.reset_state()
    
    water.boil(140)
    water.melt(25)
    
    water.reset_state()

    water.melt(25)
    water.melt(25)
    

    
    print("Done")
    
    

    