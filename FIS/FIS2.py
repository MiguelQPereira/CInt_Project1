import simpful as sf
import sys
import os

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout  # Save a reference to the original standard output
        sys.stdout = open(os.devnull, 'w')  # Redirect stdout to null

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout  # Reset to original stdout


def FS_pt2 (cpu_load, mem_use, net_input):

    output_formula = """
    if c > 0.85 or m > 0.85:
        result = -1
    else:
        result = max(-1, min(1, (1 - 1.5 * (c**2 + m**2)) - 1.0 * i))
    """

    #first fuzzy system:
    #
    # inputs: CPU Load, Mem Use and Input Net
    #
    #
    with HiddenPrints():
        FS1 = sf.FuzzySystem(verbose=False)
    # CPU Load
    S1_1 = sf.FuzzySet(points=[[0, 1.], [0.40, 1.], [0.50, 0], [1., 0]], term="low_load")
    S1_2 = sf.FuzzySet(points=[[0.4, 0], [0.45, 1.], [0.60, 1.], [0.75, 0]], term="medium_load")
    S1_3 = sf.FuzzySet(points=[[0.7, 0], [0.80, 1.], [1, 1.]], term="high_load")
    FS1.add_linguistic_variable("CPU_LOAD", sf.LinguisticVariable([S1_1, S1_2, S1_3]))

    # MEM USE
    S2_1 = sf.FuzzySet(points=[[0, 1.], [0.40, 1.], [0.50, 0]], term="low_use")
    S2_2 = sf.FuzzySet(points=[[0.4, 0], [0.45, 1.], [0.60, 1.], [0.75, 0]], term="medium_use")
    S2_3 = sf.FuzzySet(points=[[0.7, 0], [0.80, 1.], [1, 1.]], term="high_use")
    FS1.add_linguistic_variable("MEM_USE", sf.LinguisticVariable([S2_1, S2_2, S2_3]))

    # INPUT NET
    S3_1 = sf.FuzzySet(points=[[0, 1.], [0.20, 1.], [0.40, 0]], term="low_input")
    S3_2 = sf.FuzzySet(points=[[0.3, 0], [0.45, 1.], [0.55, 1.], [0.80, 0]], term="medium_input")
    S3_3 = sf.FuzzySet(points=[[0.70, 0], [0.85, 1.], [1, 1.]], term="high_input")
    FS1.add_linguistic_variable("NET_INPUT", sf.LinguisticVariable([S3_1, S3_2, S3_3]))

    FS1.produce_figure(outputfile="memberships_FS2.png", element_dict={
        "NET_INPUT": None, 
        "CPU_LOAD": None,
        "MEM_USE": None})

    with HiddenPrints():
        FS1.set_output_function("LOWER_CLP", "-1*(0.7*MEM_USE*NET_INPUT+0.5*CPU_LOAD)")
        FS1.set_output_function("MAINTAIN_CLP", "(1.0*CPU_LOAD/0.25*(MEM_USE*NET_INPUT))")
        FS1.set_output_function("INCREASE_CLP", "1-(0.1*MEM_USE*NET_INPUT+0.3*CPU_LOAD)")

    #FS1.set_output_function("LOWER_CLP", "max(-1, min(1, (-1 + (-2 * (CPU_LOAD**2 + MEM_USE**2)) - 1.5 * NET_INPUT)))")

    #FS1.set_output_function("MAINTAIN_CLP", "max(-1, min(1, (0 - (CPU_LOAD**2 + MEM_USE**2) - 0.5 * NET_INPUT)))")

    #FS1.set_output_function("INCREASE_CLP", "max(-1, min(1, (1 - 2 * (CPU_LOAD**2 + MEM_USE**2) - 1 * NET_INPUT)))")

    ##low input
    #low load
    RULE1 = "IF (CPU_LOAD IS low_load) AND (MEM_USE IS low_use) AND (NET_INPUT IS low_input) THEN (CLP IS INCREASE_CLP)"
    RULE2 = "IF (CPU_LOAD IS low_load) AND (MEM_USE IS medium_use) AND (NET_INPUT IS low_input) THEN (CLP IS INCREASE_CLP)"
    RULE3 = "IF (CPU_LOAD IS low_load) AND (MEM_USE IS high_use) AND (NET_INPUT IS low_input) THEN (CLP IS MAINTAIN_CLP)"
    #medium load
    RULE4 = "IF (CPU_LOAD IS medium_load) AND (MEM_USE IS low_use) AND (NET_INPUT IS low_input) THEN (CLP IS INCREASE_CLP)"
    RULE5 = "IF (CPU_LOAD IS medium_load) AND (MEM_USE IS medium_use) AND (NET_INPUT IS low_input) THEN (CLP IS INCREASE_CLP)"
    RULE6 = "IF (CPU_LOAD IS medium_load) AND (MEM_USE IS high_use) AND (NET_INPUT IS low_input) THEN (CLP IS MAINTAIN_CLP)"
    #high load
    RULE7 = "IF (CPU_LOAD IS high_load) AND (MEM_USE IS low_use) AND (NET_INPUT IS low_input) THEN (CLP IS INCREASE_CLP)"
    RULE8 = "IF (CPU_LOAD IS high_load) AND (MEM_USE IS medium_use) AND (NET_INPUT IS low_input) THEN (CLP IS INCREASE_CLP)"
    RULE9 = "IF (CPU_LOAD IS high_load) AND (MEM_USE IS high_use) AND (NET_INPUT IS low_input) THEN (CLP IS MAINTAIN_CLP)"



    #medium input
    #low load
    RULE10 = "IF (CPU_LOAD IS low_load) AND (MEM_USE IS low_use) AND (NET_INPUT IS medium_input) THEN (CLP IS INCREASE_CLP)"
    RULE11 = "IF (CPU_LOAD IS low_load) AND (MEM_USE IS medium_use) AND (NET_INPUT IS medium_input) THEN (CLP IS MAINTAIN_CLP)"
    RULE12 = "IF (CPU_LOAD IS low_load) AND (MEM_USE IS high_use) AND (NET_INPUT IS medium_input) THEN (CLP IS MAINTAIN_CLP)"
    #medium load
    RULE13 = "IF (CPU_LOAD IS medium_load) AND (MEM_USE IS low_use) AND (NET_INPUT IS medium_input) THEN (CLP IS INCREASE_CLP)"
    RULE14 = "IF (CPU_LOAD IS medium_load) AND (MEM_USE IS medium_use) AND (NET_INPUT IS medium_input) THEN (CLP IS MAINTAIN_CLP)"
    RULE15 = "IF (CPU_LOAD IS medium_load) AND (MEM_USE IS high_use) AND (NET_INPUT IS medium_input) THEN (CLP IS LOWER_CLP)"
    #high load
    RULE16 = "IF (CPU_LOAD IS high_load) AND (MEM_USE IS low_use) AND (NET_INPUT IS medium_input) THEN (CLP IS MAINTAIN_CLP)"
    RULE17 = "IF (CPU_LOAD IS high_load) AND (MEM_USE IS medium_use) AND (NET_INPUT IS medium_input) THEN (CLP IS MAINTAIN_CLP)"
    RULE18 = "IF (CPU_LOAD IS high_load) AND (MEM_USE IS high_use) AND (NET_INPUT IS medium_input) THEN (CLP IS LOWER_CLP)"



    #high input
    #low load
    RULE19 = "IF (CPU_LOAD IS low_load) AND (MEM_USE IS low_use) AND (NET_INPUT IS high_input) THEN (CLP IS MAINTAIN_CLP)"
    RULE20 = "IF (CPU_LOAD IS low_load) AND (MEM_USE IS medium_use) AND (NET_INPUT IS high_input) THEN (CLP IS LOWER_CLP)"
    RULE21 = "IF (CPU_LOAD IS low_load) AND (MEM_USE IS high_use) AND (NET_INPUT IS high_input) THEN (CLP IS LOWER_CLP)"
    #medium load
    RULE22 = "IF (CPU_LOAD IS medium_load) AND (MEM_USE IS low_use) AND (NET_INPUT IS high_input) THEN (CLP IS MAINTAIN_CLP)"
    RULE23 = "IF (CPU_LOAD IS medium_load) AND (MEM_USE IS medium_use) AND (NET_INPUT IS high_input) THEN (CLP IS LOWER_CLP)"
    RULE24 = "IF (CPU_LOAD IS medium_load) AND (MEM_USE IS high_use) AND (NET_INPUT IS high_input) THEN (CLP IS LOWER_CLP)"
    #high load
    RULE25 = "IF (CPU_LOAD IS high_load) AND (MEM_USE IS low_use) AND (NET_INPUT IS high_input) THEN (CLP IS LOWER_CLP)"
    RULE26 = "IF (CPU_LOAD IS high_load) AND (MEM_USE IS medium_use) AND (NET_INPUT IS high_input) THEN (CLP IS LOWER_CLP)"
    RULE27 = "IF (CPU_LOAD IS high_load) AND (MEM_USE IS high_use) AND (NET_INPUT IS high_input) THEN (CLP IS LOWER_CLP)"

    FS1.add_rules([RULE1, RULE2, RULE3, RULE4, RULE5, RULE6, RULE7, RULE8, RULE9, RULE10, RULE11, RULE12, RULE13, RULE14, RULE15, RULE16, RULE17, RULE18, RULE19, RULE20, RULE21, RULE22, RULE23, RULE24, RULE25, RULE26, RULE27])
    #for i in range(0, 100, 5):
    #    for j in range(0, 100, 5):
    #        for k in range(0, 100, 5):
    #            FS1.set_variable("CPU_LOAD", i/100)
    #            FS1.set_variable("MEM_USE", j/100)
    #            FS1.set_variable("NET_INPUT", k/100)
    #            print(FS1.Sugeno_inference(['CLP']))
    FS1.set_variable("CPU_LOAD", cpu_load)
    FS1.set_variable("MEM_USE",mem_use)
    FS1.set_variable("NET_INPUT", net_input)

    
    result = FS1.Sugeno_inference(['CLP'], verbose=False)

    return result