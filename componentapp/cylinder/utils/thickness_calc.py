"""Calculate inner thickness."""
from math import exp, atan, cos
from django.db import connection
from reporter.models import CylinderState, Report

def cylinder_t(P, S, D, C_A, report_id, E=1.0):
    """Calculate thickness as per ASME DIV I

    Parameters
    ----------
    P : float psi
        Design pressure or max allowable working pressure.
    S : float psi
        Stress value of material.
    D : float inches
        Inside diameter.
    CA : float inches
        Corrosion allowance.
    E : float max 1.0
        Joint Efficiency.

    Returns
    -------
    float
        Description of returned object.

    """
    # return (D/2) * (exp(P / (S * E)) - 1
    # R = (D + 2.0 * C_A) / 2.0
    # t_wo_allowance = (P * R) / (S * 1000 * E - 0.6 * P)
    # t_w_allowance = t_wo_allowance + C_A
    # return t_w_allowance

    # Process to calculate using Postgres Procedure
    # with connection.cursor() as cursor:
    #     cursor.callproc('cylinder_t', [P, S, D, C_A, E])
    #     return cursor.fetchall()[0][0]
    upper_part = float(P * ( (D+2*C_A)/2.0 ) )
    lower_part = float((S *1000* E) - (0.6 * P))
    t_inter = upper_part/lower_part
    t = t_inter + C_A
    # think about how you can save the calculation steps later
    calc_steps = CylinderState(
        report = Report.objects.get(id=report_id),
        P = P,
        D = D,
        C_A = C_A,
        R = D/2.0,
        S = S,
        E = E,
        t_inter = t_inter,
        t = t
    )
    calc_steps.save()
    return t
    # return (upper_part/lower_part) + C_A

def conical_t(D, P, S, D_l, D_s, L_c, CA, E=1.0):
    D_l += 2 * CA
    D_s += 2 * CA
    alpha = atan(0.5 * (D_l - D_s) / L_c)
    t_wo_allowance = (P * D) / (2 * cos(alpha) * (S * E * 1000 - 0.6 * P))
    return t_wo_allowance
