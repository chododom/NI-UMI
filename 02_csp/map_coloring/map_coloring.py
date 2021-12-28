# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:14:55 2021

@author: Dominik Chodounský
"""

class Map():
    def __init__(self, colors, nodes):
        self.colors = colors
        self.nodes = nodes
        self.constraints = {}
        self.coloring = {}
        
        for n in self.nodes:
            self.constraints[n] = []
            self.coloring[n] = None
        
    def add_constraint(self, n1, n2):
        self.constraints[n1].append(n2)
        self.constraints[n2].append(n1)


    def check_consistency(self, node):
        for neighbour in self.constraints[node]:
            if self.coloring[neighbour] == self.coloring[node]:
                return False
        return True

    def backtracking(self):
        # find nodes without colors
        no_color = []
        for n in self.nodes:
            if self.coloring[n] is None:
                no_color.append(n)
                
        if len(no_color) == 0:
            print('All nodes have been assigned a color!')
            
            for n in self.nodes:
                if not self.check_consistency(n):
                    print('FAIL')
            
            return self.coloring
                
        current = no_color[0]
        for color in self.colors:
            self.coloring[current] = color
            if self.check_consistency(current):
                result = self.backtracking()
                if result is not None:
                    return result
            self.coloring[current] = None # backtracking
        return None
    
    
    def get_conflicts(self, node):
        conflicts = []
        for neighbour in self.constraints[node]:
            if self.coloring[neighbour] == self.coloring[node]:
                conflicts.append(neighbour)
        return conflicts
    
    def backjumping(self):
        # find nodes without colors
        no_color = []
        for n in self.nodes:
            if self.coloring[n] is None:
                no_color.append(n)
        if len(no_color) == 0:
            
            for n in self.nodes:
                if not self.check_consistency(n):
                    print('FAIL')
            
            return self.coloring, None
        
        current = no_color[0]
        answer = None
        conflict_set = []
        for color in self.colors:
            self.coloring[current] = color
            if self.check_consistency(current):
                new_map = Map(self.colors, self.nodes)
                new_map.constraints = self.constraints.copy()
                new_map.coloring = self.coloring.copy()
                answer, new_conflicts = new_map.backjumping()
            else:
                new_conflicts = self.get_conflicts(current)
                new_conflicts.append(current)
            if answer != None:
                return answer, None # jump back
            elif current not in new_conflicts:
                return None, new_conflicts
            else:
                conflict_set = list(set(conflict_set + new_conflicts))
                conflict_set.remove(current)
        return None, conflict_set


if __name__ == "__main__":
    
    
    
    '''
    # Australia:
        
    COLORS = {'R', 'G', 'B'}
    NODES = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
        
    _map = Map(COLORS, NODES)
    
    _map.add_constraint('WA', 'NT') 
    _map.add_constraint('WA', 'SA')
    _map.add_constraint('NT', 'Q')
    _map.add_constraint('NT', 'SA')
    _map.add_constraint('SA', 'Q')
    _map.add_constraint('SA', 'NSW')
    _map.add_constraint('NSW', 'Q')
    _map.add_constraint('NSW', 'V')
    
    coloring = _map.backtracking()
    print(coloring)
    '''
    
    # Czech Republic

    COLORS = {'R', 'G', 'B', 'O'}
    NODES = [
                'Hlavní město Praha',
                'Jihočeský kraj',
                'Jihomoravský kraj',
                'Karlovarský kraj',
                'Královehradecký kraj',
                'Liberecký kraj',
                'Moravskoslezský kraj',
                'Olomoucký kraj',
                'Pardubický kraj',
                'Plzeňský kraj',
                'Středočeský kraj',
                'Ústecký kraj',
                'Vysočina',
                'Zlínský kraj'
            ]
        
    _map = Map(COLORS, NODES)
    
    _map.add_constraint('Karlovarský kraj', 'Plzeňský kraj') 
    _map.add_constraint('Karlovarský kraj', 'Ústecký kraj')
    _map.add_constraint('Ústecký kraj', 'Plzeňský kraj')
    _map.add_constraint('Ústecký kraj', 'Středočeský kraj')
    _map.add_constraint('Ústecký kraj', 'Liberecký kraj')
    _map.add_constraint('Plzeňský kraj', 'Středočeský kraj')
    _map.add_constraint('Plzeňský kraj', 'Jihočeský kraj')
    _map.add_constraint('Jihočeský kraj', 'Středočeský kraj')
    _map.add_constraint('Jihočeský kraj', 'Vysočina') 
    _map.add_constraint('Jihočeský kraj', 'Jihomoravský kraj')
    _map.add_constraint('Středočeský kraj', 'Hlavní město Praha')
    _map.add_constraint('Středočeský kraj', 'Liberecký kraj')
    _map.add_constraint('Středočeský kraj', 'Královehradecký kraj')
    _map.add_constraint('Královehradecký kraj', 'Pardubický kraj')
    _map.add_constraint('Středočeský kraj', 'Pardubický kraj')
    _map.add_constraint('Středočeský kraj', 'Vysočina')
    _map.add_constraint('Liberecký kraj', 'Královehradecký kraj')
    _map.add_constraint('Vysočina', 'Pardubický kraj')
    _map.add_constraint('Jihomoravský kraj', 'Pardubický kraj')
    _map.add_constraint('Olomoucký kraj', 'Pardubický kraj')
    _map.add_constraint('Vysočina', 'Jihomoravský kraj')
    _map.add_constraint('Jihomoravský kraj', 'Olomoucký kraj')
    _map.add_constraint('Jihomoravský kraj', 'Zlínský kraj')
    _map.add_constraint('Moravskoslezský kraj', 'Olomoucký kraj')
    _map.add_constraint('Zlínský kraj', 'Olomoucký kraj')
    _map.add_constraint('Zlínský kraj', 'Moravskoslezský kraj')
    
    coloring, _ = _map.backjumping()
    print(coloring)
    
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    