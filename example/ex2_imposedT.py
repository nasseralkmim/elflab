__author__ = 'Nasser'

import numpy as np
import elasticity2d

meshName = 'patch'

material = {'E':1000.0, 'nu':0.3}

def body_forces(x1, x2):
    return np.array([
        0.0,
        0.0,
    ])

def traction_imposed(x1, x2):
    return {
        ('line', 3):[-1.0, 0.0],
        ('line', 1):[1.0, 0.0]
    }

def displacement_imposed(x1, x2):
    return {
        ('node', 0):[0.0, 0.0],
        ('node', 1):['free', 0.0]

    }

elasticity2d.solver(meshName,
                              material,
                              body_forces,
                              traction_imposed,
                              displacement_imposed,
                              plotUndeformed={'Domain':True,
                                              'Elements':True,
                                              'NodeLabel':True,
                                              'EdgesLabel':False,
                                              'ElementLabel':False},
                              plotStress={'s11':True,
                                          's22':False,
                                          's12':False,
                                          'sPmax':False,
                                          'sPmin':False},
                              plotDeformed={'DomainUndeformed':True,
                                            'ElementsUndeformed':True,
                                            'DomainDeformed':True,
                                            'ElementsDeformed':True,
                                            'DeformationMagf': 100}
                              )



