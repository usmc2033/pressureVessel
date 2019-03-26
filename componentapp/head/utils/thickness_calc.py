"""Calculate inner thickness."""
from math import exp, atan, cos, pi, pow

def head_t(P, S, diameterWithOutCorrosion, corrosionAllowance,position, report_id,E=1.0):
    """Calculate thickness as per ASME DIV I

    Parameters
    ----------
    P : float
        Design Pressure or max. allowable working pressure psi.
    S : int
        Stress value of material psi.
    D : inch float
        Inside diameter .
    CA : float
        Corrosion Allowance.
    E : float max 1 
        Joint efficiency.

    Returns
    -------
    float
        thickness.
    """

    upper_part = float(P * diameterWithOutCorrosion)
    lower_part = float( (2 * S * 1000 * E) - (0.2 * P) )
    thicknessWithCorrosion =  (upper_part/lower_part) + corrosionAllowance

    heightWithOutCorrosion = diameterWithOutCorrosion/4 
    L = 81.0
    r = 15.3

    '''
    From pdf Examples Problem Manual VIII-1.pdf
    page 39 Example E4.3.5 - Elliptical Head
    Determine the elliptical head diameter to height ratio, k , and adjust for corrosion allowance.
    '''

    kFactor = diameterWithOutCorrosion/(2*heightWithOutCorrosion)
    diameterWithCorrosion = diameterWithOutCorrosion + 2*corrosionAllowance
    lengthWithCorrosion = L + corrosionAllowance
    rWithCorrosion = r + corrosionAllowance
    thicknessWithOutCorrosion = thicknessWithCorrosion - corrosionAllowance

    '''
    Section VIII, Division 1 Solution
    Evaluate per Mandatory Appendix 1-4(c). Note, the rules of UG-32(d) can also be used to evaluate ellipsoidal heads. However, the rules contained in this paragraph are only applicable for a specific geometry, i.e. half the minor axis (inside depth of head minus the skirt) equals one–fourth of the inside diameter of the head skirt. Additionally, if the ratio ts / L >= 0.002 , is not satisfied, the rules of Mandatory Appendix 1-4(f) shall also be met.
    '''
    
    KFactor = (1/6.0)*( 2 + pow(kFactor,2))
    MAWPressure = (2 * S * E * thicknessWithOutCorrosion) / ((KFactor*diameterWithCorrosion) + (0.2 * thicknessWithOutCorrosion))

    comparisionFactor = thicknessWithOutCorrosion/L
    msg = ""
    if comparisionFactor >= 0.002:
        msg = "the rules of 1- 4(f) are not required"
    else :
        msg = "the rules of Mandatory Appendix 1-4(f) shall also be met"

    return thicknessWithCorrosion,MAWPressure,msg

def center_of_gravity(headDiameterOutside,density,skirtHeight,headThickness,Sf=2):
    headHeightOutside = headDiameterOutside/4
    headVolumeOutside = ((2*pi*pow((headDiameterOutside/2.0),2)*(headHeightOutside))/3)+(pi*pow((headDiameterOutside/2.0),2)*Sf)
    headIndividualCGOutside = (4*headHeightOutside)/(3*pi)
    cgFromDatumOutside = (skirtHeight-headIndividualCGOutside)

    headDiameterInside = headDiameterOutside-headThickness
    headHeightInside = headDiameterInside/4
    headVoulmeInside = ((2*pi*pow((headDiameterInside/2.0),2)*(headHeightInside))/3)+(pi*pow((headDiameterInside/2.0),2)*Sf)
    headIndividualCGInside = (4*headHeightInside)/(3*pi)
    cgFromDatumInside = (skirtHeight-headIndividualCGInside)

    netHeadVolume = headVolumeOutside-headVoulmeInside
    netCGFromDatum = (cgFromDatumInside+cgFromDatumOutside)/2.0

    newWeight = netHeadVolume * density
    weightTimesCG = newWeight*netCGFromDatum

    return weightTimesCG,newWeight
