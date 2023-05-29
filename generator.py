#!/usr/bin/env python3

import sys
import random
import getopt

def cubeInit():
    red='red'
    orange='orange'
    white='white'
    green='green'
    yellow='yellow'
    blue='blue'
    cr=[[[red,red,red],[red,red,red],[red,red,red]],
        [[orange,orange,orange],[orange,orange,orange],[orange,orange,orange]],
        [[white,white,white],[white,white,white],[white,white,white]],
        [[green,green,green],[green,green,green],[green,green,green]],
        [[blue,blue,blue],[blue,blue,blue],[blue,blue,blue]],
        [[yellow,yellow,yellow],[yellow,yellow,yellow],[yellow,yellow,yellow]]]
    return cr

def F(CC):
    cm1= [[[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][0], CC[1][0][1], CC[3][0][0]], [CC[1][1][0], CC[1][1][1], CC[3][0][1]], [CC[1][2][0], CC[1][2][1], CC[3][0][2]]], #orange    
          [[CC[2][0][2], CC[2][1][2], CC[2][2][2]], [CC[2][0][1], CC[2][1][1], CC[2][2][1]], [CC[2][0][0], CC[2][1][0], CC[2][2][0]]], #white    
          [[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #green    
          [[CC[1][0][2], CC[1][1][2], CC[1][2][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[5][0][0], CC[5][0][1], CC[5][0][2]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[5][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow   
    return cm1

def Frev(CC):
    cm2= [[[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][0], CC[1][0][1], CC[4][0][0]], [CC[1][1][0], CC[1][1][1], CC[4][0][1]], [CC[1][2][0], CC[1][2][1], CC[4][0][2]]], #orange    
          [[CC[2][2][0], CC[2][1][0], CC[2][0][0]], [CC[2][2][1], CC[2][1][1], CC[2][0][1]], [CC[2][2][2], CC[2][1][2], CC[2][0][2]]], #white    
          [[CC[1][0][2], CC[1][1][2], CC[1][2][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #green    
          [[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[5][0][0], CC[5][0][1], CC[5][0][2]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[5][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow  
    return cm2

def B(CC):
    cm5= [[[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #red     
          [[CC[4][2][0], CC[1][0][1], CC[1][0][2]], [CC[4][2][1], CC[1][1][1], CC[1][1][2]], [CC[4][2][2], CC[1][2][1], CC[1][2][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[2][0][2]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[2][2][0], CC[2][2][1], CC[2][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[1][0][0], CC[1][1][0], CC[1][2][0]]], #green    
          [[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #blue    
          [[CC[5][0][2], CC[5][1][2], CC[5][2][2]], [CC[5][0][1], CC[5][1][1], CC[5][2][1]], [CC[5][0][0], CC[5][1][0], CC[5][2][0]]]] #yellow   
    return cm5

def Brev(CC):
    cm6= [[[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #red     
          [[CC[3][2][0], CC[1][0][1], CC[1][0][2]], [CC[3][2][1], CC[1][1][1], CC[1][1][2]], [CC[3][2][2], CC[1][2][1], CC[1][2][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[2][0][2]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[2][2][0], CC[2][2][1], CC[2][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #green    
          [[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[1][0][0], CC[1][1][0], CC[1][2][0]]], #blue    
          [[CC[5][2][0], CC[5][1][0], CC[5][0][0]], [CC[5][2][1], CC[5][1][1], CC[5][0][1]], [CC[5][2][2], CC[5][1][2], CC[5][0][2]]]] #yellow  
    return cm6

def L(CC):
    cm7= [[[CC[5][0][2], CC[0][0][1], CC[0][0][2]], [CC[5][0][1], CC[0][1][1], CC[0][1][2]], [CC[5][0][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][0], CC[1][0][1], CC[1][0][2]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[2][0][2], CC[2][0][1], CC[2][0][0]]], #orange    
          [[CC[0][2][0], CC[0][1][0], CC[0][0][0]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[2][2][0], CC[2][2][1], CC[2][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #green    
          [[CC[4][0][2], CC[4][1][2], CC[4][2][2]], [CC[4][0][1], CC[4][1][1], CC[4][2][1]], [CC[4][0][0], CC[4][1][0], CC[4][2][0]]], #blue    
          [[CC[1][2][2], CC[1][2][1], CC[1][2][0]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[5][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow  
    return cm7

def Lrev(CC):
    cm8= [[[CC[2][0][2], CC[0][0][1], CC[0][0][2]], [CC[2][0][1], CC[0][1][1], CC[0][1][2]], [CC[2][0][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][0], CC[1][0][1], CC[1][0][2]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[5][0][2], CC[5][0][1], CC[5][0][0]]], #orange    
          [[CC[1][2][2], CC[1][2][1], CC[1][2][0]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[2][2][0], CC[2][2][1], CC[2][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #green    
          [[CC[4][2][0], CC[4][1][0], CC[4][0][0]], [CC[4][2][1], CC[4][1][1], CC[4][0][1]], [CC[4][2][2], CC[4][1][2], CC[4][0][2]]], #blue    
          [[CC[0][2][0], CC[0][1][0], CC[0][0][0]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[5][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow   
    return cm8

def R(CC):
    cm12=[[[CC[0][0][0], CC[0][0][1], CC[2][2][2]], [CC[0][1][0], CC[0][1][1], CC[2][2][1]], [CC[0][2][0], CC[0][2][1], CC[2][2][0]]], #red     
          [[CC[5][2][2], CC[5][2][1], CC[5][2][0]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[1][2][0], CC[1][2][1], CC[1][2][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[2][0][2]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[1][0][2], CC[1][0][1], CC[1][0][0]]], #white    
          [[CC[3][0][2], CC[3][1][2], CC[3][2][2]], [CC[3][0][1], CC[3][1][1], CC[3][2][1]], [CC[3][0][0], CC[3][1][0], CC[3][2][0]]], #green    
          [[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[5][0][0], CC[5][0][1], CC[5][0][2]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[0][2][2], CC[0][1][2], CC[0][0][2]]]] #yellow  
    return cm12

def Rrev(CC):
    cm11=[[[CC[0][0][0], CC[0][0][1], CC[5][2][2]], [CC[0][1][0], CC[0][1][1], CC[5][2][1]], [CC[0][2][0], CC[0][2][1], CC[5][2][0]]], #red     
          [[CC[2][2][2], CC[2][2][1], CC[2][2][0]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[1][2][0], CC[1][2][1], CC[1][2][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[2][0][2]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[0][2][2], CC[0][1][2], CC[0][0][2]]], #white    
          [[CC[3][2][0], CC[3][1][0], CC[3][0][0]], [CC[3][2][1], CC[3][1][1], CC[3][0][1]], [CC[3][2][2], CC[3][1][2], CC[3][0][2]]], #green    
          [[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[5][0][0], CC[5][0][1], CC[5][0][2]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[1][0][2], CC[1][0][1], CC[1][0][0]]]] #yellow   
    return cm11

def D(CC):
    cm13=[[[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][2], CC[1][1][2], CC[1][2][2]], [CC[1][0][1], CC[1][1][1], CC[1][2][1]], [CC[1][0][0], CC[1][1][0], CC[1][2][0]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[4][2][0]], [CC[2][1][0], CC[2][1][1], CC[4][1][0]], [CC[2][2][0], CC[2][2][1], CC[4][0][0]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[2][0][2]], [CC[3][1][0], CC[3][1][1], CC[2][1][2]], [CC[3][2][0], CC[3][2][1], CC[2][2][2]]], #green    
          [[CC[5][0][0], CC[4][0][1], CC[4][0][2]], [CC[5][1][0], CC[4][1][1], CC[4][1][2]], [CC[5][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[3][2][2], CC[5][0][1], CC[5][0][2]], [CC[3][1][2], CC[5][1][1], CC[5][1][2]], [CC[3][0][2], CC[5][2][1], CC[5][2][2]]]] #yellow  
    return cm13

def Drev(CC):
    cm14=[[[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][2][0], CC[1][1][0], CC[1][0][0]], [CC[1][2][1], CC[1][1][1], CC[1][0][1]], [CC[1][2][2], CC[1][1][2], CC[1][0][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[3][0][2]], [CC[2][1][0], CC[2][1][1], CC[3][1][2]], [CC[2][2][0], CC[2][2][1], CC[3][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[5][2][0]], [CC[3][1][0], CC[3][1][1], CC[5][1][0]], [CC[3][2][0], CC[3][2][1], CC[5][0][0]]], #green    
          [[CC[2][2][2], CC[4][0][1], CC[4][0][2]], [CC[2][1][2], CC[4][1][1], CC[4][1][2]], [CC[2][0][2], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[4][0][0], CC[5][0][1], CC[5][0][2]], [CC[4][1][0], CC[5][1][1], CC[5][1][2]], [CC[4][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow   
    return cm14

def U(CC):
    cm18=[[[CC[0][0][2], CC[0][1][2], CC[0][2][2]], [CC[0][0][1], CC[0][1][1], CC[0][2][1]], [CC[0][0][0], CC[0][1][0], CC[0][2][0]]], #red
          [[CC[1][0][0], CC[1][0][1], CC[1][0][2]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[1][2][0], CC[1][2][1], CC[1][2][2]]], #orange
          [[CC[3][0][0], CC[2][0][1], CC[2][0][2]], [CC[3][1][0], CC[2][1][1], CC[2][1][2]], [CC[3][2][0], CC[2][2][1], CC[2][2][2]]], #white
          [[CC[5][2][2], CC[3][0][1], CC[3][0][2]], [CC[5][1][2], CC[3][1][1], CC[3][1][2]], [CC[5][0][2], CC[3][2][1], CC[3][2][2]]], #green
          [[CC[4][0][0], CC[4][0][1], CC[2][2][0]], [CC[4][1][0], CC[4][1][1], CC[2][1][0]], [CC[4][2][0], CC[4][2][1], CC[2][0][0]]], #blue
          [[CC[5][0][0], CC[5][0][1], CC[4][0][2]], [CC[5][1][0], CC[5][1][1], CC[4][1][2]], [CC[5][2][0], CC[5][2][1], CC[4][2][2]]]] #yellow
    return cm18

def Urev(CC):
    cm17=[[[CC[0][2][0], CC[0][1][0], CC[0][0][0]], [CC[0][2][1], CC[0][1][1], CC[0][0][1]], [CC[0][2][2], CC[0][1][2], CC[0][0][2]]], #red     
          [[CC[1][0][0], CC[1][0][1], CC[1][0][2]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[1][2][0], CC[1][2][1], CC[1][2][2]]], #orange    
          [[CC[4][2][2], CC[2][0][1], CC[2][0][2]], [CC[4][1][2], CC[2][1][1], CC[2][1][2]], [CC[4][0][2], CC[2][2][1], CC[2][2][2]]], #white    
          [[CC[2][0][0], CC[3][0][1], CC[3][0][2]], [CC[2][1][0], CC[3][1][1], CC[3][1][2]], [CC[2][2][0], CC[3][2][1], CC[3][2][2]]], #green    
          [[CC[4][0][0], CC[4][0][1], CC[5][0][2]], [CC[4][1][0], CC[4][1][1], CC[5][1][2]], [CC[4][2][0], CC[4][2][1], CC[5][2][2]]], #blue    
          [[CC[5][0][0], CC[5][0][1], CC[3][2][0]], [CC[5][1][0], CC[5][1][1], CC[3][1][0]], [CC[5][2][0], CC[5][2][1], CC[3][0][0]]]] #yellow   
    return cm17

def toPddlState(CC):
    cube1 = '(cube1 '+CC[0][0][0] + ' ' +CC[2][0][0]+ ' ' +CC[4][0][2]+')'
    cube2 = '(cube2 '+CC[1][2][2] + ' ' +CC[2][0][2]+ ' ' +CC[4][0][0]+')'
    cube3 = '(cube3 '+CC[0][2][0] + ' ' +CC[5][0][2]+ ' ' +CC[4][2][2]+')'
    cube4 = '(cube4 '+CC[1][2][0] + ' ' +CC[5][0][0]+ ' ' +CC[4][2][0]+')'
    cube5 = '(cube5 '+CC[0][0][2] + ' ' +CC[2][2][0]+ ' ' +CC[3][0][0]+')'
    cube6 = '(cube6 '+CC[1][0][2] + ' ' +CC[2][2][2]+ ' ' +CC[3][0][2]+')'
    cube7 = '(cube7 '+CC[0][2][2] + ' ' +CC[5][2][2]+ ' ' +CC[3][2][0]+')'
    cube8 = '(cube8 '+CC[1][0][0] + ' ' +CC[5][2][0]+ ' ' +CC[3][2][2]+')'

    edge12 = '(edge12 '+CC[2][0][1]+ ' ' +CC[4][0][1]+')'
    edge24 = '(edge24 '+CC[1][2][1]+ ' ' +CC[4][1][0]+')'
    edge34 = '(edge34 '+CC[5][0][1]+ ' ' +CC[4][2][1]+')'
    edge13 = '(edge13 '+CC[0][1][0]+ ' ' +CC[4][1][2]+')'

    edge15 = '(edge15 '+CC[0][0][1]+ ' ' +CC[2][1][0]+')'
    edge26 = '(edge26 '+CC[1][1][2]+ ' ' +CC[2][1][2]+')'
    edge48 = '(edge48 '+CC[1][1][0]+ ' ' +CC[5][1][0]+')'
    edge37 = '(edge37 '+CC[0][2][1]+ ' ' +CC[5][1][2]+')'

    edge56 = '(edge56 '+CC[2][2][1]+ ' ' +CC[3][0][1]+')'
    edge68 = '(edge68 '+CC[1][0][1]+ ' ' +CC[3][1][2]+')'
    edge78 = '(edge78 '+CC[5][2][1]+ ' ' +CC[3][2][1]+')'
    edge57 = '(edge57 '+CC[0][1][2]+ ' ' +CC[3][1][0]+')'

    var_to_append = [cube1,cube2,cube3,cube4,cube5,cube6,cube7,cube8,edge12,edge24,edge34,edge13,edge15,edge26,edge48,edge37,edge56,edge68,edge78,edge57 ]
    return var_to_append

cube_actions = {
    'U': U,
    'Urev': Urev,
    'D': D,
    'Drev': Drev,
    'F': F,
    'Frev': Frev,
    'B': B,
    'Brev': Brev,
    'R': R,
    'Rrev': Rrev,
    'L': L,
    'Lrev': Lrev,

    'U2': lambda x: U(U(x)),
    'D2': lambda x: D(D(x)),
    'F2': lambda x: F(F(x)),
    'B2': lambda x: B(B(x)),
    'R2': lambda x: R(R(x)),
    'L2': lambda x: L(L(x)),
}

def check_not_optimal(face, last_face, second_to_last_face):
    # print(face, last_face, second_to_last_face)
    if face == last_face:
        return True
    if face == second_to_last_face:
        if ((face in ['F','B']) and (last_face in ['F', 'B'])) or ((face in ['L', 'R']) and (last_face in ['L', 'R'])) or ((face in ['U', 'D']) and (last_face in ['U', 'D'])):
            return True
    return False

def genRandomState(moves_to_shuffle, actions):
    move_list = []
    CC = cubeInit()
    for i in range(moves_to_shuffle):
        move = random.choice(actions)

        if i > 1:
            current_move = move
            last_move = move_list[-1]
            second_to_last_move = move_list[-2]
            while check_not_optimal(current_move[0].upper(), last_move[0].upper(), second_to_last_move[0].upper()):
                move = random.choice(actions)
                current_move = move
        if i > 0:
            last_move = move_list[-1]
            while move[0] == last_move[0]:
                move = random.choice(actions)

        move_list.append(move)
        CC = cube_actions[move](CC)

    return CC, move_list

def toPddl(CC, problem_name):
    init_facts = toPddlState(CC)

    problem_pddl = '''(define
(problem {problem_name})
(:domain rubiks-cube)
(:objects yellow white blue green orange red)
(:init
    {init}
)
(:goal
    (and
        (cube1 red white blue)
        (cube2 orange white blue)
        (cube3 red yellow blue)
        (cube4 orange yellow blue)
        (cube5 red white green)
        (cube6 orange white green)
        (cube7 red yellow green)
        (cube8 orange yellow green)

        (edge12 white blue)
        (edge24 orange blue)
        (edge34 yellow blue)
        (edge13 red blue)

        (edge15 red white)
        (edge26 orange white)
        (edge48 orange yellow)
        (edge37 red yellow)

        (edge56 white green)
        (edge68 orange green)
        (edge78 yellow green)
        (edge57 red green)

    )
)
)
'''.format(problem_name = problem_name, init = '\n    '.join(init_facts))
    return problem_pddl

def generate(moves_to_shuffle, actions):
    CC, gen_actions = genRandomState(moves_to_shuffle, actions)
    pddl = toPddl(CC, 'rubiks-cube-shuffle-{0}'.format(moves_to_shuffle))
    print(gen_actions)

    plan_actions = []
    for a in gen_actions[::-1]:
        if a.endswith('rev'):
            plan_actions += [a[:-3]]
        else:
            plan_actions += [a + 'rev']
    plan = '(' + ')\n('.join(plan_actions) + ')\n'
    return pddl, plan

def usage():
    print('Usage: {0} [OPTIONS] number-of-moves'.format(sys.argv[0]))
    sys.exit(-1)

if __name__ == '__main__':
    double_actions = False
    moves = None
    validate = None
    output = None
    plan_output = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'do:s:',
                                   ['double-actions', 'output=',
                                    'plan-output=', 'seed='])
    except getopt.GetoptError as err:
        print('Error:', err)
        usage()

    if len(args) != 1:
        usage()
    moves = int(args[0])
    for o, a in opts:
        if o in ['-d', '--double-actions']:
            double_actions = True
        elif o in ['-o', '--output']:
            output = a
        elif o in ['--plan-output']:
            plan_output = a
        elif o in ['--validate']:
            validate = a
        elif o in ['-s', '--seed']:
            random.seed(int(a))

    if double_actions:
        actions = cube_actions.keys()
    else:
        actions = [x for x in cube_actions.keys() if not x.endswith('2')]
    actions = sorted(actions)

    pddl, plan = generate(moves, actions)
    pddl = ';; Generated with {0}\n'.format(' '.join(sys.argv)) + pddl

    if output is None:
        print(pddl)
    else:
        with open(output, 'w') as fout:
            fout.write(pddl)

    if plan_output is not None:
        with open(plan_output, 'w') as fout:
            fout.write(plan)
