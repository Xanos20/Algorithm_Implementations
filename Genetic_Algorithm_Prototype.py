import pdb
import random
import secrets



"""
Prototype of a genetic algorithm for organism adaptation
https://stackoverflow.com/questions/3783530/python-tuple-to-dict
"""
class Organisms(object):
    def __init__(self, traits):
        self.stats = []
        #pdb.set_trace()
        for j in range(traits+1):
            #pdb.set_trace()
            rand = secrets.randbelow(101)
            if(rand > 50):
                self.stats.append(1)
            else:
                self.stats.append(0)
        #pdb.set_trace()
    def get_stats(self):
        if(self.stats == None):
            return(None)
        ret = 0
        for bit in self.stats:
            ret += bit
        return(ret)
    def child(self, stats):
        self.stats = stats

class Simulation():
    def __init__(self, population, traits):
        self.organisms = {}
        self.population = population
        self.traits = traits

    def make_organisms(self):
        for i in range(self.population):
            self.organisms[i] = (Organisms(self.traits))
    def cycle(self):
        # cannot update dict while iterating so add children after loop
        new_len = len(self.organisms)-1
        new_organism_keys = []
        new_organism_stats = []

        all_stats = {}
        for o in self.organisms:
            all_stats[o] = self.organisms[o].get_stats()
            # take top half
        sorted_stats = sorted(all_stats.items(), key=lambda x: x[1])
        #pdb.set_trace()


        for o in self.organisms:
            #pdb.set_trace()
            stats = self.organisms[o].get_stats()
            #print(o)

            if(stats == None):
                # organism is not accounted for
                continue
            if(stats == 0):
                # kill off organisms with no traits
                print("No organism")
                continue
            # find organism relative position
            p = 0
            while(sorted_stats[p][0] != o):
                p = p + 1
            #pdb.set_trace()
            if(p >= len(sorted_stats)/2.0):
                new_len = new_len + 1
                new_organism_keys.append(new_len)
                new_organism_stats.append(self.organisms[o].stats)
                #self.organisms[len(self.organisms)+1] = Organisms(self.traits)
            """
            if(stats >= self.traits/2):
                # asexually create new children
                new_len = new_len + 1
                new_organism_keys.append(new_len)
                new_organism_stats.append(self.organisms[o].stats)
                #self.organisms[len(self.organisms)+1] = Organisms(self.traits)
            """
            # events that can kill
            rand = secrets.randbelow(101)
            if(rand > 90):
                for s in self.organisms[o].stats:
                    self.organisms[o].stats[s] = 0
                continue

        # add new children
        n = 0
        #pdb.set_trace()
        while(n < len(new_organism_keys)):
            self.organisms[new_organism_keys[n]] = Organisms(self.traits)
            self.organisms[new_organism_keys[n]].child(new_organism_stats[n])
            # potentially mutate new children
            for bit in self.organisms[new_organism_keys[n]].stats:
                rand_mut = secrets.randbelow(101)
                if(rand_mut > 80):
                    # flip bits
                    print("Mutated O=" + str(new_organism_keys[n]))
                    if(self.organisms[new_organism_keys[n]].stats[bit] == 1):
                        self.organisms[new_organism_keys[n]].stats[bit] = 0
                    else:
                        self.organisms[new_organism_keys[n]].stats[bit] = 1
            n = n + 1
            continue
        for k in self.organisms:
            print("Organism: " + str(k) + " Traits: " + str(self.organisms[k].stats))
        #pdb.set_trace()
        #print("Simulation Iteration End")





def main():
    sim = Simulation(6, 4)
    sim.make_organisms()
    i = 0
    while(i < 4):
        sim.cycle()
        print("Simulation=" + str(i) + " Iteration End")
        i = i + 1

    #sim.cycle()
    #sim.cycle()
    #pdb.set_trace()

main()
