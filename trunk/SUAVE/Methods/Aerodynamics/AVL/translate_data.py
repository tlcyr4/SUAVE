# translate_data.py
# 
# Created:  Mar 2015, T. Momose
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import numpy as np

import SUAVE
from SUAVE.Core import Data, Units
from .Data.Cases import Run_Case

def translate_conditions_to_cases(avl,conditions):
    """ SUAVE.Methods.Aerodynamics.AVL.translate_data.translate_conditions_to_cases(avl,conditions)
        Takes SUAVE Conditions() data structure and translates to a Container of
        avl Run_Case()s.
        
        Inputs:
            avl - AVL object
            conditions. - SUAVE conditions
                freestream.
                    mach_number - mach number
                    velocity - velocity
                    density - density
                aerodynamics.
                    angle_of_attack - aoa
                    side_slip_angle - side slip angle
            
        Outputs:
            cases - container of AVL cases
    """
    # set up aerodynamic Conditions object
    cases = Run_Case.Container()

    for i in range(conditions._size):
        case = Run_Case()
        case.tag  = avl.settings.filenames.case_template.format(avl.current_status.batch_index,i+1)
        case.mass = conditions.weights.total_mass[i][0]
        case.conditions.freestream.mach     = conditions.freestream.mach_number[i][0]
        case.conditions.freestream.velocity = conditions.freestream.velocity[i][0]
        case.conditions.freestream.density  = conditions.freestream.density[i][0]
        case.conditions.freestream.gravitational_acceleration = conditions.freestream.gravity[i][0]
        case.conditions.aerodynamics.angle_of_attack = conditions.aerodynamics.angle_of_attack[i][0]/Units.deg
        case.conditions.aerodynamics.side_slip_angle = conditions.aerodynamics.side_slip_angle[i][0]
        case.stability_and_control.control_deflections = np.array([[]]) # TODO How to do this from the SUAVE side?
        cases.append_case(case)

    return cases

def translate_results_to_conditions(cases,results):
    """ SUAVE.Methods.Aerodynamics.AVL.translate_data.translate_results_to_conditions(avl,conditions)
        Takes avl results structure containing the results of each run case stored
        each in its own Data() object. Translates into the Conditions() data structure.
        
        Inputs:
            cases[i]. - AVL cases
                conditions. - SUAVE conditions
                freestream.
                    mach_number - mach number
                    velocity - velocity
                    density - density
                    gravitational_acceleration - acceleration due to gravity
                aerodynamics.
                    angle_of_attack - aoa
                    side_slip_angle - side slip angle
                mass
            results - results from AVL
            
        Outputs:
            res. - SUAVE results
                freestream.
                    mach_number
                    gravity
                    density
                aerodynamics.
                    roll_moment_coefficient
                    pitch_moment_coefficient
                    yaw_moment_coefficient
                    drag_breakdown
                        induced.
                            total
                            efficiency_factor
                    cz_alpha
                    cy_alpha
                    cl_alpha
                    cm_alpha
                    cn_alpha
                    cz_beta
                    cy_beta
                    cl_beta
                    cm_beta
                    cn_beta
                    neutral_point
                weights.total_mass
    """
    # set up aerodynamic Conditions object
    res = SUAVE.Analyses.Mission.Segments.Conditions.Aerodynamics()
    ones_1col = res.ones_row(1)
    # add missing entries
    res.aerodynamics.roll_moment_coefficient  = ones_1col * 0
    res.aerodynamics.pitch_moment_coefficient = ones_1col * 0
    res.aerodynamics.yaw_moment_coefficient   = ones_1col * 0
    res.aerodynamics.drag_breakdown.induced   = SUAVE.Analyses.Mission.Segments.Conditions.Conditions()
    res.aerodynamics.drag_breakdown.induced.total = ones_1col * 0
    res.aerodynamics.drag_breakdown.induced.efficiency_factor = ones_1col * 0
    res.aerodynamics.cz_alpha                 = ones_1col * 0
    res.aerodynamics.cy_alpha                 = ones_1col * 0
    res.aerodynamics.cl_alpha                 = ones_1col * 0
    res.aerodynamics.cm_alpha                 = ones_1col * 0
    res.aerodynamics.cn_alpha                 = ones_1col * 0
    res.aerodynamics.cz_beta                  = ones_1col * 0
    res.aerodynamics.cy_beta                  = ones_1col * 0
    res.aerodynamics.cl_beta                  = ones_1col * 0
    res.aerodynamics.cm_beta                  = ones_1col * 0
    res.aerodynamics.cn_beta                  = ones_1col * 0
    res.aerodynamics.neutral_point            = ones_1col * 0

    res.expand_rows(len(cases))

    # Move results data to the Conditions data structure       
    for i,case_res in enumerate(results):
        res.freestream.velocity[i][0]          = cases[i].conditions.freestream.velocity
        res.freestream.mach_number[i][0]       = cases[i].conditions.freestream.mach
        res.freestream.gravity[i][0]           = cases[i].conditions.freestream.gravitational_acceleration
        res.freestream.density[i][0]           = cases[i].conditions.freestream.density
        res.aerodynamics.angle_of_attack[i][0] = cases[i].conditions.aerodynamics.angle_of_attack * Units.deg
        res.aerodynamics.side_slip_angle[i][0] = cases[i].conditions.aerodynamics.side_slip_angle * Units.deg      
        res.weights.total_mass[i][0]           = cases[i].mass

        res.aerodynamics.roll_moment_coefficient[i][0] = case_res.aerodynamics.roll_moment_coefficient
        res.aerodynamics.pitch_moment_coefficient[i][0] = case_res.aerodynamics.pitch_moment_coefficient
        res.aerodynamics.yaw_moment_coefficient[i][0] = case_res.aerodynamics.yaw_moment_coefficient
        res.aerodynamics.lift_coefficient[i][0] = case_res.aerodynamics.total_lift_coefficient
        res.aerodynamics.drag_breakdown.induced.total[i][0] = case_res.aerodynamics.induced_drag_coefficient
        res.aerodynamics.drag_breakdown.induced.efficiency_factor[i][0] = case_res.aerodynamics.span_efficiency_factor
        res.aerodynamics.cz_alpha[i][0] = -case_res.stability.alpha_derivatives.lift_curve_slope
        res.aerodynamics.cy_alpha[i][0] = case_res.stability.alpha_derivatives.side_force_derivative
        res.aerodynamics.cl_alpha[i][0] = case_res.stability.alpha_derivatives.roll_moment_derivative
        res.aerodynamics.cm_alpha[i][0] = case_res.stability.alpha_derivatives.pitch_moment_derivative
        res.aerodynamics.cn_alpha[i][0] = case_res.stability.alpha_derivatives.yaw_moment_derivative
        res.aerodynamics.cz_beta[i][0] = -case_res.stability.beta_derivatives.lift_coefficient_derivative
        res.aerodynamics.cy_beta[i][0] = case_res.stability.beta_derivatives.side_force_derivative
        res.aerodynamics.cl_beta[i][0] = case_res.stability.beta_derivatives.roll_moment_derivative
        res.aerodynamics.cm_beta[i][0] = case_res.stability.beta_derivatives.pitch_moment_derivative
        res.aerodynamics.cn_beta[i][0] = case_res.stability.beta_derivatives.yaw_moment_derivative
        res.aerodynamics.neutral_point[i][0] = case_res.stability.neutral_point

    return res